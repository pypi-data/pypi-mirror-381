"""
BioQL Inference Server - Base Model (No LoRA)
==============================================

Uses base Qwen2.5-7B model without LoRA for stable inference.
Integrated with BioQL billing system.
"""

import modal
import time

# Create volume references
billing_volume = modal.Volume.from_name("bioql-billing-db")

# Image with inference dependencies
image = (
    modal.Image.debian_slim(python_version="3.11")
    .pip_install(
        "torch==2.1.0",
        "transformers==4.37.0",
        "fastapi==0.109.0",
        "accelerate==0.25.0",
    )
)

app = modal.App(name="bioql-inference-base", image=image)

# Pricing Configuration
MODAL_A10G_COST_PER_SECOND = 0.000305556  # $1.10/hour
PROFIT_MARGIN = 0.40  # 40% markup
PRICE_PER_SECOND = MODAL_A10G_COST_PER_SECOND * (1 + PROFIT_MARGIN)


@app.cls(
    gpu="A10G",
    volumes={"/billing": billing_volume},
    scaledown_window=300,
)
class BioQLInference:
    """BioQL code generation inference server."""

    @modal.enter()
    def load_model(self):
        """Load base model on container start."""
        import torch
        from transformers import AutoTokenizer, AutoModelForCausalLM

        print("🔄 Loading Qwen2.5-7B base model...")

        base_model = "Qwen/Qwen2.5-7B-Instruct"

        # Load tokenizer
        self.tokenizer = AutoTokenizer.from_pretrained(
            base_model,
            trust_remote_code=True
        )

        # Load base model in fp16 (no quantization for stability)
        self.model = AutoModelForCausalLM.from_pretrained(
            base_model,
            device_map="auto",
            torch_dtype=torch.float16,
            trust_remote_code=True
        )

        print("✅ Base model loaded successfully!")

    @modal.method()
    def generate(
        self,
        prompt: str,
        max_length: int = 300,
        temperature: float = 0.7
    ) -> dict:
        """Generate BioQL code from natural language."""
        import torch

        start_time = time.time()

        # Format prompt for BioQL code generation
        formatted_prompt = f"""You are a BioQL quantum programming assistant. Generate clean, executable BioQL code.

User request: {prompt}

BioQL code:
```python
"""

        inputs = self.tokenizer(formatted_prompt, return_tensors="pt").to(self.model.device)

        generation_start = time.time()
        with torch.no_grad():
            outputs = self.model.generate(
                **inputs,
                max_new_tokens=max_length,
                temperature=temperature,
                top_p=0.9,
                do_sample=True,
                pad_token_id=self.tokenizer.eos_token_id,
                eos_token_id=self.tokenizer.eos_token_id
            )
        generation_time = time.time() - generation_start

        generated = self.tokenizer.decode(outputs[0], skip_special_tokens=True)

        # Extract code part
        if "```python" in generated:
            code = generated.split("```python")[-1].split("```")[0].strip()
        elif "BioQL code:" in generated:
            code = generated.split("BioQL code:")[-1].strip()
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
    """
    import sys
    sys.path.insert(0, "/billing")
    from billing_integration import (
        authenticate_api_key,
        check_sufficient_balance,
        log_inference_usage
    )

    # Extract API key
    api_key = request.get("api_key", "")
    if not api_key:
        return {"error": "API key required"}

    # Authenticate user
    auth_result = authenticate_api_key(api_key)
    if "error" in auth_result:
        return {"error": auth_result["error"], "authenticated": False}

    user_id = auth_result["user_id"]
    api_key_id = auth_result["api_key_id"]
    user_email = auth_result["email"]
    user_balance = auth_result["balance"]

    # Estimate cost (3 seconds average)
    estimated_cost = 3.0 * PRICE_PER_SECOND

    # Check balance
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

        # Log usage
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
            "model": "qwen2.5-7b-base",
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
