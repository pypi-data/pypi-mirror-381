"""
Download Trained BioQL Model from Modal
========================================

Downloads the trained model from Modal volume to local disk.

Usage:
    python modal_download.py
"""

import modal
from pathlib import Path

app = modal.App("bioql-model-download")

# Volume where model is stored
volume = modal.Volume.from_name("bioql-training-data")


@app.function(
    volumes={"/data": volume},
    timeout=3600,
)
def download_model(local_path: str = "./bioql_trained_model"):
    """
    Package model for download.

    Args:
        local_path: Where to save locally

    Returns:
        Model files as bytes
    """
    import tarfile
    import io
    import os

    print(f"Packaging model from /data/bioql_model_output...")

    # Check if model exists
    model_path = "/data/bioql_model_output"
    if not os.path.exists(model_path):
        raise FileNotFoundError(f"Model not found at {model_path}. Train first with: modal run modal_train.py")

    # List files
    files = []
    for root, dirs, filenames in os.walk(model_path):
        for filename in filenames:
            filepath = os.path.join(root, filename)
            arcname = os.path.relpath(filepath, model_path)
            files.append((filepath, arcname))

    print(f"Found {len(files)} files to download")

    # Create tar archive in memory
    tar_buffer = io.BytesIO()
    with tarfile.open(fileobj=tar_buffer, mode='w:gz') as tar:
        for filepath, arcname in files:
            tar.add(filepath, arcname=arcname)
            print(f"  Added: {arcname}")

    tar_buffer.seek(0)
    return tar_buffer.read()


@app.function(
    volumes={"/data": volume},
)
def list_checkpoints():
    """List all available model checkpoints."""
    import os

    model_dir = "/data/bioql_model_output"

    if not os.path.exists(model_dir):
        return {"error": "No model found. Train first!"}

    # List all files
    files = []
    total_size = 0

    for root, dirs, filenames in os.walk(model_dir):
        for filename in filenames:
            filepath = os.path.join(root, filename)
            size = os.path.getsize(filepath)
            total_size += size
            rel_path = os.path.relpath(filepath, model_dir)
            files.append({
                "file": rel_path,
                "size_mb": size / (1024 * 1024)
            })

    return {
        "model_path": model_dir,
        "total_files": len(files),
        "total_size_mb": total_size / (1024 * 1024),
        "files": sorted(files, key=lambda x: x["file"])
    }


@app.local_entrypoint()
def main(
    output_dir: str = "./bioql_trained_model",
    list_only: bool = False
):
    """
    Download trained model from Modal.

    Usage:
        # List files in model
        modal run modal_download.py --list-only

        # Download model
        modal run modal_download.py

        # Download to specific directory
        modal run modal_download.py --output-dir ./my_model
    """
    import sys

    if list_only:
        print("Listing model files on Modal...")
        info = list_checkpoints.remote()

        if "error" in info:
            print(f"❌ {info['error']}")
            sys.exit(1)

        print(f"\n✅ Model found on Modal!")
        print(f"Path: {info['model_path']}")
        print(f"Total files: {info['total_files']}")
        print(f"Total size: {info['total_size_mb']:.1f} MB")
        print(f"\nFiles:")
        for f in info['files']:
            print(f"  {f['file']:<50} {f['size_mb']:>8.2f} MB")
        return

    print("=" * 60)
    print("Downloading BioQL Trained Model from Modal")
    print("=" * 60)

    print(f"\nDownload destination: {output_dir}")

    # Create output directory
    output_path = Path(output_dir)
    output_path.mkdir(parents=True, exist_ok=True)

    print("\n[1/3] Fetching model from Modal...")

    try:
        model_bytes = download_model.remote(output_dir)
    except Exception as e:
        print(f"\n❌ Error downloading model: {e}")
        print("\nMake sure you've trained the model first:")
        print("  modal run modal_train.py")
        sys.exit(1)

    print(f"✅ Downloaded {len(model_bytes) / (1024*1024):.1f} MB")

    print("\n[2/3] Extracting model files...")

    import tarfile
    import io

    tar_buffer = io.BytesIO(model_bytes)
    with tarfile.open(fileobj=tar_buffer, mode='r:gz') as tar:
        tar.extractall(output_path)
        members = tar.getmembers()
        print(f"✅ Extracted {len(members)} files")

    print("\n[3/3] Verifying model...")

    # Check for key files
    required_files = [
        "adapter_config.json",
        "adapter_model.bin",
        "training_config.json"
    ]

    all_present = True
    for filename in required_files:
        filepath = output_path / filename
        if filepath.exists():
            size = filepath.stat().st_size / (1024 * 1024)
            print(f"  ✅ {filename:<30} ({size:.2f} MB)")
        else:
            print(f"  ❌ {filename:<30} (missing)")
            all_present = False

    print("\n" + "=" * 60)

    if all_present:
        print("✅ Model downloaded successfully!")
        print("=" * 60)
        print(f"\nModel location: {output_path.absolute()}")
        print("\nTo use the model:")
        print(f'''
from bioql.llm.models.inference import quick_inference

code = quick_inference(
    prompt="Create a Bell state",
    model_path="{output_path.absolute()}",
    model_name="mistralai/Mistral-7B-v0.1",
    quantization="4bit"
)

print(code)
''')
    else:
        print("⚠️  Model downloaded but some files missing")
        print("=" * 60)

    print("\n" + "=" * 60)
