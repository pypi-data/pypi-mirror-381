"""
BioQL Model Diagnostics
=======================

Check the state of the fine-tuned model in Modal volume.
"""

import modal

volume = modal.Volume.from_name("bioql-deepseek", create_if_missing=False)
image = modal.Image.debian_slim(python_version="3.11")

app = modal.App(name="bioql-check-model", image=image)


@app.function(volumes={"/model": volume})
def check_model():
    """Check if model exists and is valid."""
    import os
    from pathlib import Path

    print("\n" + "=" * 70)
    print("🔍 BioQL Model Diagnostics")
    print("=" * 70 + "\n")

    model_dir = Path("/model/final_model")

    # Check if directory exists
    if not model_dir.exists():
        print("❌ CRITICAL: /model/final_model does NOT exist!")
        print("\n📋 Solution:")
        print("   Run training first:")
        print("   $ modal run training/TRAIN_DEEPSEEK.py")
        return {"status": "missing", "error": "Model directory not found"}

    print(f"✅ Model directory exists: {model_dir}\n")

    # List all files
    print("📁 Files in /model/final_model:")
    files = sorted(model_dir.rglob("*"))
    if not files:
        print("   ❌ Directory is EMPTY!")
        return {"status": "empty", "error": "Model directory is empty"}

    total_size = 0
    for file in files:
        if file.is_file():
            size = file.stat().st_size
            total_size += size
            size_mb = size / (1024 * 1024)
            print(f"   📄 {file.name:30s} {size_mb:8.2f} MB")

    print(f"\n   Total size: {total_size / (1024*1024):.2f} MB")

    # Check critical files
    print("\n🔍 Checking critical files:")
    required_files = {
        "adapter_config.json": "LoRA configuration",
        "adapter_model.bin": "LoRA weights (PyTorch)",
        "adapter_model.safetensors": "LoRA weights (SafeTensors)",
        "tokenizer_config.json": "Tokenizer configuration",
    }

    status = {"status": "ok", "missing": [], "found": []}

    for filename, description in required_files.items():
        filepath = model_dir / filename
        if filepath.exists():
            size = filepath.stat().st_size / 1024
            print(f"   ✅ {filename:30s} ({size:.1f} KB) - {description}")
            status["found"].append(filename)
        else:
            print(f"   ❌ {filename:30s} MISSING - {description}")
            status["missing"].append(filename)

    # Check for adapter model (need at least one)
    has_adapter = (
        (model_dir / "adapter_model.bin").exists() or
        (model_dir / "adapter_model.safetensors").exists()
    )

    if not (model_dir / "adapter_config.json").exists():
        print("\n❌ CRITICAL: adapter_config.json is MISSING!")
        status["status"] = "incomplete"
    elif not has_adapter:
        print("\n❌ CRITICAL: No adapter model file found!")
        print("   Expected: adapter_model.bin OR adapter_model.safetensors")
        status["status"] = "incomplete"
    else:
        print("\n✅ Model appears complete and valid!")
        status["status"] = "ok"

    # Recommendations
    print("\n" + "=" * 70)
    print("📋 Recommendations:")
    print("=" * 70)

    if status["status"] == "ok":
        print("✅ Model is ready to use!")
        print("\n🚀 Next steps:")
        print("   1. Deploy inference server:")
        print("      $ modal deploy modal/bioql_inference_deepseek.py")
        print("\n   2. Test endpoint:")
        print("      $ curl -X POST <endpoint-url> -d @test.json")
    elif status["status"] == "incomplete":
        print("❌ Model is incomplete or corrupted!")
        print("\n🔧 Solution:")
        print("   1. Delete existing model:")
        print("      $ modal volume rm bioql-deepseek --confirm")
        print("\n   2. Retrain from scratch:")
        print("      $ modal run training/TRAIN_DEEPSEEK.py")
    elif status["status"] == "missing":
        print("❌ Model has not been trained yet!")
        print("\n🔧 Solution:")
        print("   Train the model:")
        print("      $ modal run training/TRAIN_DEEPSEEK.py")

    print("=" * 70 + "\n")

    return status


@app.local_entrypoint()
def main():
    """Run diagnostics."""
    result = check_model.remote()
    print(f"\n📊 Final Status: {result['status'].upper()}")
