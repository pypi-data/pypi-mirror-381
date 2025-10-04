"""
BioQL VS Code Model Server - Modal Deployment
Sirve el checkpoint-2000 entrenado para VS Code extension
"""
import modal
import os

# Create Modal app
app = modal.App("bioql-vscode-server")

# GPU image with dependencies
image = (
    modal.Image.debian_slim(python_version="3.11")
    .pip_install(
        "torch==2.1.0",
        "transformers==4.37.0",
        "peft==0.7.1",
        "accelerate==0.25.0",
        "bitsandbytes==0.41.3",
        "fastapi==0.108.0",
        "pydantic==2.5.0"
    )
)

# Create volume for checkpoint
checkpoint_volume = modal.Volume.from_name("bioql-checkpoint", create_if_missing=True)


@app.cls(
    image=image,
    gpu="A10G",  # Smaller GPU, más barato
    volumes={"/checkpoint": checkpoint_volume},
    timeout=600,
    container_idle_timeout=300,
    allow_concurrent_inputs=10
)
class BioQLVSCodeServer:
    """Server para VS Code extension"""

    @modal.enter()
    def load_model(self):
        """Load model on container startup"""
        import torch
        from transformers import AutoTokenizer, AutoModelForCausalLM
        from peft import PeftModel

        print("🔄 Loading base model...")
        base_model = "Qwen/Qwen2.5-7B-Instruct"

        # Tokenizer
        self.tokenizer = AutoTokenizer.from_pretrained(
            base_model,
            trust_remote_code=True
        )

        # Base model with 4-bit quantization
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

        print("🔄 Loading LoRA checkpoint-2000...")
        self.model = PeftModel.from_pretrained(
            model,
            "/checkpoint",
            torch_dtype=torch.float16
        )

        self.model.eval()
        print("✅ Model loaded and ready!")

    @modal.method()
    def generate(self, prompt: str, max_length: int = 300, temperature: float = 0.7) -> dict:
        """Generate BioQL code from prompt"""
        import torch

        # Format prompt for BioQL code generation
        formatted_prompt = f"""You are a BioQL code generator. Generate clean, working BioQL code.

User request: {prompt}

BioQL code:
```python
"""

        # Tokenize
        inputs = self.tokenizer(
            formatted_prompt,
            return_tensors="pt",
            truncation=True,
            max_length=512
        ).to(self.model.device)

        # Generate
        with torch.no_grad():
            outputs = self.model.generate(
                **inputs,
                max_new_tokens=max_length,
                temperature=temperature,
                do_sample=True,
                top_p=0.95,
                pad_token_id=self.tokenizer.eos_token_id
            )

        # Decode
        generated = self.tokenizer.decode(outputs[0], skip_special_tokens=True)

        # Extract code after the prompt
        code = generated.split("```python")[-1].split("```")[0].strip()

        return {
            "code": code,
            "success": True
        }


@app.function(
    image=image,
    allow_concurrent_inputs=100
)
@modal.asgi_app()
def fastapi_app():
    """FastAPI endpoint"""
    from fastapi import FastAPI, HTTPException
    from pydantic import BaseModel

    web_app = FastAPI(title="BioQL VS Code Server")

    class GenerateRequest(BaseModel):
        prompt: str
        max_length: int = 300
        temperature: float = 0.7

    class GenerateResponse(BaseModel):
        code: str
        success: bool

    @web_app.get("/health")
    async def health():
        return {"status": "healthy"}

    @web_app.post("/generate", response_model=GenerateResponse)
    async def generate_endpoint(request: GenerateRequest):
        try:
            server = BioQLVSCodeServer()
            result = server.generate.remote(
                request.prompt,
                request.max_length,
                request.temperature
            )
            return result
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))

    return web_app


# For local testing
@app.local_entrypoint()
def test():
    """Test the model locally"""
    server = BioQLVSCodeServer()

    test_prompts = [
        "Create a Bell state",
        "Generate a 3-qubit GHZ state",
        "Apply Hadamard to qubit 0"
    ]

    print("\n" + "="*60)
    print("Testing BioQL VS Code Server")
    print("="*60 + "\n")

    for prompt in test_prompts:
        print(f"📝 Prompt: {prompt}")
        result = server.generate.remote(prompt)
        print(f"✅ Code:\n{result['code']}\n")
        print("-"*60 + "\n")
