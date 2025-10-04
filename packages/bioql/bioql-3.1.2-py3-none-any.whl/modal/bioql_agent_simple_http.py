"""
BioQL Simple Agent - Using HTTP Billing Server
"""
import modal
import time
import requests
from typing import Dict, Any

# Your ngrok billing server
BILLING_SERVER_URL = "https://aae99709f69d.ngrok-free.app"

model_volume = modal.Volume.from_name("bioql-deepseek")

image = (
    modal.Image.debian_slim(python_version="3.11")
    .pip_install(
        "torch==2.1.0",
        "transformers==4.37.0",
        "peft==0.7.0",
        "fastapi[standard]",
        "accelerate==0.25.0",
        "requests",
    )
)

app = modal.App(name="bioql-agent-simple-http", image=image)

MODAL_A10G_COST_PER_SECOND = 0.000305556
PROFIT_MARGIN = 0.40
PRICE_PER_SECOND = MODAL_A10G_COST_PER_SECOND * (1 + PROFIT_MARGIN)


def authenticate_api_key(api_key: str) -> Dict[str, Any]:
    """Authenticate via HTTP billing server."""
    try:
        response = requests.post(
            f"{BILLING_SERVER_URL}/auth/validate",
            json={"api_key": api_key},
            timeout=10,
            headers={"ngrok-skip-browser-warning": "true"}
        )

        if response.status_code == 200:
            data = response.json()
            if data.get("valid"):
                return {
                    "user_id": data["user"]["id"],
                    "email": data["user"]["email"],
                    "name": data["user"]["name"],
                    "api_key_id": api_key,
                    "tier": data["user"]["tier"],
                    "quotas": data["quotas"],
                    "balance": 100.0  # Mock balance
                }

        return {"error": "Invalid API key"}
    except Exception as e:
        return {"error": f"Auth failed: {str(e)}"}


def log_inference_usage(
    user_id: str,
    api_key: str,
    prompt: str,
    code_generated: str,
    time_seconds: float,
    user_cost: float,
    success: bool = True,
    error_message: str = None
) -> bool:
    """Log usage to billing server."""
    try:
        response = requests.post(
            f"{BILLING_SERVER_URL}/billing/log-usage",
            json={
                "api_key": api_key,
                "backend": "gpu",
                "shots": 1,
                "time_seconds": time_seconds,
                "notes": f"Code generation: {prompt[:100]}"
            },
            timeout=5,
            headers={"ngrok-skip-browser-warning": "true"}
        )
        return response.status_code == 200
    except:
        return False


@app.cls(gpu="A10G", volumes={"/model": model_volume})
class SimpleBioQLAgent:
    @modal.enter()
    def load_model(self):
        import torch
        from transformers import AutoTokenizer, AutoModelForCausalLM
        from peft import PeftModel

        base_model = "deepseek-ai/deepseek-coder-6.7b-instruct"

        self.tokenizer = AutoTokenizer.from_pretrained(
            base_model,
            trust_remote_code=True
        )

        model = AutoModelForCausalLM.from_pretrained(
            base_model,
            torch_dtype=torch.float16,
            device_map="auto",
            trust_remote_code=True
        )

        self.model = PeftModel.from_pretrained(
            model,
            "/model/final_model",
            torch_dtype=torch.float16
        )

    @modal.method()
    def generate_code(
        self,
        user_request: str,
        max_tokens: int = 500,
        temperature: float = 0.1
    ) -> dict:
        """Generate BioQL code."""
        prompt = f"""Generate clean, executable BioQL code for the following request:

{user_request}

Code:"""

        inputs = self.tokenizer(prompt, return_tensors="pt").to("cuda")

        outputs = self.model.generate(
            **inputs,
            max_new_tokens=max_tokens,
            temperature=temperature,
            do_sample=True,
            pad_token_id=self.tokenizer.eos_token_id
        )

        generated = self.tokenizer.decode(outputs[0], skip_special_tokens=True)

        if "Code:" in generated:
            code = generated.split("Code:")[-1].strip()
        else:
            code = generated

        return {"code": code, "success": True}


@app.function()
@modal.fastapi_endpoint(method="POST")
def simple_agent(request: dict) -> dict:
    """Simple agent endpoint with HTTP billing."""

    # Auth
    api_key = request.get("api_key", "")
    if not api_key:
        return {"error": "API key required"}

    auth_result = authenticate_api_key(api_key)
    if "error" in auth_result:
        return {"error": auth_result["error"]}

    user_id = auth_result["user_id"]
    user_email = auth_result["email"]

    # Get request
    user_request = request.get("request", "")
    if not user_request:
        return {"error": "request is required"}

    # Generate code
    start_time = time.time()

    try:
        agent = SimpleBioQLAgent()
        result = agent.generate_code.remote(user_request)

        execution_time = time.time() - start_time

        # Calculate cost
        base_cost = execution_time * MODAL_A10G_COST_PER_SECOND
        user_cost = base_cost * (1 + PROFIT_MARGIN)
        profit = user_cost - base_cost

        # Log usage
        log_inference_usage(
            user_id=user_id,
            api_key=api_key,
            prompt=user_request,
            code_generated=result.get('code', ''),
            time_seconds=execution_time,
            user_cost=user_cost,
            success=result['success']
        )

        return {
            **result,
            "action": "code_generation",
            "timing": {"total_seconds": round(execution_time, 3)},
            "cost": {
                "base_cost_usd": round(base_cost, 6),
                "user_cost_usd": round(user_cost, 6),
                "profit_usd": round(profit, 6)
            },
            "user": {
                "email": user_email,
                "balance": round(100.0 - user_cost, 6)
            }
        }

    except Exception as e:
        return {"error": f"Code generation failed: {str(e)}"}
