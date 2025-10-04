"""
Resume BioQL Training from Checkpoint
======================================

Simple script to resume training from checkpoint-2000
"""

import modal

# Use existing volume
volume = modal.Volume.from_name("bioql-model-volume")

# Same image as before
image = (
    modal.Image.debian_slim(python_version="3.11")
    .pip_install(
        "torch==2.1.0",
        "transformers==4.46.0",  # Updated for Qwen2
        "datasets==2.16.0",
        "accelerate==0.25.0",
        "peft==0.7.0",
        "bitsandbytes==0.41.0",
        "scipy",
        "sentencepiece",
        "protobuf",
        "numpy<2",  # Fix numpy compatibility
    )
)

app = modal.App(name="bioql-resume", image=image)


@app.function(
    gpu="A100-40GB",
    timeout=43200,  # 12 hours
    volumes={"/data": volume},
)
def resume_training():
    """Resume training from last checkpoint."""
    import os
    import torch
    from transformers import (
        AutoTokenizer,
        AutoModelForCausalLM,
        TrainingArguments,
        Trainer,
        BitsAndBytesConfig,
    )
    from peft import LoraConfig, get_peft_model, prepare_model_for_kbit_training
    from datasets import Dataset
    import random

    print("=" * 60)
    print("Resuming BioQL Training from Checkpoint")
    print("=" * 60)
    print("")

    # Check for checkpoints
    checkpoint_dir = "/data/bioql_model"

    if not os.path.exists(checkpoint_dir):
        print(f"❌ No checkpoint directory found at {checkpoint_dir}")
        print("   Creating new training from scratch...")
        checkpoint = None
    else:
        checkpoints = [
            d for d in os.listdir(checkpoint_dir)
            if d.startswith("checkpoint-") and os.path.isdir(os.path.join(checkpoint_dir, d))
        ]

        if checkpoints:
            latest = sorted(checkpoints, key=lambda x: int(x.split("-")[1]))[-1]
            checkpoint = os.path.join(checkpoint_dir, latest)
            print(f"✅ Found checkpoint: {latest}")
            print(f"   Resuming from: {checkpoint}")
        else:
            print("⚠️  No checkpoints found, starting fresh")
            checkpoint = None

    print("")

    # Generate dataset (same as before)
    print("[1/4] Generating training data...")

    templates = {
        "bell": "Create a Bell state",
        "qft": "Run QFT on {} qubits",
        "grover": "Run Grover's algorithm",
        "protein": "Simulate {} protein folding",
        "drug": "Simulate drug binding to {}",
    }

    examples = []
    for i in range(100000):
        cat = random.choice(list(templates.keys()))
        template = templates[cat]

        if "{}" in template:
            if cat == "qft" or cat == "grover":
                task = template.format(random.randint(2, 8))
            elif cat == "protein":
                task = template.format(random.choice(["insulin", "hemoglobin"]))
            else:
                task = template.format(random.choice(["GLP1R", "DRD2"]))
        else:
            task = template

        code = f'''from bioql import quantum

result = quantum(
    "{task}",
    api_key="your_api_key",
    backend="simulator",
    shots=1000
)

print(f"Results: {{result.counts}}")'''

        examples.append({"text": f"Task: {task}\n\nCode:\n{code}"})

        if (i + 1) % 20000 == 0:
            print(f"   {i + 1:,} examples...")

    dataset = Dataset.from_list(examples)
    print(f"   ✅ {len(examples):,} examples ready")
    print("")

    # Load model
    print("[2/4] Loading model...")

    bnb_config = BitsAndBytesConfig(
        load_in_4bit=True,
        bnb_4bit_use_double_quant=True,
        bnb_4bit_quant_type="nf4",
        bnb_4bit_compute_dtype=torch.bfloat16,
    )

    tokenizer = AutoTokenizer.from_pretrained(
        "Qwen/Qwen2.5-7B-Instruct",
        trust_remote_code=True,
    )
    tokenizer.pad_token = tokenizer.eos_token

    model = AutoModelForCausalLM.from_pretrained(
        "Qwen/Qwen2.5-7B-Instruct",
        quantization_config=bnb_config,
        device_map="auto",
        trust_remote_code=True,
        torch_dtype=torch.bfloat16,
    )

    print("   ✅ Model loaded")
    print("")

    # Add LoRA
    print("[3/4] Adding LoRA...")

    model = prepare_model_for_kbit_training(model)

    lora_config = LoraConfig(
        r=16,
        lora_alpha=32,
        target_modules=["q_proj", "k_proj", "v_proj", "o_proj", "gate_proj", "up_proj", "down_proj"],
        lora_dropout=0.05,
        bias="none",
        task_type="CAUSAL_LM",
    )

    model = get_peft_model(model, lora_config)

    trainable = sum(p.numel() for p in model.parameters() if p.requires_grad)
    print(f"   ✅ LoRA ready: {trainable:,} params")
    print("")

    # Tokenize
    def tokenize(examples):
        return tokenizer(
            examples["text"],
            truncation=True,
            max_length=512,
            padding="max_length",
        )

    tokenized = dataset.map(tokenize, batched=True, remove_columns=dataset.column_names)
    print("   ✅ Dataset tokenized")
    print("")

    # Train
    print("[4/4] Training...")
    print("")

    training_args = TrainingArguments(
        output_dir="/data/bioql_model",
        num_train_epochs=5,
        per_device_train_batch_size=4,
        gradient_accumulation_steps=8,
        learning_rate=1e-5,
        warmup_steps=100,
        max_grad_norm=1.0,
        weight_decay=0.01,
        bf16=True,
        optim="paged_adamw_8bit",
        logging_steps=10,
        save_steps=500,
        save_total_limit=3,
        gradient_checkpointing=True,
        dataloader_pin_memory=False,
        remove_unused_columns=False,
        report_to="none",
    )

    trainer = Trainer(
        model=model,
        args=training_args,
        train_dataset=tokenized,
    )

    # Train (resume if checkpoint exists)
    if checkpoint:
        print(f"🔄 Resuming from checkpoint...")
        trainer.train(resume_from_checkpoint=checkpoint)
    else:
        print(f"🚀 Starting fresh training...")
        trainer.train()

    print("")
    print("💾 Saving final model...")
    trainer.save_model("/data/bioql_model/final")
    tokenizer.save_pretrained("/data/bioql_model/final")

    volume.commit()

    print("")
    print("=" * 60)
    print("✅ Training completed!")
    print("=" * 60)

    return {"status": "success", "trainable_params": trainable}


@app.local_entrypoint()
def main():
    print("\n🚀 Resuming BioQL training on Modal...\n")
    result = resume_training.remote()
    print(f"\n✅ Done: {result}\n")
