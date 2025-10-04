"""
BioQL Training - ROBUST VERSION
================================
Features:
- Frequent checkpoints (every 100 steps)
- Auto-resume from last checkpoint
- Better error handling
- Progress tracking
"""

import modal

# Volume for persistent storage
volume = modal.Volume.from_name("bioql-training-robust", create_if_missing=True)

# Image with dependencies
image = (
    modal.Image.debian_slim(python_version="3.11")
    .pip_install(
        "numpy==1.26.4",
        "torch==2.1.0",
        "transformers==4.37.0",
        "datasets==2.16.0",
        "accelerate==0.25.0",
        "peft==0.7.0",
        "bitsandbytes==0.41.3",
        "scipy==1.11.4",
    )
)

app = modal.App(name="bioql-training-robust", image=image)


@app.function(
    gpu="A100-40GB",
    timeout=7200,  # 2 hours
    volumes={"/data": volume},
    retries=3  # Auto-retry on failure
)
def train():
    """Train with robust checkpoint system."""
    import torch
    from transformers import (
        AutoTokenizer,
        AutoModelForCausalLM,
        TrainingArguments,
        Trainer,
    )
    from peft import LoraConfig, get_peft_model, prepare_model_for_kbit_training
    from datasets import Dataset
    import random
    import os
    from pathlib import Path

    print("\n" + "="*70)
    print("🚀 BioQL Robust Training")
    print("="*70 + "\n")

    # Check for existing checkpoint
    checkpoint_dir = Path("/data/checkpoints")
    checkpoint_dir.mkdir(parents=True, exist_ok=True)

    latest_checkpoint = None
    if list(checkpoint_dir.glob("checkpoint-*")):
        checkpoints = sorted(checkpoint_dir.glob("checkpoint-*"),
                           key=lambda x: int(x.name.split("-")[1]))
        latest_checkpoint = str(checkpoints[-1])
        print(f"📂 Found checkpoint: {latest_checkpoint}")
        print(f"   Resuming from step {latest_checkpoint.split('-')[-1]}\n")
    else:
        print("📂 No checkpoint found, starting fresh training\n")

    # Generate dataset (only if not resuming)
    dataset_file = "/data/dataset.pt"
    if os.path.exists(dataset_file) and latest_checkpoint:
        print("[1/5] Loading cached dataset...")
        dataset = torch.load(dataset_file)
        print(f"   ✅ Loaded {len(dataset)} examples\n")
    else:
        print("[1/5] Generating 100K training examples...")

        examples = []
        templates = [
            "Create a Bell state",
            "Run QFT on {} qubits",
            "Run Grover's algorithm on {} qubits",
            "Create {} qubit GHZ state",
            "Apply Hadamard to qubit {}",
            "Implement quantum teleportation",
            "Build a {} qubit random circuit",
        ]

        for i in range(10000):  # Reduced to 10K for 2-hour training
            if i % 2500 == 0 and i > 0:
                print(f"   Generated {i}...")

            template = random.choice(templates)
            if "{}" in template:
                task = template.format(random.randint(2, 8))
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

        dataset = Dataset.from_list(examples)
        torch.save(dataset, dataset_file)
        volume.commit()
        print(f"   ✅ {len(examples)} examples ready\n")

    # Load model
    print("[2/5] Loading Qwen2.5-7B model...")
    base_model = "Qwen/Qwen2.5-7B-Instruct"

    tokenizer = AutoTokenizer.from_pretrained(base_model, trust_remote_code=True)

    model = AutoModelForCausalLM.from_pretrained(
        base_model,
        device_map="auto",
        torch_dtype=torch.float16,
        trust_remote_code=True,
        load_in_4bit=True,
        bnb_4bit_compute_dtype=torch.float16,
        bnb_4bit_quant_type="nf4",
        bnb_4bit_use_double_quant=True
    )
    print("   ✅ Model loaded with 4-bit quantization\n")

    # Add LoRA
    print("[3/5] Adding LoRA adapters...")
    model = prepare_model_for_kbit_training(model)

    lora_config = LoraConfig(
        r=16,
        lora_alpha=32,
        target_modules=["q_proj", "k_proj", "v_proj", "o_proj"],
        lora_dropout=0.05,
        bias="none",
        task_type="CAUSAL_LM"
    )

    model = get_peft_model(model, lora_config)
    trainable = sum(p.numel() for p in model.parameters() if p.requires_grad)
    print(f"   ✅ LoRA ready")
    print(f"   Trainable: {trainable:,} params\n")

    # Tokenize
    print("[4/5] Tokenizing dataset...")

    def tokenize(examples):
        tokenized = tokenizer(
            examples["text"],
            truncation=True,
            max_length=512,
            padding="max_length",
        )
        tokenized["labels"] = tokenized["input_ids"].copy()
        return tokenized

    tokenized = dataset.map(tokenize, batched=True, batch_size=1000)
    print("   ✅ Dataset tokenized\n")

    # Training arguments - CHECKPOINT EVERY 10 MINUTES
    print("[5/5] Training (checkpoints every ~10 minutes)...\n")

    training_args = TrainingArguments(
        output_dir=str(checkpoint_dir),
        num_train_epochs=3,  # Reduced for 2-hour window
        per_device_train_batch_size=4,
        gradient_accumulation_steps=8,
        learning_rate=2e-4,
        weight_decay=0.01,
        logging_steps=5,
        save_steps=50,  # ~10 min checkpoints (50 steps × ~12 sec/step)
        save_total_limit=10,  # Keep last 10 checkpoints
        fp16=True,
        gradient_checkpointing=True,
        report_to="none",
        remove_unused_columns=False,
    )

    trainer = Trainer(
        model=model,
        args=training_args,
        train_dataset=tokenized,
    )

    # Resume or start fresh
    if latest_checkpoint:
        print(f"🔄 Resuming from {latest_checkpoint}\n")
        trainer.train(resume_from_checkpoint=latest_checkpoint)
    else:
        print("🚀 Starting fresh training...\n")
        trainer.train()

    # Save final model
    final_dir = "/data/final_model"
    print(f"\n💾 Saving final model to {final_dir}...")
    trainer.save_model(final_dir)
    volume.commit()

    print("\n" + "="*70)
    print("✅ TRAINING COMPLETED!")
    print("="*70)
    print(f"Final model saved to: {final_dir}")
    print(f"Checkpoints saved in: {checkpoint_dir}")
    print("="*70 + "\n")


@app.local_entrypoint()
def main():
    """Start training."""
    print("\n🚀 Launching 2-HOUR training on Modal GPU A100...")
    print("   - 10K examples, 3 epochs")
    print("   - Checkpoints every ~10 minutes (50 steps)")
    print("   - Auto-resume on restart")
    print("   - 2 hour timeout\n")

    train.remote()
