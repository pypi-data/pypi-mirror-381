"""
Resume Improved Model Training
================================
Continúa desde el último checkpoint (epoch 3.68)
Solo necesita completar el último 8% del training.
"""

import modal
import time

# Volumes
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

app = modal.App(name="bioql-resume-improved", image=image)


@app.function(
    gpu="A100",
    timeout=7200,  # 2 horas es suficiente para el 8% restante
    volumes={"/data": volume}
)
def resume_training():
    """Resume training from last checkpoint."""
    import torch
    from transformers import AutoTokenizer, AutoModelForCausalLM, TrainingArguments, Trainer
    from peft import PeftModel
    import os

    print("=" * 70)
    print("🔄 RESUMING Improved Model Training")
    print("=" * 70)

    # Check if checkpoint exists
    checkpoint_dir = "/data/improved_model"
    if not os.path.exists(checkpoint_dir):
        print("❌ No checkpoint found! Run full training first.")
        return

    print(f"\n✅ Found checkpoint at {checkpoint_dir}")

    # Find latest checkpoint subdirectory
    checkpoints = [d for d in os.listdir(checkpoint_dir) if d.startswith("checkpoint-")]
    if checkpoints:
        latest_checkpoint = sorted(checkpoints, key=lambda x: int(x.split("-")[1]))[-1]
        resume_from = os.path.join(checkpoint_dir, latest_checkpoint)
        print(f"📂 Resuming from: {resume_from}")
    else:
        resume_from = checkpoint_dir
        print(f"📂 Resuming from: {resume_from}")

    # Load model and resume training
    print("\n[1/2] Loading model from checkpoint...")

    model_name = "deepseek-ai/deepseek-coder-6.7b-instruct"
    tokenizer = AutoTokenizer.from_pretrained(model_name, trust_remote_code=True)
    tokenizer.pad_token = tokenizer.eos_token

    print("   ✅ Tokenizer loaded")

    # Training args for resume
    print("\n[2/2] Resuming training...")

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
        resume_from_checkpoint=resume_from  # KEY: Resume from here
    )

    # Initialize trainer with checkpoint
    trainer = Trainer(
        model=None,  # Will be loaded from checkpoint
        args=training_args,
        tokenizer=tokenizer,
    )

    print("   🏋️  Resuming training from checkpoint...")
    start_time = time.time()

    try:
        trainer.train(resume_from_checkpoint=resume_from)

        training_time = time.time() - start_time
        print(f"\n   ✅ Training complete in {training_time/60:.1f} minutes")

        # Save final model
        print("\n[3/3] Saving final model...")
        trainer.save_model("/data/improved_model/final")
        tokenizer.save_pretrained("/data/improved_model/final")

        volume.commit()

        print("\n" + "=" * 70)
        print("✅ TRAINING RESUMED AND COMPLETED")
        print("=" * 70)
        print(f"⏱️  Additional time: {training_time/60:.1f} minutes")
        print(f"💾 Final model saved to: /data/improved_model/final")

    except Exception as e:
        print(f"\n❌ Error resuming training: {e}")
        import traceback
        traceback.print_exc()


@app.local_entrypoint()
def main():
    """Resume training."""
    print("🔄 Resuming improved model training from checkpoint...")
    resume_training.remote()
    print("✅ Training resumed and completed!")
