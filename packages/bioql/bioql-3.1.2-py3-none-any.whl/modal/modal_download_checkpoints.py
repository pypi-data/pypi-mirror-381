"""
Download BioQL Training Checkpoints from Modal
===============================================

Downloads all checkpoints to continue training locally or for inference.
"""

import modal
from pathlib import Path
import tarfile
import io

app = modal.App("bioql-download-checkpoints")

volume = modal.Volume.from_name("bioql-data")


@app.function(
    volumes={"/data": volume},
    timeout=3600,
)
def download_checkpoint(checkpoint_name: str = "checkpoint-2000"):
    """
    Download a specific checkpoint.

    Args:
        checkpoint_name: Name of checkpoint folder (e.g., "checkpoint-2000")
    """
    import os

    checkpoint_path = f"/data/bioql_model/{checkpoint_name}"

    if not os.path.exists(checkpoint_path):
        available = []
        if os.path.exists("/data/bioql_model"):
            available = [d for d in os.listdir("/data/bioql_model") if d.startswith("checkpoint")]
        return {
            "error": f"Checkpoint {checkpoint_name} not found",
            "available_checkpoints": available
        }

    # Create tar archive
    tar_buffer = io.BytesIO()

    with tarfile.open(fileobj=tar_buffer, mode='w:gz') as tar:
        for root, dirs, files in os.walk(checkpoint_path):
            for file in files:
                filepath = os.path.join(root, file)
                arcname = os.path.relpath(filepath, checkpoint_path)
                tar.add(filepath, arcname=arcname)
                print(f"  Added: {arcname}")

    tar_buffer.seek(0)

    # Get size info
    total_size = 0
    file_count = 0
    for root, dirs, files in os.walk(checkpoint_path):
        for file in files:
            filepath = os.path.join(root, file)
            total_size += os.path.getsize(filepath)
            file_count += 1

    return {
        "checkpoint": checkpoint_name,
        "files": file_count,
        "size_mb": total_size / (1024 * 1024),
        "data": tar_buffer.read()
    }


@app.function(
    volumes={"/data": volume},
)
def list_checkpoints():
    """List all available checkpoints."""
    import os

    checkpoints = []
    base_path = "/data/bioql_model"

    if not os.path.exists(base_path):
        return {"error": "No model directory found"}

    for item in os.listdir(base_path):
        item_path = os.path.join(base_path, item)
        if os.path.isdir(item_path) and item.startswith("checkpoint"):
            # Get size
            size = sum(
                os.path.getsize(os.path.join(root, file))
                for root, dirs, files in os.walk(item_path)
                for file in files
            )

            # Count files
            file_count = sum(
                len(files)
                for root, dirs, files in os.walk(item_path)
            )

            checkpoints.append({
                "name": item,
                "size_mb": size / (1024 * 1024),
                "files": file_count
            })

    return {
        "checkpoints": sorted(checkpoints, key=lambda x: x["name"]),
        "total": len(checkpoints)
    }


@app.local_entrypoint()
def main(
    checkpoint: str = "checkpoint-2000",
    output_dir: str = "/Users/heinzjungbluth/Desktop/bioql/bioql/llm/trained_model",
    list_only: bool = False
):
    """
    Download checkpoints from Modal.

    Usage:
        # List all checkpoints
        modal run modal_download_checkpoints.py --list-only

        # Download latest checkpoint
        modal run modal_download_checkpoints.py --checkpoint checkpoint-2000

        # Download to specific directory
        modal run modal_download_checkpoints.py --checkpoint checkpoint-2000 --output-dir /path/to/save
    """
    import sys

    if list_only:
        print("Listing checkpoints on Modal...")
        result = list_checkpoints.remote()

        if "error" in result:
            print(f"❌ {result['error']}")
            sys.exit(1)

        print(f"\n✅ Found {result['total']} checkpoint(s):\n")
        for cp in result["checkpoints"]:
            print(f"  📁 {cp['name']}")
            print(f"     Size: {cp['size_mb']:.1f} MB")
            print(f"     Files: {cp['files']}")
            print()

        return

    print("=" * 60)
    print("Downloading BioQL Training Checkpoint")
    print("=" * 60)
    print(f"\nCheckpoint: {checkpoint}")
    print(f"Output: {output_dir}")

    print("\n[1/3] Downloading from Modal...")

    try:
        result = download_checkpoint.remote(checkpoint)
    except Exception as e:
        print(f"\n❌ Error: {e}")
        sys.exit(1)

    if "error" in result:
        print(f"\n❌ {result['error']}")
        if "available_checkpoints" in result:
            print(f"\nAvailable checkpoints:")
            for cp in result["available_checkpoints"]:
                print(f"  - {cp}")
        sys.exit(1)

    print(f"✅ Downloaded {result['size_mb']:.1f} MB ({result['files']} files)")

    print("\n[2/3] Extracting checkpoint...")

    output_path = Path(output_dir)
    output_path.mkdir(parents=True, exist_ok=True)

    import tarfile
    import io

    tar_buffer = io.BytesIO(result["data"])
    with tarfile.open(fileobj=tar_buffer, mode='r:gz') as tar:
        tar.extractall(output_path)
        print(f"✅ Extracted to {output_path}")

    print("\n[3/3] Verifying files...")

    files = list(output_path.glob("**/*"))
    print(f"✅ {len(files)} files extracted")

    # Show key files
    key_files = ["adapter_model.bin", "adapter_config.json", "trainer_state.json"]
    for key_file in key_files:
        file_path = output_path / key_file
        if file_path.exists():
            size = file_path.stat().st_size / (1024 * 1024)
            print(f"  ✅ {key_file} ({size:.1f} MB)")
        else:
            print(f"  ⚠️  {key_file} (not found)")

    print("\n" + "=" * 60)
    print("✅ Checkpoint downloaded successfully!")
    print("=" * 60)
    print(f"\nLocation: {output_path.absolute()}")
    print("\nTo use for inference:")
    print(f'''
from bioql.llm.models.inference import BioQLInference

inference = BioQLInference(
    model_path="{output_path.absolute()}",
    model_name="Qwen/Qwen2.5-7B-Instruct",
    quantization="4bit"
)

result = inference.generate("Create a Bell state")
print(result.generated_code)
''')
