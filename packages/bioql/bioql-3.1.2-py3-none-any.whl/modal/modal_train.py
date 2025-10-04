"""
BioQL Foundational Model Training on Modal
===========================================

Train BioQL foundational model on Modal's cloud GPUs.

Usage:
    modal run modal_train.py
"""

import modal

# Create Modal app
app = modal.App("bioql-foundational-training")

# Define GPU configuration
GPU_CONFIG = "A100-40GB"  # A100 GPU with 40GB

# Docker image with all dependencies
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
        "loguru>=0.7.0",
    )
)

# No need for mount - will install bioql from local directory


@app.function(
    image=image,
    gpu=GPU_CONFIG,
    timeout=3600 * 4,  # 4 hours
    volumes={"/data": modal.Volume.from_name("bioql-training-data", create_if_missing=True)},
)
def train_model(
    num_examples: int = 10000,
    model_name: str = "TinyLlama/TinyLlama-1.1B-Chat-v1.0",
    num_epochs: int = 3,
    use_qlora: bool = True,
):
    """
    Train BioQL foundational model on GPU.

    Args:
        num_examples: Number of training examples to generate
        model_name: Base model to fine-tune
        num_epochs: Number of training epochs
        use_qlora: Use 4-bit quantization (saves memory)
    """
    import sys
    sys.path.insert(0, "/root/bioql")

    import torch
    from loguru import logger

    logger.info("=" * 60)
    logger.info("BioQL Foundational Model Training on Modal")
    logger.info("=" * 60)

    # Check GPU
    if torch.cuda.is_available():
        gpu_name = torch.cuda.get_device_name(0)
        gpu_memory = torch.cuda.get_device_properties(0).total_memory / 1e9
        logger.info(f"GPU: {gpu_name}")
        logger.info(f"GPU Memory: {gpu_memory:.1f} GB")
    else:
        logger.warning("No GPU detected!")

    # Step 1: Generate training dataset
    logger.info("\n[1/4] Generating training dataset...")

    from bioql.llm.models.training import create_training_dataset

    splits = create_training_dataset(
        num_examples=num_examples,
        output_path="/data/bioql_dataset",
        split_ratio=(0.8, 0.1, 0.1)
    )

    logger.info(f"✅ Train: {len(splits['train']):,} examples")
    logger.info(f"✅ Val: {len(splits['val']):,} examples")
    logger.info(f"✅ Test: {len(splits['test']):,} examples")

    # Step 2: Configure training
    logger.info("\n[2/4] Configuring training...")

    from bioql.llm.models.training import TrainingConfig

    config = TrainingConfig(
        model_name=model_name,
        output_dir="/data/bioql_model_output",
        num_train_epochs=num_epochs,
        per_device_train_batch_size=4,
        gradient_accumulation_steps=8,  # Increased for stability
        learning_rate=1e-5,  # Lower LR for better quality
        warmup_steps=500,  # More warmup steps
        logging_steps=10,
        eval_steps=200,
        save_steps=1000,  # Save checkpoints every 1000 steps
        use_lora=True,
        use_qlora=use_qlora,
        lora_r=16,  # Increased rank for better capacity
        lora_alpha=32,  # Increased alpha
        lora_dropout=0.05,
        fp16=True,
        max_seq_length=512,
    )

    logger.info(f"Model: {model_name}")
    logger.info(f"Epochs: {num_epochs}")
    logger.info(f"LoRA: True, QLoRA: {use_qlora}")

    # Step 3: Train model
    logger.info("\n[3/4] Training model...")
    logger.info("This will take 1-4 hours depending on dataset size...")

    from bioql.llm.models.training import BioQLTrainer

    trainer = BioQLTrainer(config)
    trainer.prepare_model()

    # Create PyTorch datasets
    from transformers import AutoTokenizer

    tokenizer = AutoTokenizer.from_pretrained(model_name)
    tokenizer.pad_token = tokenizer.eos_token

    from bioql.llm.models.training import BioQLDataset

    train_dataset = BioQLDataset(splits["train"], tokenizer)
    eval_dataset = BioQLDataset(splits["val"], tokenizer)

    # Train
    trainer.train(train_dataset, eval_dataset)

    # Save
    trainer.save("/data/bioql_model_output")

    logger.info("✅ Training complete!")
    logger.info("Model saved to: /data/bioql_model_output")

    # Step 4: Test model
    logger.info("\n[4/4] Testing trained model...")

    from bioql.llm.models.inference import BioQLInference, GenerationConfig

    inference = BioQLInference(
        model_path="/data/bioql_model_output",
        model_name=model_name,
        quantization="4bit" if use_qlora else None
    )

    test_prompts = [
        "Create a Bell state",
        "Run QFT on 4 qubits",
        "Simulate protein folding"
    ]

    logger.info("\nTesting code generation:")
    for prompt in test_prompts:
        logger.info(f"\nPrompt: {prompt}")
        result = inference.generate(
            prompt=prompt,
            config=GenerationConfig(max_length=256, temperature=0.7)
        )
        logger.info(f"Generated:\n{result.generated_code[:200]}...")

    logger.info("\n" + "=" * 60)
    logger.info("Training Complete!")
    logger.info("=" * 60)
    logger.info("\nModel saved in Modal volume: bioql-training-data")
    logger.info("Path: /data/bioql_model_output")

    return {
        "status": "success",
        "model_path": "/data/bioql_model_output",
        "train_examples": len(splits["train"]),
        "val_examples": len(splits["val"]),
        "test_examples": len(splits["test"])
    }


@app.function(
    image=image,
    gpu=GPU_CONFIG,
    volumes={"/data": modal.Volume.from_name("bioql-training-data")},
)
def test_model(prompt: str = "Create a Bell state"):
    """
    Test the trained model.

    Args:
        prompt: Natural language prompt
    """
    import sys
    sys.path.insert(0, "/root/bioql")

    from bioql.llm.models.inference import BioQLInference, GenerationConfig

    print(f"Testing model with prompt: {prompt}")

    inference = BioQLInference(
        model_path="/data/bioql_model_output",
        quantization="4bit"
    )

    result = inference.generate(
        prompt=prompt,
        config=GenerationConfig(max_length=512, temperature=0.7)
    )

    print("\n" + "=" * 60)
    print("Generated Code:")
    print("=" * 60)
    print(result.generated_code)
    print("=" * 60)

    return result.generated_code


@app.local_entrypoint()
def main(
    num_examples: int = 100000,  # 100K examples for best quality
    model: str = "mistralai/Mistral-7B-v0.1",  # Mistral 7B (better than TinyLlama)
    epochs: int = 10,  # More epochs for better convergence
    test_only: bool = False,
):
    """
    Main entry point.

    Usage:
        # Train model
        modal run modal_train.py

        # Train with custom settings
        modal run modal_train.py --num-examples 50000 --epochs 5

        # Use different base model
        modal run modal_train.py --model mistralai/Mistral-7B-v0.1

        # Test existing model
        modal run modal_train.py --test-only
    """
    if test_only:
        print("Testing existing model...")
        code = test_model.remote("Create a Bell state and measure it")
        print(f"\nGenerated code:\n{code}")
    else:
        print(f"Starting training on Modal GPU...")
        print(f"  Examples: {num_examples:,}")
        print(f"  Model: {model}")
        print(f"  Epochs: {epochs}")
        print(f"\nThis will use Modal credits. Continue? (Ctrl+C to cancel)")

        import time
        time.sleep(3)

        result = train_model.remote(
            num_examples=num_examples,
            model_name=model,
            num_epochs=epochs,
            use_qlora=True
        )

        print("\n✅ Training completed successfully!")
        print(f"Results: {result}")
        print("\nTo test the model:")
        print("  modal run modal_train.py --test-only")
