"""
BioQL Simple Agent - Agent wrapper que usa el modelo solo para código
=====================================================================
El agente decide tools, el modelo solo genera código
"""

import modal
import time

billing_volume = modal.Volume.from_name("bioql-billing", create_if_missing=True)
model_volume = modal.Volume.from_name("bioql-deepseek")

# Inline billing functions (to avoid module import issues)
import hashlib
import sqlite3
from typing import Dict, Any

DATABASE_PATH = "/billing/bioql_billing.db"

def authenticate_api_key(api_key: str) -> Dict[str, Any]:
    """Authenticate API key."""
    if not api_key:
        return {"error": "API key required"}

    try:
        api_key_hash = hashlib.sha256(api_key.encode()).hexdigest()

        conn = sqlite3.connect(DATABASE_PATH)
        conn.row_factory = sqlite3.Row
        cursor = conn.cursor()

        cursor.execute("""
            SELECT
                u.id, u.email, u.name, u.current_plan, u.is_active,
                u.tier_id, ak.id as api_key_id,
                t.name as tier_name,
                t.quota_simulator, t.quota_gpu, t.quota_quantum,
                t.rate_limit_per_minute,
                COALESCE(b.balance, 0.0) as balance
            FROM users u
            JOIN api_keys ak ON u.id = ak.user_id
            LEFT JOIN pricing_tiers t ON u.tier_id = t.id
            LEFT JOIN (
                SELECT user_id, SUM(amount) as balance
                FROM billing_transactions
                GROUP BY user_id
            ) b ON u.id = b.user_id
            WHERE ak.key_hash = ? AND ak.is_active = 1 AND u.is_active = 1
        """, (api_key_hash,))

        result = cursor.fetchone()
        conn.close()

        if not result:
            return {"error": "Invalid or inactive API key"}

        return {
            "user_id": result["id"],
            "email": result["email"],
            "name": result["name"] or "Unknown",
            "plan": result["current_plan"],
            "api_key_id": result["api_key_id"],
            "tier_id": result["tier_id"] or "tier_free",
            "tier_name": result["tier_name"] or "free",
            "quota_gpu": result["quota_gpu"] or 10,
            "rate_limit": result["rate_limit_per_minute"] or 10,
            "balance": float(result["balance"])
        }
    except Exception as e:
        return {"error": f"Authentication failed: {str(e)}"}

def check_sufficient_balance(user_id: str, estimated_cost: float = 0.01) -> Dict[str, Any]:
    """Check if user has sufficient balance."""
    try:
        conn = sqlite3.connect(DATABASE_PATH)
        cursor = conn.cursor()

        cursor.execute("""
            SELECT COALESCE(SUM(amount), 0.0) as balance
            FROM billing_transactions
            WHERE user_id = ?
        """, (user_id,))

        result = cursor.fetchone()
        conn.close()

        balance = result[0] if result else 0.0

        if balance < estimated_cost:
            return {
                "sufficient": False,
                "balance": balance,
                "message": f"Insufficient balance: ${balance:.6f} < ${estimated_cost:.6f}"
            }

        return {
            "sufficient": True,
            "balance": balance,
            "message": f"Balance OK: ${balance:.6f}"
        }
    except Exception as e:
        return {
            "sufficient": False,
            "balance": 0.0,
            "message": f"Balance check failed: {str(e)}"
        }

def log_inference_usage(
    user_id: str,
    api_key_id: str,
    prompt: str,
    code_generated: str,
    time_seconds: float,
    base_cost: float,
    user_cost: float,
    profit: float,
    success: bool = True,
    error_message: str = None
) -> bool:
    """Log inference usage."""
    try:
        conn = sqlite3.connect(DATABASE_PATH)
        cursor = conn.cursor()

        cursor.execute("""
            INSERT INTO inference_logs
            (user_id, api_key_id, prompt, code_generated, time_seconds,
             base_cost, user_cost, profit, success, error_message)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        """, (user_id, api_key_id, prompt, code_generated, time_seconds,
              base_cost, user_cost, profit, success, error_message))

        cursor.execute("""
            INSERT INTO billing_transactions (user_id, amount, transaction_type, description)
            VALUES (?, ?, ?, ?)
        """, (user_id, -user_cost, "inference", f"Code generation: {prompt[:100]}"))

        conn.commit()
        conn.close()
        return True
    except Exception as e:
        print(f"Failed to log usage: {e}")
        return False

image = (
    modal.Image.debian_slim(python_version="3.11")
    .pip_install(
        "torch==2.1.0",
        "transformers==4.37.0",
        "peft==0.7.0",
        "fastapi==0.109.0",
        "accelerate==0.25.0",
    )
)

app = modal.App(name="bioql-agent-simple", image=image)

MODAL_A10G_COST_PER_SECOND = 0.000305556
PROFIT_MARGIN = 0.40
PRICE_PER_SECOND = MODAL_A10G_COST_PER_SECOND * (1 + PROFIT_MARGIN)


@app.cls(
    gpu="A10G",
    volumes={"/billing": billing_volume, "/model": model_volume},
    scaledown_window=300,
)
class SimpleBioQLAgent:
    """Agent que decide actions y usa el modelo para código."""

    @modal.enter()
    def load_model(self):
        import torch
        from transformers import AutoTokenizer, AutoModelForCausalLM
        from peft import PeftModel

        print("🤖 Loading Simple BioQL Agent...")

        base_model_name = "deepseek-ai/deepseek-coder-1.3b-instruct"
        self.tokenizer = AutoTokenizer.from_pretrained(base_model_name)
        if self.tokenizer.pad_token is None:
            self.tokenizer.pad_token = self.tokenizer.eos_token

        base_model = AutoModelForCausalLM.from_pretrained(
            base_model_name,
            device_map="auto",
            torch_dtype=torch.bfloat16
        )

        self.model = PeftModel.from_pretrained(
            base_model,
            "/model/final_model",
            torch_dtype=torch.bfloat16
        )
        self.model.eval()
        print("✅ Simple Agent ready")

    @modal.method()
    def execute(self, user_request: str, workspace_context: dict = None) -> dict:
        """Ejecuta request decidiendo qué hacer."""
        import re
        import torch

        workspace_context = workspace_context or {}

        # Analizar request y decidir action
        request_lower = user_request.lower()

        # Check if file content was provided in context (for review/fix requests)
        file_content = workspace_context.get('file_content', '')
        current_file = workspace_context.get('current_file', '')

        # Decision tree basado en keywords
        if any(word in request_lower for word in ['review', 'fix', 'analyze', 'debug']) and file_content:
            # Review/fix code usando el contenido enviado
            prompt = f"""### Instruction:
Review and fix this BioQL code file: {current_file}

Code to review:
```python
{file_content[:2000]}  # Limit to first 2000 chars
```

{user_request}

Provide specific fixes and improvements.

### Response:
"""
            inputs = self.tokenizer(prompt, return_tensors="pt").to(self.model.device)

            with torch.no_grad():
                outputs = self.model.generate(
                    **inputs,
                    max_new_tokens=500,
                    temperature=0.3,  # Lower temp for code review
                    do_sample=True,
                    pad_token_id=self.tokenizer.pad_token_id,
                    eos_token_id=self.tokenizer.eos_token_id,
                )

            response = self.tokenizer.decode(outputs[0], skip_special_tokens=True)

            # Extract the review/fixes
            if "### Response:" in response:
                review = response.split("### Response:")[-1].strip()
            else:
                review = response.strip()

            return {
                'success': True,
                'action': 'review_code',
                'response': review,
                'file_reviewed': current_file,
                'reasoning': f'Reviewed {len(file_content)} chars of code'
            }

        elif any(word in request_lower for word in ['create', 'generate', 'write code', 'bell state', 'quantum', 'docking', 'dock', 'molecular']):
            # Generar código con el modelo - USAR FORMATO DE ENTRENAMIENTO

            # Detectar si es docking molecular
            is_docking = any(word in request_lower for word in ['docking', 'dock', 'molecular', 'binding', 'protein', 'ligand'])

            # IMPORTANTE: El modelo fue entrenado con este formato EXACTO:
            # ### Instruction:
            # {instruction}
            #
            # ### Reasoning:
            # {reasoning}
            #
            # ### Code:
            # {code}

            if is_docking:
                # Few-shot: Dar ejemplo del entrenamiento antes del request
                prompt = f"""### Instruction:
Dock ibuprofen to COX-2 protein

### Reasoning:
Molecular docking uses the dock() function with natural language description, SMILES string, and PDB code.

### Code:
from bioql.docking import dock

result = dock(
    "dock ibuprofen to COX-2 protein and calculate binding affinity",
    ligand_smiles="CC(C)Cc1ccc(cc1)[C@@H](C)C(=O)O",
    protein_pdb="1CX2",
    backend="simulator",
    shots=1000
)
print("Binding affinity:", result.score)

### Instruction:
{user_request}

### Reasoning:"""
            else:
                # Few-shot para quantum
                prompt = f"""### Instruction:
Create a Bell state using BioQL

### Reasoning:
A Bell state is a maximally entangled 2-qubit state. Steps: 1) Apply Hadamard to qubit 0 to create superposition, 2) Apply CNOT with qubit 0 as control and qubit 1 as target to create entanglement.

### Code:
from bioql import quantum

result = quantum("Create Bell state on 2 qubits", backend="simulator", shots=1000)
print(result)

### Instruction:
{user_request}

### Reasoning:"""

            inputs = self.tokenizer(prompt, return_tensors="pt").to(self.model.device)
            prompt_length = inputs['input_ids'].shape[1]  # Guardar longitud del prompt

            with torch.no_grad():
                outputs = self.model.generate(
                    **inputs,
                    max_new_tokens=400,  # Suficiente para reasoning + code completo
                    temperature=0.3,  # No tan baja para evitar cortes
                    do_sample=True,
                    top_p=0.9,
                    pad_token_id=self.tokenizer.pad_token_id,
                    eos_token_id=self.tokenizer.eos_token_id,
                    repetition_penalty=1.2,  # Evitar copiar el ejemplo
                    no_repeat_ngram_size=5
                )

            # Decodificar TODO el output
            generated = self.tokenizer.decode(outputs[0], skip_special_tokens=True)

            # DEBUG: Ver qué genera el modelo
            raw_output = generated  # Guardar para debug

            # El modelo copia el prompt Y genera la respuesta
            # Buscar la ÚLTIMA aparición de "### Instruction:" que es donde empieza SU respuesta
            instruction_splits = generated.split("### Instruction:")

            if len(instruction_splits) > 1:
                # Tomar la última parte (la respuesta del modelo al último instruction)
                model_response = instruction_splits[-1]
            else:
                # No hay ### Instruction:, usar todo
                model_response = generated

            code = ""
            reasoning = ""

            # Extraer reasoning y code de la respuesta
            # El modelo puede generar: "{request}\n\n### Reasoning:\n{text}\n\n### Code:\n{code}"
            # Primero saltar el request y llegar al ### Reasoning:
            if "### Reasoning:" in model_response:
                reasoning_part = model_response.split("### Reasoning:")[-1]
            elif "###Reasoning:" in model_response:
                reasoning_part = model_response.split("###Reasoning:")[-1]
            else:
                reasoning_part = model_response

            # Ahora buscar el código
            code_marker = None
            if "### Code:" in reasoning_part:
                code_marker = "### Code:"
            elif "###Code:" in reasoning_part:
                code_marker = "###Code:"

            if code_marker:
                parts = reasoning_part.split(code_marker)
                reasoning = parts[0].strip()
                code = parts[1].strip() if len(parts) > 1 else ""
            else:
                # Solo hay reasoning, no code
                reasoning = reasoning_part.strip()

            # Limpiar código
            # Remover markdown code blocks si existen
            if "```python" in code:
                code = code.split("```python")[1].split("```")[0].strip()
            elif "```" in code:
                code = code.split("```")[1].split("```")[0].strip()

            # Limpiar marcadores sobrantes
            code = code.replace("###", "").strip()

            # Validar que el código es bueno
            is_valid = (
                len(code) > 50 and  # Tiene contenido
                ('from bioql' in code or 'import bioql' in code) and  # Usa BioQL
                code.count('}') < 5  # No tiene repeticiones raras
            )

            # Si el código no es válido, usar template
            original_code = code  # Guardar para debug
            if not is_valid:
                if is_docking:
                    code = self._generate_docking_template(user_request)
                    reasoning = f"Template fallback (model generated: {len(original_code)} chars)"
                else:
                    code = self._generate_quantum_template(user_request)
                    reasoning = f"Template fallback (model generated: {len(original_code)} chars)"

            return {
                'success': True,
                'action': 'generate_code',
                'code': code,
                'reasoning': reasoning if reasoning else f'Generated {"docking" if is_docking else "quantum"} code',
                'debug': {
                    'raw_model_output': raw_output[:1000],  # First 1000 chars
                    'parsed_code': original_code[:500] if original_code else "",
                    'parsed_code_length': len(original_code),
                    'used_template': not is_valid,
                    'validation_passed': is_valid
                }
            }

        elif 'list' in request_lower and 'file' in request_lower:
            # List files
            import os
            workspace = workspace_context.get('workspace', '/tmp')
            try:
                files = os.listdir(workspace)
                return {
                    'success': True,
                    'action': 'list_files',
                    'result': '\n'.join(files),
                    'reasoning': f'Listed files in {workspace}'
                }
            except Exception as e:
                return {'success': False, 'error': str(e)}

        elif 'read' in request_lower and 'file' in request_lower:
            # Read file
            import os
            file_match = re.search(r'(\w+\.py|\w+/\w+\.py)', user_request)
            if file_match:
                file_path = os.path.join(
                    workspace_context.get('workspace', '/tmp'),
                    file_match.group(1)
                )
                try:
                    with open(file_path, 'r') as f:
                        content = f.read()
                    return {
                        'success': True,
                        'action': 'read_file',
                        'result': content,
                        'file': file_match.group(1)
                    }
                except Exception as e:
                    return {'success': False, 'error': str(e)}

        elif any(word in request_lower for word in ['run', 'execute']):
            # Generate and run code
            prompt = f"""### Instruction:
{user_request}

### Code:
"""
            inputs = self.tokenizer(prompt, return_tensors="pt").to(self.model.device)

            with torch.no_grad():
                outputs = self.model.generate(
                    **inputs,
                    max_new_tokens=200,
                    temperature=0.5,
                    do_sample=True,
                    pad_token_id=self.tokenizer.pad_token_id,
                    eos_token_id=self.tokenizer.eos_token_id,
                )

            generated = self.tokenizer.decode(outputs[0], skip_special_tokens=True)

            # Extract code
            if "### Code:" in generated:
                code = generated.split("### Code:")[-1].strip()
            else:
                code = generated.strip()

            # Run it
            import subprocess
            temp_file = '/tmp/agent_exec.py'
            with open(temp_file, 'w') as f:
                f.write(code)

            try:
                result = subprocess.run(
                    ['python3', temp_file],
                    capture_output=True,
                    text=True,
                    timeout=30
                )

                return {
                    'success': result.returncode == 0,
                    'action': 'execute_code',
                    'code': code,
                    'result': result.stdout if result.returncode == 0 else result.stderr
                }
            except Exception as e:
                return {'success': False, 'action': 'execute_code', 'error': str(e)}

        else:
            # Default: use model to answer
            prompt = f"""### Instruction:
{user_request}

### Response:
"""
            inputs = self.tokenizer(prompt, return_tensors="pt").to(self.model.device)

            with torch.no_grad():
                outputs = self.model.generate(
                    **inputs,
                    max_new_tokens=200,
                    temperature=0.7,
                    do_sample=True,
                    pad_token_id=self.tokenizer.pad_token_id,
                    eos_token_id=self.tokenizer.eos_token_id,
                )

            response = self.tokenizer.decode(outputs[0], skip_special_tokens=True)

            return {
                'success': True,
                'action': 'answer',
                'response': response
            }

    def _generate_docking_template(self, request: str) -> str:
        """Generate a docking template when model output is poor."""
        # Extract ligand and target from request
        import re

        # Try to find molecule names
        ligand = "aspirin"  # default
        target = "COX-2"  # default

        # Look for common patterns
        ligand_match = re.search(r'(?:ligand|drug|molecule|compound)[\s:]+(\w+)', request, re.IGNORECASE)
        target_match = re.search(r'(?:target|protein|receptor)[\s:]+(\w+[-]?\w*)', request, re.IGNORECASE)

        # Or just find capitalized words that might be molecules
        words = re.findall(r'\b[A-Z][A-Za-z0-9-]+\b', request)
        if len(words) >= 2:
            ligand = words[0]
            target = words[1]
        elif len(words) == 1:
            ligand = words[0]

        if ligand_match:
            ligand = ligand_match.group(1)
        if target_match:
            target = target_match.group(1)

        return f'''"""
Molecular Docking Analysis
==========================
Docking {ligand} against {target} protein.
"""

from bioql.docking import dock_molecules

def run_docking():
    """Perform molecular docking analysis."""
    try:
        print(f"🔬 Starting docking: {ligand} → {target}")

        # Perform docking
        result = dock_molecules(
            ligand="{ligand}",
            target="{target}",
            exhaustiveness=8,
            num_modes=5
        )

        # Display results
        print(f"✅ Docking complete!")
        print(f"📊 Binding Affinity: {{result['affinity']}} kcal/mol")
        print(f"📍 Number of poses: {{len(result['poses'])}}")

        # Show top 3 poses
        for i, pose in enumerate(result['poses'][:3]):
            print(f"  Pose {{i+1}}: {{pose['affinity']}} kcal/mol")

        return result

    except Exception as e:
        print(f"❌ Error: {{e}}")
        raise

if __name__ == "__main__":
    results = run_docking()
'''

    def _generate_quantum_template(self, request: str) -> str:
        """Generate a quantum template when model output is poor."""
        # Detect what kind of quantum circuit
        request_lower = request.lower()

        if 'bell' in request_lower:
            circuit_desc = "Create a Bell state (maximally entangled pair)"
            nl_request = "Create a Bell state with two qubits"
        elif 'ghz' in request_lower:
            circuit_desc = "Create a GHZ state (3-qubit entanglement)"
            nl_request = "Create GHZ state with 3 qubits"
        elif 'teleport' in request_lower:
            circuit_desc = "Quantum teleportation circuit"
            nl_request = "Create quantum teleportation circuit"
        else:
            circuit_desc = "Quantum circuit"
            nl_request = "Create a Bell state"

        return f'''"""
{circuit_desc}
{'=' * len(circuit_desc)}
"""

from bioql import quantum

def run_circuit():
    """Execute quantum circuit on simulator."""
    try:
        print("🔬 Running quantum circuit...")

        # Create and run circuit
        result = quantum(
            "{nl_request}",
            backend="simulator",
            shots=1000
        )

        # Display results
        print("✅ Circuit executed!")
        print(f"📊 Results: {{result}}")

        return result

    except Exception as e:
        print(f"❌ Error: {{e}}")
        raise

if __name__ == "__main__":
    results = run_circuit()
'''


@app.function(volumes={"/billing": billing_volume, "/model": model_volume})
@modal.fastapi_endpoint(method="POST")
def simple_agent(request: dict) -> dict:
    """Simple agent endpoint."""
    # Billing functions are defined at module level (no import needed)

    # Auth
    api_key = request.get("api_key", "")
    if not api_key:
        return {"error": "API key required"}

    auth_result = authenticate_api_key(api_key)
    if "error" in auth_result:
        return {"error": auth_result["error"]}

    user_id = auth_result["user_id"]
    api_key_id = auth_result["api_key_id"]
    user_email = auth_result["email"]
    user_balance = auth_result["balance"]

    # Check balance
    estimated_cost = 5.0 * PRICE_PER_SECOND
    has_balance, balance_msg = check_sufficient_balance(user_id, estimated_cost)
    if not has_balance:
        return {"error": balance_msg, "balance": user_balance}

    # Extract params
    user_request = request.get("request", "")
    workspace_context = request.get("workspace_context", {})

    if not user_request:
        return {"error": "request is required"}

    # Execute
    start_time = time.time()

    try:
        agent = SimpleBioQLAgent()
        result = agent.execute.remote(user_request, workspace_context)

        execution_time = time.time() - start_time

        # Calculate costs
        base_cost = execution_time * MODAL_A10G_COST_PER_SECOND
        user_cost = execution_time * PRICE_PER_SECOND
        profit = user_cost - base_cost

        # Log
        log_inference_usage(
            user_id=user_id,
            api_key_id=api_key_id,
            prompt=f"SIMPLE_AGENT: {user_request}",
            code_generated=result.get('code', ''),
            time_seconds=execution_time,
            base_cost=base_cost,
            user_cost=user_cost,
            profit=profit,
            success=result['success'],
            error_message=result.get('error')
        )

        return {
            **result,
            "model": "bioql-simple-agent",
            "timing": {"total_seconds": round(execution_time, 3)},
            "cost": {
                "base_cost_usd": round(base_cost, 6),
                "user_cost_usd": round(user_cost, 6),
                "profit_usd": round(profit, 6)
            },
            "user": {
                "email": user_email,
                "balance": round(user_balance - user_cost, 6)
            }
        }

    except Exception as e:
        execution_time = time.time() - start_time

        log_inference_usage(
            user_id=user_id,
            api_key_id=api_key_id,
            prompt=f"SIMPLE_AGENT: {user_request}",
            code_generated="",
            time_seconds=execution_time,
            base_cost=0.0,
            user_cost=0.0,
            profit=0.0,
            success=False,
            error_message=str(e)
        )

        return {"error": f"Agent failed: {str(e)}"}
