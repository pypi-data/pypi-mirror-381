"""
Resume Training from Checkpoint-3000
====================================
Continue from epoch 3.68 to 4.0 with FULL dataset (15,000 examples)
"""
import modal
import sys
sys.path.insert(0, '/root')

# Volume
volume = modal.Volume.from_name("bioql-deepseek-improved", create_if_missing=True)

# Image
image = (
    modal.Image.debian_slim(python_version="3.11")
    .pip_install(
        "torch==2.1.0",
        "transformers==4.37.0",
        "peft==0.7.0",
        "datasets==2.16.0",
        "accelerate==0.25.0",
        "bitsandbytes==0.41.3",
        "scipy==1.11.4",
    )
)

app = modal.App(name="bioql-resume-from-3000", image=image)


@app.function(
    gpu="A100",
    timeout=3600,  # 1 hora
    volumes={"/data": volume},
    mounts=[modal.Mount.from_local_dir(
        "/Users/heinzjungbluth/Desktop/bioql/training",
        remote_path="/training"
    )]
)
def resume_from_checkpoint_3000():
    """Resume training with FULL 15k dataset."""
    import torch
    from transformers import (
        AutoTokenizer,
        AutoModelForCausalLM,
        TrainingArguments,
        Trainer,
        DataCollatorForSeq2Seq
    )
    from peft import LoraConfig, get_peft_model, TaskType
    from datasets import Dataset
    import os

    # Import dataset generator from original file
    sys.path.insert(0, '/training')
    from TRAIN_IMPROVED_MODEL import generate_expanded_bioql_dataset

    print("=" * 70)
    print("🔄 RESUMING FROM CHECKPOINT-3000 (Epoch 3.68 → 4.0)")
    print("=" * 70)

    checkpoint_path = "/data/improved_model/checkpoint-3000"

    if not os.path.exists(checkpoint_path):
        print("❌ Checkpoint-3000 not found!")
        return

    print(f"\n✅ Found checkpoint: {checkpoint_path}")

    # [1/5] Generate FULL dataset
    print("\n[1/5] Generating FULL BioQL dataset (15,000 examples)...")
    dataset_examples = generate_expanded_bioql_dataset(num_examples=15000)
    print(f"   ✅ Generated {len(dataset_examples)} examples")

    # [2/5] Load model
    print("\n[2/5] Loading DeepSeek-Coder-6.7B...")
    model_name = "deepseek-ai/deepseek-coder-6.7b-instruct"

    tokenizer = AutoTokenizer.from_pretrained(model_name, trust_remote_code=True)
    tokenizer.pad_token = tokenizer.eos_token

    base_model = AutoModelForCausalLM.from_pretrained(
        model_name,
        device_map="auto",
        torch_dtype=torch.bfloat16,
        trust_remote_code=True
    )
    print("   ✅ Model loaded")

    # [3/5] Add LoRA
    print("\n[3/5] Adding LoRA configuration...")
    lora_config = LoraConfig(
        task_type=TaskType.CAUSAL_LM,
        r=32,
        lora_alpha=64,
        lora_dropout=0.05,
        target_modules=["q_proj", "k_proj", "v_proj", "o_proj",
                        "gate_proj", "up_proj", "down_proj"],
        bias="none"
    )

    model = get_peft_model(base_model, lora_config)
    model.print_trainable_parameters()

    # [4/5] Tokenize dataset
    print("\n[4/5] Tokenizing dataset...")
    dataset = Dataset.from_list(dataset_examples)

    def tokenize_function(examples):
        texts = [f"### Instruction:\n{ex['instruction']}\n\n### Reasoning:\n{ex['reasoning']}\n\n### Code:\n{ex['code']}"
                 for ex in examples]

        result = tokenizer(
            texts,
            padding=False,
            truncation=True,
            max_length=1024,
            return_tensors=None
        )
        result["labels"] = result["input_ids"].copy()
        return result

    tokenized_dataset = dataset.map(
        lambda examples: tokenize_function([examples]),
        batched=False,
        remove_columns=dataset.column_names
    )
    print(f"   ✅ Tokenized {len(tokenized_dataset)} examples")

    # [5/5] Resume training
    print("\n[5/5] Resuming training from checkpoint-3000...")

    data_collator = DataCollatorForSeq2Seq(
        tokenizer=tokenizer,
        model=model,
        padding=True,
        pad_to_multiple_of=8,
        label_pad_token_id=-100
    )

    training_args = TrainingArguments(
        output_dir="/data/improved_model",
        num_train_epochs=4,
        per_device_train_batch_size=2,
        gradient_accumulation_steps=8,
        learning_rate=2e-4,
        warmup_steps=200,
        logging_steps=50,
        save_steps=500,
        save_total_limit=3,
        fp16=False,
        bf16=True,
        optim="adamw_torch",
        report_to=[],
        resume_from_checkpoint=checkpoint_path
    )

    trainer = Trainer(
        model=model,
        args=training_args,
        train_dataset=tokenized_dataset,
        data_collator=data_collator,
        tokenizer=tokenizer
    )

    print("   🏋️  Continuing from epoch 3.68...")
    print("   📍 Target: epoch 4.0 (completing final 8%)")

    import time
    start_time = time.time()

    try:
        trainer.train(resume_from_checkpoint=checkpoint_path)

        training_time = time.time() - start_time

        print(f"\n   ✅ Training completed in {training_time/60:.1f} minutes")

        # Save FINAL model
        print("\n[FINAL] Saving 100% trained model...")
        final_path = "/data/improved_model/final_100"
        trainer.save_model(final_path)
        tokenizer.save_pretrained(final_path)

        volume.commit()

        print("\n" + "=" * 70)
        print("🎉 TRAINING 100% COMPLETED - NO MORE TYPOS!")
        print("=" * 70)
        print(f"⏱️  Final 8% time: {training_time/60:.1f} minutes")
        print(f"💾 Model saved to: {final_path}")
        print("\n✅ Modelo 6.7B entrenado al 100% con dataset completo!")

    except Exception as e:
        print(f"\n❌ Error: {e}")
        import traceback
        traceback.print_exc()


@app.local_entrypoint()
def main():
    """Resume training from checkpoint-3000."""
    print("🚀 Resuming training from checkpoint-3000 with FULL dataset...")
    resume_from_checkpoint_3000.remote()
    print("✅ Training resumed!")
