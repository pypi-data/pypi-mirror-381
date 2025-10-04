"""
BioQL Inference Server on Modal
================================

Serves the trained BioQL LoRA model via FastAPI endpoint.
VS Code extension calls this API for code completion.

Pricing Model:
- Base cost: Modal GPU time (A10G)
- Markup: 40% profit margin
- Billing per inference request
- Integrated with BioQL billing database

Authentication:
- Requires valid API key
- Validates user quota/balance
- Logs usage to billing database
- Auto-cutoff on insufficient funds
"""

import modal
import time
import sys
from pathlib import Path

# Create volume references
model_volume = modal.Volume.from_name("bioql-training-robust")
billing_volume = modal.Volume.from_name("bioql-billing-db")

# Image with inference dependencies
image = (
    modal.Image.debian_slim(python_version="3.11")
    .pip_install(
        "numpy==1.26.4",  # Fix NumPy 2.x incompatibility
        "scipy==1.11.4",  # Missing dependency for bitsandbytes
        "torch==2.1.0",
        "transformers==4.37.0",
        "peft==0.7.0",
        "fastapi==0.109.0",
        "bitsandbytes==0.41.3",
    )
)

app = modal.App(name="bioql-inference", image=image)

# Pricing Configuration
# Modal A10G pricing: ~$1.10/hour = $0.000305556/second
# Reference: https://modal.com/pricing
MODAL_A10G_COST_PER_SECOND = 0.000305556  # $1.10/hour
PROFIT_MARGIN = 0.40  # 40% markup
PRICE_PER_SECOND = MODAL_A10G_COST_PER_SECOND * (1 + PROFIT_MARGIN)  # $0.000427778/sec


@app.cls(
    gpu="A10G",  # Cheaper GPU for inference
    volumes={
        "/data": model_volume,
        "/billing": billing_volume
    },
    scaledown_window=300,  # Keep warm for 5 minutes
)
class BioQLInference:
    """BioQL code generation inference server."""

    @modal.enter()
    def load_model(self):
        """Load model on container start."""
        import torch
        from transformers import AutoTokenizer, AutoModelForCausalLM
        from peft import PeftModel

        print("🔄 Loading BioQL LoRA v1 model...")

        base_model = "Qwen/Qwen2.5-7B-Instruct"

        # Load tokenizer
        self.tokenizer = AutoTokenizer.from_pretrained(
            base_model,
            trust_remote_code=True
        )

        # Load base model
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

        # Load LoRA adapter
        self.model = PeftModel.from_pretrained(
            model,
            "/data/final_model",
            torch_dtype=torch.float16
        )

        print("✅ Model loaded successfully!")

    @modal.method()
    def generate(
        self,
        prompt: str,
        max_length: int = 300,
        temperature: float = 0.7
    ) -> dict:
        """
        Generate BioQL code from natural language with cost tracking.

        Args:
            prompt: Natural language description
            max_length: Maximum tokens to generate
            temperature: Sampling temperature

        Returns:
            dict with code, timing, and cost information
        """
        import torch

        start_time = time.time()

        # Format prompt
        formatted_prompt = f"""Task: {prompt}

Code:
"""

        inputs = self.tokenizer(formatted_prompt, return_tensors="pt").to(self.model.device)

        generation_start = time.time()
        with torch.no_grad():
            outputs = self.model.generate(
                **inputs,
                max_new_tokens=max_length,
                do_sample=False,  # Use greedy decoding (no sampling)
                pad_token_id=self.tokenizer.pad_token_id or self.tokenizer.eos_token_id,
                eos_token_id=self.tokenizer.eos_token_id
            )
        generation_time = time.time() - generation_start

        generated = self.tokenizer.decode(outputs[0], skip_special_tokens=True)

        # Extract code part
        if "Code:" in generated:
            code = generated.split("Code:")[-1].strip()
        else:
            code = generated

        total_time = time.time() - start_time

        # Calculate costs
        base_cost = total_time * MODAL_A10G_COST_PER_SECOND
        user_cost = total_time * PRICE_PER_SECOND
        profit = user_cost - base_cost

        return {
            "code": code,
            "timing": {
                "total_seconds": round(total_time, 3),
                "generation_seconds": round(generation_time, 3),
                "overhead_seconds": round(total_time - generation_time, 3)
            },
            "cost": {
                "base_cost_usd": round(base_cost, 6),
                "user_cost_usd": round(user_cost, 6),
                "profit_usd": round(profit, 6),
                "profit_margin_percent": PROFIT_MARGIN * 100
            }
        }


@app.function(volumes={"/billing": billing_volume})
@modal.fastapi_endpoint(method="POST")
def generate_code(request: dict) -> dict:
    """
    Web endpoint for code generation with authentication and billing.

    Example:
        curl -X POST https://your-modal-url.modal.run \
             -H "Content-Type: application/json" \
             -H "Authorization: Bearer YOUR_API_KEY" \
             -d '{"prompt": "Create a Bell state", "max_length": 200}'

    Response (success):
        {
            "code": "from bioql import quantum...",
            "prompt": "Create a Bell state",
            "model": "bioql-lora-v1",
            "timing": {...},
            "cost": {...},
            "user": {"email": "user@example.com", "balance": 10.50}
        }

    Response (error):
        {
            "error": "Insufficient balance: $0.50 < $0.001283",
            "balance": 0.50,
            "estimated_cost": 0.001283
        }
    """
    import sys
    sys.path.insert(0, "/billing")
    from billing_integration import (
        authenticate_api_key,
        check_sufficient_balance,
        log_inference_usage,
        DATABASE_PATH
    )

    # Extract API key from request
    api_key = request.get("api_key", "")
    if not api_key:
        return {"error": "API key required. Provide 'api_key' in request body or Authorization header."}

    # Authenticate user
    auth_result = authenticate_api_key(api_key)
    if "error" in auth_result:
        return {"error": auth_result["error"], "authenticated": False}

    user_id = auth_result["user_id"]
    api_key_id = auth_result["api_key_id"]
    user_email = auth_result["email"]
    user_balance = auth_result["balance"]

    # Estimate cost (assume 3 seconds average)
    estimated_time = 3.0
    estimated_cost = estimated_time * PRICE_PER_SECOND

    # Check sufficient balance
    has_balance, balance_msg = check_sufficient_balance(user_id, estimated_cost)
    if not has_balance:
        return {
            "error": balance_msg,
            "balance": user_balance,
            "estimated_cost": round(estimated_cost, 6),
            "authenticated": True
        }

    # Extract parameters
    prompt = request.get("prompt", "")
    max_length = request.get("max_length", 300)
    temperature = request.get("temperature", 0.7)

    if not prompt:
        return {"error": "prompt is required"}

    # Generate code
    try:
        inference = BioQLInference()
        result = inference.generate.remote(prompt, max_length, temperature)

        # Log usage to billing database
        log_inference_usage(
            user_id=user_id,
            api_key_id=api_key_id,
            prompt=prompt,
            code_generated=result["code"],
            time_seconds=result["timing"]["total_seconds"],
            base_cost=result["cost"]["base_cost_usd"],
            user_cost=result["cost"]["user_cost_usd"],
            profit=result["cost"]["profit_usd"],
            success=True,
            error_message=None
        )

        return {
            "code": result["code"],
            "prompt": prompt,
            "model": "bioql-lora-v1",
            "timing": result["timing"],
            "cost": result["cost"],
            "user": {
                "email": user_email,
                "balance": round(user_balance - result["cost"]["user_cost_usd"], 6)
            }
        }

    except Exception as e:
        # Log failed attempt
        log_inference_usage(
            user_id=user_id,
            api_key_id=api_key_id,
            prompt=prompt,
            code_generated="",
            time_seconds=0.0,
            base_cost=0.0,
            user_cost=0.0,
            profit=0.0,
            success=False,
            error_message=str(e)
        )

        return {
            "error": f"Generation failed: {str(e)}",
            "authenticated": True
        }


@app.local_entrypoint()
def test():
    """Test the inference server locally with cost tracking."""
    print("\n🧪 Testing BioQL Inference Server with Cost Tracking\n")

    inference = BioQLInference()

    test_prompts = [
        "Create a Bell state",
        "Run QFT on 4 qubits",
        "Create 3 qubit GHZ state",
    ]

    total_cost = 0.0
    total_profit = 0.0

    for i, prompt in enumerate(test_prompts, 1):
        print(f"\n{'='*70}")
        print(f"Test {i}/{len(test_prompts)}: {prompt}")
        print("=" * 70)

        result = inference.generate.remote(prompt, max_length=200)

        print("\n📝 Generated Code:")
        print("-" * 70)
        print(result["code"])
        print("-" * 70)

        print("\n⏱️  Timing:")
        print(f"   Total: {result['timing']['total_seconds']}s")
        print(f"   Generation: {result['timing']['generation_seconds']}s")
        print(f"   Overhead: {result['timing']['overhead_seconds']}s")

        print("\n💰 Cost Breakdown:")
        print(f"   Base Cost (Modal): ${result['cost']['base_cost_usd']:.6f}")
        print(f"   User Price: ${result['cost']['user_cost_usd']:.6f}")
        print(f"   Profit: ${result['cost']['profit_usd']:.6f} ({result['cost']['profit_margin_percent']}% margin)")

        total_cost += result['cost']['user_cost_usd']
        total_profit += result['cost']['profit_usd']

    print("\n" + "=" * 70)
    print("📊 Summary")
    print("=" * 70)
    print(f"Total User Cost: ${total_cost:.6f}")
    print(f"Total Profit: ${total_profit:.6f}")
    print(f"Average per Request: ${total_cost/len(test_prompts):.6f}")
    print("=" * 70)

    print("\n✅ Testing complete!\n")
