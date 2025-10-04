"""
BioQL Training - FINAL VERSION
================================

Fixed all issues:
- Correct transformers version for Qwen2
- NumPy compatibility
- Proper checkpoint handling
"""

import modal

# New volume name to start fresh
volume = modal.Volume.from_name("bioql-training-v2", create_if_missing=True)

# Correct image with all dependencies
image = (
    modal.Image.debian_slim(python_version="3.11")
    .pip_install(
        "numpy==1.26.4",  # Compatible version FIRST
        "torch==2.1.0",
        "transformers==4.37.0",  # Has Qwen2Tokenizer
        "datasets==2.16.0",
        "accelerate==0.25.0",
        "peft==0.7.0",
        "bitsandbytes==0.41.3",
        "scipy==1.11.4",
        "sentencepiece==0.1.99",
        "protobuf==4.25.1",
    )
)

app = modal.App(name="bioql-final-training", image=image)


@app.function(
    gpu="A100-40GB",
    timeout=43200,  # 12 hours
    volumes={"/model": volume},
)
def train():
    """Train BioQL model - clean version."""
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
    import os

    print("=" * 70)
    print("BioQL Foundational Model Training - FINAL")
    print("=" * 70)
    print()

    # Generate dataset
    print("[1/5] Generating 100K training examples...")

    examples = []
    templates = [
        "Create a Bell state",
        "Run QFT on {} qubits",
        "Run Grover's algorithm on {} qubits",
        "Simulate {} protein folding using VQE",
        "Calculate drug binding to {} receptor",
    ]

    proteins = ["insulin", "hemoglobin", "myoglobin", "collagen"]
    receptors = ["GLP1R", "DRD2", "EGFR", "ACE2"]

    for i in range(100000):
        template = random.choice(templates)

        if "qubits" in template:
            task = template.format(random.randint(2, 8))
        elif "protein" in template:
            task = template.format(random.choice(proteins))
        elif "receptor" in template:
            task = template.format(random.choice(receptors))
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

        if (i + 1) % 25000 == 0:
            print(f"   Generated {i + 1:,}...")

    dataset = Dataset.from_list(examples)
    print(f"   ✅ {len(examples):,} examples ready\n")

    # Load model
    print("[2/5] Loading Qwen2.5-7B model...")

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

    print("   ✅ Model loaded with 4-bit quantization\n")

    # Add LoRA
    print("[3/5] Adding LoRA adapters...")

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
    total = sum(p.numel() for p in model.parameters())

    print(f"   ✅ LoRA ready")
    print(f"   Trainable: {trainable:,} params ({100 * trainable / total:.2f}%)\n")

    # Tokenize
    print("[4/5] Tokenizing dataset...")

    def tokenize(examples):
        tokenized = tokenizer(
            examples["text"],
            truncation=True,
            max_length=512,
            padding="max_length",
        )
        # Copy input_ids to labels for causal LM
        tokenized["labels"] = tokenized["input_ids"].copy()
        return tokenized

    tokenized = dataset.map(
        tokenize,
        batched=True,
        remove_columns=dataset.column_names,
    )

    print("   ✅ Dataset tokenized\n")

    # Training
    print("[5/5] Training (this will take 3-5 hours)...")
    print()

    training_args = TrainingArguments(
        output_dir="/model/bioql",
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

    # Check for checkpoints
    checkpoint = None
    if os.path.exists("/model/bioql"):
        checkpoints = [
            d for d in os.listdir("/model/bioql")
            if d.startswith("checkpoint-") and os.path.isdir(f"/model/bioql/{d}")
        ]

        if checkpoints:
            latest = sorted(checkpoints, key=lambda x: int(x.split("-")[1]))[-1]
            checkpoint = f"/model/bioql/{latest}"
            print(f"🔄 Resuming from {latest}...\n")

    if checkpoint:
        trainer.train(resume_from_checkpoint=checkpoint)
    else:
        print("🚀 Starting fresh training...\n")
        trainer.train()

    # Save final model
    print("\n💾 Saving final model...")
    trainer.save_model("/model/bioql/final")
    tokenizer.save_pretrained("/model/bioql/final")

    volume.commit()

    print()
    print("=" * 70)
    print("✅ TRAINING COMPLETED!")
    print("=" * 70)
    print()
    print(f"Model: Qwen2.5-7B-Instruct")
    print(f"Examples: 100,000")
    print(f"Epochs: 5")
    print(f"LoRA rank: 16")
    print(f"Trainable params: {trainable:,}")
    print()
    print("Next steps:")
    print("  1. Download: modal volume get bioql-training-v2 /model/bioql/final .")
    print("  2. Use in VS Code with modal mode")
    print()

    return {
        "status": "success",
        "trainable_params": trainable,
        "total_params": total,
    }


@app.local_entrypoint()
def main():
    print("\n🚀 Starting BioQL training on Modal GPU A100...\n")

    try:
        result = train.remote()
        print(f"\n✅ Training complete: {result}\n")
    except Exception as e:
        print(f"\n❌ Training failed: {e}\n")
        print("Check Modal dashboard for details")
        print("https://modal.com/apps/spectrix\n")
        raise
