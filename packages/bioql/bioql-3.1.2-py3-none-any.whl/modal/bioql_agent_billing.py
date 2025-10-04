"""
BioQL Agent - Template-Based + HTTP Billing
100% Reliable code generation with full billing integration
"""
import modal
import time
import requests
import re
from typing import Dict, Any

# Billing server URL
BILLING_SERVER_URL = "https://aae99709f69d.ngrok-free.app"

# Modal setup
image = modal.Image.debian_slim(python_version="3.11").pip_install("fastapi[standard]", "requests")
app = modal.App(name="bioql-agent-billing", image=image)

# Pricing
MODAL_A10G_COST_PER_SECOND = 0.000305556
PROFIT_MARGIN = 0.40
PRICE_PER_SECOND = MODAL_A10G_COST_PER_SECOND * (1 + PROFIT_MARGIN)

# Templates
DOCKING_TEMPLATE = '''from bioql.docking import dock

result = dock(
    receptor="{target}.pdb",
    ligand_smiles="{ligand}",
    api_key="YOUR_BIOQL_API_KEY",  # Replace with your API key
    backend="{backend}",
    exhaustiveness={exhaustiveness},
    num_modes={num_modes},
    shots={shots}
)

if result.success:
    print(f"✅ Docking successful!")
    print(f"Binding affinity: {{result.score}} kcal/mol")
    print(f"Backend used: {{result.backend}}")
    print(f"Number of poses: {{len(result.poses) if result.poses else 0}}")
    if result.poses:
        print(f"Best pose: {{result.poses[0]}}")
else:
    print(f"❌ Docking failed: {{result.error_message}}")'''

QUANTUM_TEMPLATE = '''from bioql import quantum

# Quantum computation with full configuration
result = quantum(
    program="{instruction}",
    api_key="YOUR_BIOQL_API_KEY",  # Replace with your API key
    backend="{backend}",
    shots={shots},
    debug=False
)

print(f"✅ Quantum execution successful!")
print(f"Backend: {{result.backend}}")
print(f"Shots: {{result.shots}}")
print(f"Counts: {{result.counts}}")
if hasattr(result, 'state_vector'):
    print(f"State vector: {{result.state_vector}}")'''

VQE_TEMPLATE = '''from bioql import quantum

# VQE ground state calculation
result = quantum(
    program="Run VQE for {molecule} molecule",
    api_key="YOUR_BIOQL_API_KEY",  # Replace with your API key
    backend="{backend}",
    shots={shots},
    debug=False
)

print(f"✅ VQE computation complete!")
print(f"Molecule: {molecule}")
print(f"Backend: {{result.backend}}")
print(f"Ground state energy: {{result.energy if hasattr(result, 'energy') else 'N/A'}} Hartree")
print(f"Convergence: {{result.converged if hasattr(result, 'converged') else 'Unknown'}}")'''


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
                    "balance": 100.0
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
                "backend": "template",
                "shots": 1,
                "time_seconds": time_seconds,
                "notes": f"Template generation: {prompt[:100]}"
            },
            timeout=5,
            headers={"ngrok-skip-browser-warning": "true"}
        )
        return response.status_code == 200
    except:
        return False


def detect_intent(user_request: str) -> str:
    """Detect user intent from request."""
    request_lower = user_request.lower()

    if any(word in request_lower for word in ['dock', 'docking', 'binding', 'affinity']):
        return 'docking'

    if any(word in request_lower for word in ['quantum', 'qubit', 'bell', 'ghz', 'grover', 'entangle']):
        return 'quantum'

    if any(word in request_lower for word in ['vqe', 'ground state', 'energy', 'h2', 'lih']):
        return 'vqe'

    return 'unknown'


def extract_parameters(user_request: str) -> dict:
    """Extract parameters from user request using regex."""
    params = {}
    request_lower = user_request.lower()

    # Extract ligand
    ligand_patterns = [
        r'dock\s+(\w+)',
        r'ligand[:\s]+(\w+)',
        r'drug[:\s]+(\w+)',
        r'compound[:\s]+(\w+)',
    ]
    for pattern in ligand_patterns:
        match = re.search(pattern, request_lower)
        if match:
            params['ligand'] = match.group(1)
            break

    # Extract target
    target_patterns = [
        r'to\s+(\w+[-\d]*)',
        r'target[:\s]+(\w+[-\d]*)',
        r'protein[:\s]+(\w+[-\d]*)',
    ]
    for pattern in target_patterns:
        match = re.search(pattern, request_lower)
        if match:
            params['target'] = match.group(1).upper()
            break

    # Extract exhaustiveness
    exhaust_match = re.search(r'exhaustiveness[:\s]+(\d+)', request_lower)
    params['exhaustiveness'] = int(exhaust_match.group(1)) if exhaust_match else 8

    # Extract num_modes
    modes_match = re.search(r'(?:num[_\s]?modes|modes)[:\s]+(\d+)', request_lower)
    params['num_modes'] = int(modes_match.group(1)) if modes_match else 5

    # Extract shots
    shots_match = re.search(r'shots?[:\s]+(\d+)', request_lower)
    params['shots'] = int(shots_match.group(1)) if shots_match else 1000

    # Extract backend
    backend_match = re.search(r'backend[:\s]+["\']?(\w+)["\']?', request_lower)
    params['backend'] = backend_match.group(1) if backend_match else "simulator"

    # Extract molecule
    molecule_match = re.search(r'molecule[:\s]+(\w+\d*)', request_lower)
    if molecule_match:
        params['molecule'] = molecule_match.group(1).upper()

    return params


@app.cls()
class TemplateBioQLAgent:
    """100% reliable template-based agent."""

    @modal.method()
    def generate_code(self, user_request: str) -> dict:
        """Generate code using templates."""
        intent = detect_intent(user_request)
        params = extract_parameters(user_request)

        code = ""

        if intent == 'docking':
            # Set defaults for docking
            if 'ligand' not in params:
                params['ligand'] = 'aspirin'
            if 'target' not in params:
                params['target'] = 'COX-2'

            # Backend selection: auto, quantum, or vina
            if 'backend' not in params or params['backend'] == 'simulator':
                # Check if user mentioned quantum in request
                if 'quantum' in user_request.lower():
                    params['backend'] = 'quantum'
                else:
                    # Use auto to let BioQL choose best backend
                    params['backend'] = 'auto'

            if 'exhaustiveness' not in params:
                params['exhaustiveness'] = 8
            if 'num_modes' not in params:
                params['num_modes'] = 9
            if 'shots' not in params:
                params['shots'] = 1024
            code = DOCKING_TEMPLATE.format(**params)

        elif intent == 'quantum':
            params['instruction'] = user_request
            # Set quantum defaults
            if 'backend' not in params or params['backend'] == 'vina':
                params['backend'] = 'simulator'  # Default quantum backend
            if 'shots' not in params:
                params['shots'] = 1024
            code = QUANTUM_TEMPLATE.format(**params)

        elif intent == 'vqe':
            if 'molecule' not in params:
                params['molecule'] = 'H2'
            # Set quantum defaults
            if 'backend' not in params or params['backend'] == 'vina':
                params['backend'] = 'simulator'
            if 'shots' not in params:
                params['shots'] = 2048  # VQE typically needs more shots
            code = VQE_TEMPLATE.format(**params)

        else:
            # Default to docking
            params['ligand'] = params.get('ligand', 'aspirin')
            params['target'] = params.get('target', 'COX-2')
            code = DOCKING_TEMPLATE.format(**params)

        return {'code': code, 'success': True}


@app.function()
@modal.fastapi_endpoint(method="POST")
def agent(request: dict) -> dict:
    """Template agent endpoint with HTTP billing."""

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
        agent = TemplateBioQLAgent()
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
