"""
BioQL Model Training - ROBUST VERSION
=======================================

Ultra-robust training with:
- Exception handling
- Frequent checkpoints (every 250 steps)
- Detailed logging
- Auto-resume from latest checkpoint
- Memory management
"""

import modal
import os

# ========================================
# Modal Configuration
# ========================================

# Volumen persistente para el modelo
volume = modal.Volume.from_name("bioql-model-volume", create_if_missing=True)

# Imagen con todas las dependencias
image = (
    modal.Image.debian_slim(python_version="3.11")
    .pip_install(
        "torch==2.1.0",
        "transformers==4.36.0",
        "datasets==2.16.0",
        "accelerate==0.25.0",
        "peft==0.7.0",
        "bitsandbytes==0.41.0",
        "scipy",
        "sentencepiece",
        "protobuf",
    )
)

# App
app = modal.App(
    name="bioql-train-robust",
    image=image
)

# ========================================
# Training Configuration
# ========================================

TRAINING_CONFIG = {
    # Dataset
    "num_examples": 100000,

    # Model
    "model_name": "Qwen/Qwen2.5-7B-Instruct",

    # Training
    "num_epochs": 5,
    "batch_size": 4,
    "gradient_accumulation_steps": 8,
    "learning_rate": 1e-5,
    "warmup_steps": 100,
    "max_grad_norm": 1.0,
    "weight_decay": 0.01,

    # LoRA
    "lora_r": 16,
    "lora_alpha": 32,
    "lora_dropout": 0.05,
    "target_modules": ["q_proj", "k_proj", "v_proj", "o_proj", "gate_proj", "up_proj", "down_proj"],

    # Optimization
    "use_qlora": True,
    "fp16": False,
    "bf16": True,
    "optim": "paged_adamw_8bit",
    "gradient_checkpointing": True,

    # Checkpointing (MÁS FRECUENTE)
    "save_steps": 250,  # Cada 250 steps (antes 500)
    "save_total_limit": 5,  # Mantener últimos 5 checkpoints

    # Logging
    "logging_steps": 10,
    "eval_steps": 500,
}


# ========================================
# Training Function
# ========================================

@app.function(
    gpu="A100-40GB",
    timeout=3600 * 12,  # 12 hours
    volumes={"/data": volume},
)
def train():
    """Train BioQL model with robust error handling."""
    import torch
    import transformers
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
    import json
    from datetime import datetime

    print("=" * 60)
    print("BioQL Foundational Model Training - ROBUST")
    print("=" * 60)
    print("")

    # Print config
    print("📊 Configuration:")
    for key, value in TRAINING_CONFIG.items():
        print(f"   {key}: {value}")
    print("")

    # ========================================
    # Step 1: Generate Training Data
    # ========================================

    def generate_training_data(num_examples: int):
        """Generate BioQL training examples."""
        print(f"[1/5] Generating {num_examples:,} training examples...")

        templates = {
            "bell": [
                "Create a Bell state",
                "Generate an entangled Bell pair",
                "Make a maximally entangled state",
                "Create EPR pair",
            ],
            "qft": [
                "Run QFT on {n} qubits",
                "Quantum Fourier Transform with {n} qubits",
                "Apply QFT to {n} qubit system",
            ],
            "grover": [
                "Run Grover's algorithm with {n} qubits",
                "Search using Grover on {n} qubits",
            ],
            "protein": [
                "Simulate {protein} protein folding",
                "Run VQE for {protein} folding",
            ],
            "drug": [
                "Simulate drug binding to {receptor}",
                "Calculate binding affinity for {receptor}",
            ],
        }

        examples = []

        for i in range(num_examples):
            category = random.choice(list(templates.keys()))
            template = random.choice(templates[category])

            # Fill template
            if "{n}" in template:
                n = random.randint(2, 8)
                task = template.format(n=n)
            elif "{protein}" in template:
                protein = random.choice(["insulin", "hemoglobin", "myoglobin"])
                task = template.format(protein=protein)
            elif "{receptor}" in template:
                receptor = random.choice(["GLP1R", "DRD2", "EGFR"])
                task = template.format(receptor=receptor)
            else:
                task = template

            # Generate code
            code = f'''from bioql import quantum

result = quantum(
    "{task}",
    api_key="your_api_key",
    backend="simulator",
    shots=1000
)

print(f"Results: {{result.counts}}")'''

            examples.append({
                "instruction": task,
                "code": code,
                "text": f"Task: {task}\n\nCode:\n{code}"
            })

            if (i + 1) % 10000 == 0:
                print(f"   Generated {i + 1:,}...")

        print(f"   ✅ Generated {num_examples:,} examples")
        return examples

    try:
        examples = generate_training_data(TRAINING_CONFIG["num_examples"])
        dataset = Dataset.from_list(examples)
        print("")
    except Exception as e:
        print(f"❌ Error generating data: {e}")
        raise

    # ========================================
    # Step 2: Load Model
    # ========================================

    print("[2/5] Loading base model...")

    try:
        # Quantization config
        bnb_config = BitsAndBytesConfig(
            load_in_4bit=TRAINING_CONFIG["use_qlora"],
            bnb_4bit_use_double_quant=True,
            bnb_4bit_quant_type="nf4",
            bnb_4bit_compute_dtype=torch.bfloat16,
        )

        # Load tokenizer
        tokenizer = AutoTokenizer.from_pretrained(
            TRAINING_CONFIG["model_name"],
            trust_remote_code=True,
        )

        if tokenizer.pad_token is None:
            tokenizer.pad_token = tokenizer.eos_token

        # Load model
        model = AutoModelForCausalLM.from_pretrained(
            TRAINING_CONFIG["model_name"],
            quantization_config=bnb_config if TRAINING_CONFIG["use_qlora"] else None,
            device_map="auto",
            trust_remote_code=True,
            torch_dtype=torch.bfloat16 if TRAINING_CONFIG["bf16"] else torch.float16,
        )

        print(f"   ✅ Loaded {TRAINING_CONFIG['model_name']}")

        if TRAINING_CONFIG["use_qlora"]:
            print("   ✅ Model loaded with 4-bit quantization")

        print("")

    except Exception as e:
        print(f"❌ Error loading model: {e}")
        raise

    # ========================================
    # Step 3: Add LoRA
    # ========================================

    print("[3/5] Adding LoRA adapters...")

    try:
        # Prepare model for training
        if TRAINING_CONFIG["use_qlora"]:
            model = prepare_model_for_kbit_training(model)

        # LoRA config
        lora_config = LoraConfig(
            r=TRAINING_CONFIG["lora_r"],
            lora_alpha=TRAINING_CONFIG["lora_alpha"],
            target_modules=TRAINING_CONFIG["target_modules"],
            lora_dropout=TRAINING_CONFIG["lora_dropout"],
            bias="none",
            task_type="CAUSAL_LM",
        )

        # Add LoRA
        model = get_peft_model(model, lora_config)

        # Print trainable params
        trainable_params = sum(p.numel() for p in model.parameters() if p.requires_grad)
        total_params = sum(p.numel() for p in model.parameters())
        trainable_pct = 100 * trainable_params / total_params

        print(f"   ✅ LoRA added: {trainable_params:,} trainable params ({trainable_pct:.2f}%)")
        print("")

    except Exception as e:
        print(f"❌ Error adding LoRA: {e}")
        raise

    # ========================================
    # Step 4: Tokenize Dataset
    # ========================================

    print("[4/5] Tokenizing dataset...")

    try:
        def tokenize_function(examples):
            return tokenizer(
                examples["text"],
                truncation=True,
                max_length=512,
                padding="max_length",
            )

        tokenized_dataset = dataset.map(
            tokenize_function,
            batched=True,
            remove_columns=dataset.column_names,
        )

        print("   ✅ Dataset tokenized")
        print("")

    except Exception as e:
        print(f"❌ Error tokenizing dataset: {e}")
        raise

    # ========================================
    # Step 5: Training
    # ========================================

    print("[5/5] Training...")
    print("   This will take several hours...")
    print("")

    try:
        # Training arguments
        training_args = TrainingArguments(
            output_dir="/data/bioql_model",
            num_train_epochs=TRAINING_CONFIG["num_epochs"],
            per_device_train_batch_size=TRAINING_CONFIG["batch_size"],
            gradient_accumulation_steps=TRAINING_CONFIG["gradient_accumulation_steps"],
            learning_rate=TRAINING_CONFIG["learning_rate"],
            warmup_steps=TRAINING_CONFIG["warmup_steps"],
            max_grad_norm=TRAINING_CONFIG["max_grad_norm"],
            weight_decay=TRAINING_CONFIG["weight_decay"],
            fp16=TRAINING_CONFIG["fp16"],
            bf16=TRAINING_CONFIG["bf16"],
            optim=TRAINING_CONFIG["optim"],
            logging_steps=TRAINING_CONFIG["logging_steps"],
            save_steps=TRAINING_CONFIG["save_steps"],
            save_total_limit=TRAINING_CONFIG["save_total_limit"],
            gradient_checkpointing=TRAINING_CONFIG["gradient_checkpointing"],
            dataloader_pin_memory=False,
            remove_unused_columns=False,
            report_to="none",
        )

        # Trainer
        trainer = Trainer(
            model=model,
            args=training_args,
            train_dataset=tokenized_dataset,
        )

        # Check for existing checkpoints
        checkpoints = []
        if os.path.exists("/data/bioql_model"):
            checkpoints = [
                d for d in os.listdir("/data/bioql_model")
                if d.startswith("checkpoint-")
            ]

        if checkpoints:
            # Resume from latest
            latest_checkpoint = sorted(
                checkpoints,
                key=lambda x: int(x.split("-")[1])
            )[-1]
            checkpoint_path = f"/data/bioql_model/{latest_checkpoint}"

            print(f"🔄 Resuming from {latest_checkpoint}...")
            print("")

            trainer.train(resume_from_checkpoint=checkpoint_path)
        else:
            print("🚀 Starting fresh training...")
            print("")

            trainer.train()

        # Save final model
        print("")
        print("💾 Saving final model...")
        trainer.save_model("/data/bioql_model/final")
        tokenizer.save_pretrained("/data/bioql_model/final")

        # Commit volume
        volume.commit()

        print("")
        print("=" * 60)
        print("✅ Training completed successfully!")
        print("=" * 60)
        print("")
        print("📊 Summary:")
        print(f"   Model: {TRAINING_CONFIG['model_name']}")
        print(f"   Examples: {TRAINING_CONFIG['num_examples']:,}")
        print(f"   Epochs: {TRAINING_CONFIG['num_epochs']}")
        print(f"   LoRA rank: {TRAINING_CONFIG['lora_r']}")
        print(f"   Trainable params: {trainable_params:,} ({trainable_pct:.2f}%)")
        print("")
        print("📦 Model saved to: /data/bioql_model/final")
        print("")
        print("Next steps:")
        print("  1. Download model: modal run modal_download_checkpoints.py")
        print("  2. Deploy API: modal deploy modal_serve.py")
        print("")

        return {
            "status": "success",
            "model": TRAINING_CONFIG["model_name"],
            "examples": TRAINING_CONFIG["num_examples"],
            "epochs": TRAINING_CONFIG["num_epochs"],
            "trainable_params": trainable_params,
        }

    except Exception as e:
        print("")
        print("=" * 60)
        print(f"❌ Training failed: {e}")
        print("=" * 60)
        print("")
        print("Debug info:")
        print(f"  Exception type: {type(e).__name__}")
        print(f"  Exception args: {e.args}")
        print("")

        # Try to save emergency checkpoint
        try:
            print("💾 Attempting emergency checkpoint save...")
            trainer.save_model("/data/bioql_model/emergency")
            volume.commit()
            print("   ✅ Emergency checkpoint saved")
        except Exception as save_error:
            print(f"   ❌ Could not save emergency checkpoint: {save_error}")

        raise


# ========================================
# Local Entry Point
# ========================================

@app.local_entrypoint()
def main():
    """Run training."""
    print("")
    print("🚀 Starting BioQL training on Modal A100 GPU...")
    print("   This will take 3-5 hours and cost ~$4-6")
    print("")

    try:
        result = train.remote()

        print("")
        print("=" * 60)
        print("🎉 Training completed!")
        print("=" * 60)
        print(f"Result: {result}")
        print("")

    except Exception as e:
        print("")
        print("=" * 60)
        print(f"❌ Training failed: {e}")
        print("=" * 60)
        print("")
        print("Troubleshooting:")
        print("  1. Check Modal logs: modal app logs bioql-train-robust")
        print("  2. Check for checkpoints: modal run modal_download_checkpoints.py")
        print("  3. Retry training (will auto-resume from last checkpoint)")
        print("")
        raise
