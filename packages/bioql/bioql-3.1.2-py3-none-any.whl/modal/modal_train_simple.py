"""
BioQL Foundational Model Training on Modal (Simplified)
========================================================

Simplified version that works with current Modal API.
"""

import modal

app = modal.App("bioql-training")

# Docker image with dependencies
image = (
    modal.Image.debian_slim(python_version="3.11")
    .pip_install(
        "torch>=2.0.0",
        "transformers>=4.35.0",
        "peft>=0.7.0",
        "bitsandbytes>=0.41.0",
        "accelerate>=0.24.0",
        "datasets>=2.14.0",
        "tqdm>=4.66.0",
    )
)


@app.function(
    image=image,
    gpu="A100-40GB",
    timeout=3600 * 12,  # 12 hours (increased)
    volumes={"/data": modal.Volume.from_name("bioql-data", create_if_missing=True)},
)
def train():
    """Train BioQL foundational model."""

    print("=" * 60)
    print("BioQL Foundational Model Training")
    print("=" * 60)

    # Configuration for HIGH QUALITY (realistic training time)
    # Using Qwen2.5-7B - open model, high quality, no auth required
    config = {
        "num_examples": 100000,
        "model_name": "Qwen/Qwen2.5-7B-Instruct",  # Open model, no auth needed
        "num_epochs": 5,  # Reduced from 10 to fit in 12h timeout
        "batch_size": 4,
        "gradient_accumulation": 8,
        "learning_rate": 1e-5,
        "lora_r": 16,
        "lora_alpha": 32,
    }

    print(f"\n📊 Configuration:")
    for k, v in config.items():
        print(f"   {k}: {v}")

    # Generate dataset inline (simplified)
    print(f"\n[1/4] Generating {config['num_examples']:,} training examples...")

    training_data = []

    # Simple template-based generation
    templates = {
        "bell": ("Create a Bell state", "from bioql import quantum\n\nresult = quantum('Create a Bell state', api_key='key', backend='simulator', shots=1000)\nprint(result.counts)"),
        "qft": ("Run QFT on 4 qubits", "from bioql import quantum\n\nresult = quantum('Run QFT on 4 qubits', api_key='key', backend='simulator', shots=1000)\nprint(result.counts)"),
        "grover": ("Search with Grover", "from bioql import quantum\n\nresult = quantum('Search with Grover', api_key='key', backend='simulator', shots=1000)\nprint(result.counts)"),
        "protein": ("Simulate protein folding", "from bioql import quantum\n\nresult = quantum('Simulate protein folding', api_key='key', backend='simulator', shots=1000)\nprint(result.bio_interpretation)"),
    }

    import random
    for i in range(config['num_examples']):
        template = random.choice(list(templates.values()))
        training_data.append({"input": template[0], "output": template[1]})
        if (i + 1) % 10000 == 0:
            print(f"   Generated {i+1:,}...")

    print(f"   ✅ Generated {len(training_data):,} examples")

    # Train model
    print("\n[2/4] Loading base model...")

    from transformers import AutoModelForCausalLM, AutoTokenizer
    import torch

    tokenizer = AutoTokenizer.from_pretrained(config['model_name'])
    tokenizer.pad_token = tokenizer.eos_token

    print(f"   ✅ Loaded {config['model_name']}")

    # Load with quantization
    from transformers import BitsAndBytesConfig

    quant_config = BitsAndBytesConfig(
        load_in_4bit=True,
        bnb_4bit_quant_type="nf4",
        bnb_4bit_compute_dtype=torch.float16,
        bnb_4bit_use_double_quant=True
    )

    model = AutoModelForCausalLM.from_pretrained(
        config['model_name'],
        quantization_config=quant_config,
        device_map="auto"
    )

    print(f"   ✅ Model loaded with 4-bit quantization")

    # Add LoRA
    print("\n[3/4] Adding LoRA adapters...")

    from peft import LoraConfig, get_peft_model, TaskType, prepare_model_for_kbit_training

    model = prepare_model_for_kbit_training(model)

    lora_config = LoraConfig(
        task_type=TaskType.CAUSAL_LM,
        r=config['lora_r'],
        lora_alpha=config['lora_alpha'],
        lora_dropout=0.05,
        target_modules=["q_proj", "k_proj", "v_proj", "o_proj"],
        bias="none"
    )

    model = get_peft_model(model, lora_config)

    trainable = sum(p.numel() for p in model.parameters() if p.requires_grad)
    total = sum(p.numel() for p in model.parameters())

    print(f"   ✅ LoRA added: {trainable:,} trainable params ({100*trainable/total:.2f}%)")

    # Training
    print("\n[4/4] Training...")
    print(f"   This will take 3-5 hours...")

    from transformers import Trainer, TrainingArguments
    from torch.utils.data import Dataset

    class BioQLDataset(Dataset):
        def __init__(self, data, tokenizer):
            self.data = data
            self.tokenizer = tokenizer

        def __len__(self):
            return len(self.data)

        def __getitem__(self, idx):
            item = self.data[idx]
            text = f"{item['input']}\n\n{item['output']}"
            enc = self.tokenizer(text, max_length=512, truncation=True, padding="max_length", return_tensors="pt")
            return {
                "input_ids": enc["input_ids"].squeeze(),
                "attention_mask": enc["attention_mask"].squeeze(),
                "labels": enc["input_ids"].squeeze()
            }

    # Split data
    train_size = int(0.9 * len(training_data))
    train_data = training_data[:train_size]
    eval_data = training_data[train_size:]

    train_dataset = BioQLDataset(train_data, tokenizer)
    eval_dataset = BioQLDataset(eval_data, tokenizer)

    training_args = TrainingArguments(
        output_dir="/data/bioql_model",
        num_train_epochs=config['num_epochs'],
        per_device_train_batch_size=config['batch_size'],
        gradient_accumulation_steps=config['gradient_accumulation'],
        learning_rate=config['learning_rate'],
        fp16=True,
        logging_steps=50,
        eval_strategy="steps",
        eval_steps=500,
        save_steps=500,  # Save more frequently (every 500 steps instead of 1000)
        save_total_limit=5,  # Keep more checkpoints
        warmup_steps=500,
        load_best_model_at_end=True,  # Load best checkpoint at the end
    )

    trainer = Trainer(
        model=model,
        args=training_args,
        train_dataset=train_dataset,
        eval_dataset=eval_dataset,
    )

    # Train! (resume from checkpoint if available)
    import os
    checkpoints = [d for d in os.listdir("/data/bioql_model") if d.startswith("checkpoint-")]

    if checkpoints:
        # Resume from latest checkpoint
        latest_checkpoint = sorted(checkpoints, key=lambda x: int(x.split("-")[1]))[-1]
        resume_path = f"/data/bioql_model/{latest_checkpoint}"
        print(f"\n🔄 Resuming from {latest_checkpoint}...")
        trainer.train(resume_from_checkpoint=resume_path)
    else:
        print(f"\n🆕 Starting fresh training...")
        trainer.train()

    # Save
    model.save_pretrained("/data/bioql_model")
    tokenizer.save_pretrained("/data/bioql_model")

    print("\n✅ Training complete!")
    print("   Model saved to Modal volume: /data/bioql_model")

    return {"status": "success", "model_path": "/data/bioql_model"}


@app.local_entrypoint()
def main():
    """Start training."""
    print("🚀 Starting BioQL training on Modal A100 GPU...")
    print("   This will take 3-5 hours and cost ~$4-6")
    print("")

    import time
    time.sleep(2)

    result = train.remote()

    print("\n✅ Training job submitted!")
    print(f"   Result: {result}")
    print("\n   Download model with:")
    print("   modal run modal_download.py")
