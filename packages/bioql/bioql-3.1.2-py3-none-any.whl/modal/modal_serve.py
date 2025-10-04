"""
BioQL Model Serving on Modal
==============================

Serve the trained BioQL model as a REST API on Modal.

Usage:
    modal deploy modal_serve.py
"""

import modal

app = modal.App("bioql-model-api")

# GPU for inference
GPU_CONFIG = modal.gpu.T4(count=1)  # T4 is cheaper for inference

# Docker image
image = (
    modal.Image.debian_slim(python_version="3.11")
    .pip_install(
        "torch>=2.0.0",
        "transformers>=4.35.0",
        "peft>=0.7.0",
        "bitsandbytes>=0.41.0",
        "accelerate>=0.24.0",
        "fastapi>=0.104.0",
        "pydantic>=2.0.0",
    )
)

# Mount bioql code
bioql_mount = modal.Mount.from_local_dir(
    ".",
    remote_path="/root/bioql",
    condition=lambda path: not any(
        x in path for x in [".git", "__pycache__", ".pyc"]
    )
)


@app.cls(
    image=image,
    gpu=GPU_CONFIG,
    mounts=[bioql_mount],
    volumes={"/data": modal.Volume.from_name("bioql-training-data")},
    container_idle_timeout=300,  # Keep warm for 5 minutes
)
class BioQLModelAPI:
    """BioQL Model API running on Modal GPU."""

    @modal.enter()
    def load_model(self):
        """Load model when container starts."""
        import sys
        sys.path.insert(0, "/root/bioql")

        from bioql.llm.models.inference import BioQLInference

        print("Loading BioQL model...")

        self.inference = BioQLInference(
            model_path="/data/bioql_model_output",
            quantization="4bit"
        )

        print("✅ Model loaded and ready!")

    @modal.method()
    def generate(
        self,
        prompt: str,
        max_length: int = 512,
        temperature: float = 0.7,
        top_p: float = 0.9
    ) -> dict:
        """
        Generate BioQL code from prompt.

        Args:
            prompt: Natural language description
            max_length: Maximum generation length
            temperature: Sampling temperature
            top_p: Nucleus sampling

        Returns:
            Generated code and metadata
        """
        from bioql.llm.models.inference import GenerationConfig

        config = GenerationConfig(
            max_length=max_length,
            temperature=temperature,
            top_p=top_p
        )

        result = self.inference.generate(prompt=prompt, config=config)

        return {
            "code": result.generated_code,
            "prompt": prompt,
            "metadata": result.metadata
        }

    @modal.web_endpoint(method="POST")
    def api_generate(self, request: dict):
        """
        REST API endpoint for code generation.

        Example:
            curl -X POST https://your-modal-url/api_generate \\
              -H "Content-Type: application/json" \\
              -d '{"prompt": "Create a Bell state"}'
        """
        prompt = request.get("prompt", "")
        max_length = request.get("max_length", 512)
        temperature = request.get("temperature", 0.7)
        top_p = request.get("top_p", 0.9)

        return self.generate(
            prompt=prompt,
            max_length=max_length,
            temperature=temperature,
            top_p=top_p
        )


@app.local_entrypoint()
def main(prompt: str = "Create a Bell state"):
    """
    Test the deployed model.

    Usage:
        modal run modal_serve.py
        modal run modal_serve.py --prompt "Run QFT on 4 qubits"
    """
    print(f"Generating code for: {prompt}")

    model = BioQLModelAPI()
    result = model.generate.remote(prompt)

    print("\n" + "=" * 60)
    print("Generated Code:")
    print("=" * 60)
    print(result["code"])
    print("=" * 60)
