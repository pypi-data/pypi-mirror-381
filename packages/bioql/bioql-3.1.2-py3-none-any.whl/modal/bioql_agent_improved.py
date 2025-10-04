"""
BioQL Agent con Modelo Mejorado 6.7B
=====================================

Usa DeepSeek-Coder-6.7B fine-tuned con:
- 15,000 ejemplos
- 40% enfocado en docking molecular
- Mejor arquitectura y entrenamiento
"""

import modal
import time
from typing import Optional

# Volumes
model_volume = modal.Volume.from_name("bioql-deepseek-improved", create_if_missing=True)
billing_volume = modal.Volume.from_name("bioql-billing", create_if_missing=True)

# Image with dependencies
image = (
    modal.Image.debian_slim(python_version="3.11")
    .pip_install(
        "torch==2.1.0",
        "transformers==4.37.0",
        "peft==0.7.0",
        "accelerate==0.25.0",
        "fastapi[standard]",  # Required for web endpoints
    )
)

app = modal.App(name="bioql-agent-improved", image=image)


@app.cls(
    gpu="A10G",  # A10G para inference
    volumes={
        "/model": model_volume,
        "/billing": billing_volume
    }
)
class ImprovedBioQLAgent:
    @modal.enter()
    def load_model(self):
        """Load improved 6.7B model."""
        import torch
        from transformers import AutoTokenizer, AutoModelForCausalLM
        from peft import PeftModel

        print("🔄 Loading improved DeepSeek-Coder-6.7B model...")

        # Load base model
        base_model_name = "deepseek-ai/deepseek-coder-6.7b-instruct"

        self.tokenizer = AutoTokenizer.from_pretrained(
            base_model_name,
            trust_remote_code=True
        )
        self.tokenizer.pad_token = self.tokenizer.eos_token

        # Load base model
        base_model = AutoModelForCausalLM.from_pretrained(
            base_model_name,
            device_map="auto",
            torch_dtype=torch.bfloat16,
            trust_remote_code=True
        )

        # Load LoRA weights from checkpoint-3500
        self.model = PeftModel.from_pretrained(
            base_model,
            "/model/improved_model/checkpoint-3500"
        )

        self.model.eval()

        print("✅ Improved 6.7B model loaded and ready!")

    @modal.method()
    def generate_code(
        self,
        user_request: str,
        max_tokens: int = 500,
        temperature: float = 0.2
    ) -> dict:
        """Generate BioQL code using improved model."""
        import torch
        import re

        # Detectar tipo de request
        request_lower = user_request.lower()
        is_docking = any(word in request_lower for word in ['docking', 'dock', 'molecular', 'binding', 'protein', 'ligand'])

        # Few-shot prompt
        if is_docking:
            prompt = f"""### Instruction:
Dock aspirin to COX-2 protein

### Reasoning:
Molecular docking simulates ligand-protein binding. Use the docking module with ligand name and target protein.

### Code:
from bioql.docking import dock_molecules

result = dock_molecules(
    ligand="aspirin",
    target="COX-2",
    exhaustiveness=8,
    num_modes=5
)

print(f"Binding affinity: {{result['affinity']}} kcal/mol")
print(f"Top pose: {{result['poses'][0]}}")

### Instruction:
{user_request}

### Reasoning:"""
        else:
            prompt = f"""### Instruction:
Create a Bell state using BioQL

### Reasoning:
A Bell state is a maximally entangled 2-qubit state. Apply H gate then CNOT.

### Code:
from bioql import quantum

result = quantum(
    "Create Bell state on 2 qubits",
    backend="simulator",
    shots=1000
)
print(result)

### Instruction:
{user_request}

### Reasoning:"""

        # Tokenize
        inputs = self.tokenizer(prompt, return_tensors="pt").to(self.model.device)
        prompt_length = inputs['input_ids'].shape[1]

        # Generate
        with torch.no_grad():
            outputs = self.model.generate(
                **inputs,
                max_new_tokens=max_tokens,
                temperature=temperature,
                do_sample=True,
                top_p=0.92,
                pad_token_id=self.tokenizer.pad_token_id,
                eos_token_id=self.tokenizer.eos_token_id,
                repetition_penalty=1.1,
                no_repeat_ngram_size=4
            )

        # Decode
        generated = self.tokenizer.decode(outputs[0], skip_special_tokens=True)

        # Parse response
        code = ""
        reasoning = ""

        # Extract last instruction's response
        instruction_splits = generated.split("### Instruction:")

        if len(instruction_splits) > 1:
            model_response = instruction_splits[-1]
        else:
            model_response = generated

        # Extract reasoning
        if "### Reasoning:" in model_response:
            reasoning_part = model_response.split("### Reasoning:")[-1]
        elif "###Reasoning:" in model_response:
            reasoning_part = model_response.split("###Reasoning:")[-1]
        else:
            reasoning_part = model_response

        # Extract code
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
            reasoning = reasoning_part.strip()

        # Clean code
        if "```python" in code:
            code = code.split("```python")[1].split("```")[0].strip()
        elif "```" in code:
            code = code.split("```")[1].split("```")[0].strip()

        code = code.replace("###", "").strip()

        # COMPREHENSIVE POST-PROCESSING: Fix ALL possible typos and errors

        # Phase 0: Pre-processing - Aggressive code reconstruction
        # Model fragments code terribly - unite everything first, then rebuild

        # Step 1: Collapse all into single line
        code_single = ' '.join(code.split())

        # Step 2: Insert newlines at strategic points
        # After imports
        code_single = re.sub(r'(\bfrom\s+\S+\s+import\s+[^;]+?)(\s+[a-z])', r'\1\n\2', code_single)
        code_single = re.sub(r'(\bimport\s+[^;]+?)(\s+[a-z])', r'\1\n\2', code_single)

        # After function calls that end with )
        code_single = re.sub(r'(\))\s+([a-z])', r'\1\n\2', code_single)

        # Before print statements
        code_single = re.sub(r'(\S)\s+(print\s*\()', r'\1\n\2', code_single)

        # After closing braces/brackets/parens at statement level
        code_single = re.sub(r'(["\'])\s+([a-z_])', r'\1\n\2', code_single)

        # Step 3: Fix obvious splits in imports
        code_single = re.sub(r'from\s+bioql\s*\.\s+', 'from bioql.', code_single)
        code_single = re.sub(r'from\s+bioql\.(\w+)\s+import\s+', r'from bioql.\1 import ', code_single)

        # Step 4: Fix function names that got split
        code_single = re.sub(r'dock\s+molecules', 'dock_molecules', code_single)
        code_single = re.sub(r'dock\s*_\s*molecules', 'dock_molecules', code_single)

        # Step 5: Fix parameter syntax (remove spaces before =)
        code_single = re.sub(r'(\w+)\s+=\s+', r'\1=', code_single)

        # Step 6: Now format properly with indentation
        lines = code_single.split('\n')
        formatted_lines = []
        indent_level = 0

        for line in lines:
            line = line.strip()
            if not line:
                continue

            # Decrease indent for closing parens
            if line.startswith(')'):
                indent_level = max(0, indent_level - 1)

            # Add line with proper indentation
            formatted_lines.append('    ' * indent_level + line)

            # Increase indent after opening parens or function calls
            if line.endswith('(') or '(' in line and not line.endswith(')'):
                indent_level += 1
            # Decrease indent after closing parens
            elif line.endswith(')') and '(' not in line:
                indent_level = max(0, indent_level - 1)

        code = '\n'.join(formatted_lines)

        # Phase 1: Module and import corrections
        import_corrections = {
            # Docking module typos
            "from bioql.Dicking": "from bioql.docking",
            "from bioql.dkocking": "from bioql.docking",
            "from bioql.dokcing": "from bioql.docking",
            "from bioql.dcking": "from bioql.docking",
            "from bioql.docking.": "from bioql.docking",
            "from bioql.Docker": "from bioql.docking",
            "from bioql.dock": "from bioql.docking",
            "from bioql. docking": "from bioql.docking",

            # Quantum module typos
            "from bioql.quantm": "from bioql",
            "from bioql.quntum": "from bioql",
            "from bioql.quatum": "from bioql",

            # Chemistry module typos
            "from bioql.chem.geomety": "from bioql.chem.geometry",
            "from bioql.chem.geomtry": "from bioql.chem.geometry",

            # Visualization typos
            "from bioql.visualze": "from bioql.visualize",
            "from bioql.vizualize": "from bioql.visualize",
            "from bioql.visual": "from bioql.visualize",
        }

        for typo, correction in import_corrections.items():
            code = code.replace(typo, correction)

        # Phase 2: Function name corrections (CRITICAL)
        function_corrections = {
            # Docking functions - ALL variations
            "dock molecules": "dock_molecules",
            "dock_moleculs": "dock_molecules",
            "dkock_moleculs": "dock_molecules",
            "dock_moelcules": "dock_molecules",
            "dock moleculs": "dock_molecules",
            "dockmolecules": "dock_molecules",
            "dock-molecules": "dock_molecules",
            "docking_molecules": "dock_molecules",
            "dock molecule": "dock_molecules",
            "dockmolecule": "dock_molecules",

            # Quantum functions
            "quantm(": "quantum(",
            "quntum(": "quantum(",
            "quatum(": "quantum(",

            # Visualization functions
            "visualze_3d": "visualize_3d",
            "vizualize_3d": "visualize_3d",
            "visual_3d": "visualize_3d",
            "visualize3d": "visualize_3d",
            "visualize_3D": "visualize_3d",
        }

        for typo, correction in function_corrections.items():
            code = code.replace(typo, correction)

        # Phase 3: Parameter name corrections
        parameter_corrections = {
            # Docking parameters
            "num modes": "num_modes",
            "nummodes": "num_modes",
            "num-modes": "num_modes",
            "number_modes": "num_modes",
            "n_modes": "num_modes",

            "exhaustivness": "exhaustiveness",
            "exhaust": "exhaustiveness",
            "exahustiveness": "exhaustiveness",

            "targer": "target",
            "targe": "target",
            "traget": "target",
            "tagret": "target",

            "lignd": "ligand",
            "lignad": "ligand",
            "ligan": "ligand",

            # Quantum parameters
            "beckend": "backend",
            "backen": "backend",
            "backnd": "backend",

            "shot": "shots",
            "shos": "shots",
        }

        for typo, correction in parameter_corrections.items():
            code = code.replace(typo, correction)

        # Phase 4: Python syntax fixes (spaces, operators, brackets)
        # Fix spacing around operators and delimiters
        syntax_patterns = [
            # Fix spacing around = in assignments and parameters
            (r' = ', '='),
            (r'= ', '='),
            (r' =', '='),

            # Fix spacing around parentheses
            (r'\( ', '('),
            (r' \)', ')'),

            # Fix spacing around brackets
            (r'\[ ', '['),
            (r' \]', ']'),

            # Fix spacing around braces
            (r'\{ ', '{'),
            (r' \}', '}'),

            # Fix spacing around commas
            (r' ,', ','),
            (r',([^\s])', r', \1'),  # Add space after comma if missing

            # Fix spacing around colons in dicts
            (r' :', ':'),
            (r':([^\s])', r': \1'),  # Add space after colon if missing
        ]

        for pattern, replacement in syntax_patterns:
            code = re.sub(pattern, replacement, code)

        # Phase 5: Fix common Python syntax errors

        # Fix missing colons in function definitions
        if 'def ' in code and ':' not in code.split('def ')[1].split('\n')[0]:
            lines = code.split('\n')
            for i, line in enumerate(lines):
                if line.strip().startswith('def ') and not line.rstrip().endswith(':'):
                    lines[i] = line.rstrip() + ':'
            code = '\n'.join(lines)

        # Fix parameter assignment syntax (add = between param and value)
        # Pattern: ligand "aspirin" -> ligand="aspirin"
        param_patterns = [
            (r'ligand\s+"', 'ligand="'),
            (r'ligand\s+\'', "ligand='"),
            (r'target\s+"', 'target="'),
            (r'target\s+\'', "target='"),
            (r'exhaustiveness\s+(\d+)', r'exhaustiveness=\1'),
            (r'num_modes\s+(\d+)', r'num_modes=\1'),
            (r'shots\s+(\d+)', r'shots=\1'),
            (r'backend\s+"', 'backend="'),
            (r'backend\s+\'', "backend='"),
        ]

        for pattern, replacement in param_patterns:
            code = re.sub(pattern, replacement, code)

        # Phase 6: Fix common BioQL-specific issues

        # Ensure proper import format
        if 'import dock_molecules' in code:
            code = code.replace('import dock_molecules', 'from bioql.docking import dock_molecules')

        if 'import quantum' in code and 'from bioql' not in code:
            code = code.replace('import quantum', 'from bioql import quantum')

        # Fix print statement f-string issues
        code = code.replace('print(f"', 'print(f"')
        code = code.replace('print (f"', 'print(f"')
        code = code.replace('print( f"', 'print(f"')

        # Phase 7: Remove excessive whitespace and clean up
        lines = code.split('\n')
        cleaned_lines = []
        for line in lines:
            # Remove trailing whitespace
            line = line.rstrip()
            # Skip empty lines at start/end, but keep internal empty lines
            if line or cleaned_lines:
                cleaned_lines.append(line)

        # Remove trailing empty lines
        while cleaned_lines and not cleaned_lines[-1]:
            cleaned_lines.pop()

        code = '\n'.join(cleaned_lines)

        # Phase 8: Validate and fix indentation
        lines = code.split('\n')
        fixed_lines = []
        current_indent = 0

        for line in lines:
            if not line.strip():
                fixed_lines.append('')
                continue

            # Detect indent level changes
            if line.strip().startswith(('def ', 'class ', 'if ', 'for ', 'while ', 'try:', 'except', 'with ')):
                fixed_lines.append('    ' * current_indent + line.strip())
                if line.strip().endswith(':'):
                    current_indent += 1
            elif line.strip() in ('else:', 'elif ', 'finally:', 'except:'):
                current_indent = max(0, current_indent - 1)
                fixed_lines.append('    ' * current_indent + line.strip())
                current_indent += 1
            else:
                # Check if this line should dedent
                if current_indent > 0 and not line.strip().startswith(('return ', 'print(', 'result', '#')):
                    pass
                fixed_lines.append('    ' * current_indent + line.strip())

        code = '\n'.join(fixed_lines)

        # Validate
        is_valid = (
            len(code) > 80 and
            ('from bioql' in code or 'import bioql' in code) and
            code.count('}') < 5
        )

        return {
            'success': is_valid,
            'code': code,
            'reasoning': reasoning,
            'model': 'deepseek-coder-6.7b-bioql-improved',
            'is_valid': is_valid
        }


@app.function(
    volumes={"/billing": billing_volume, "/model": model_volume}
)
@modal.fastapi_endpoint(method="POST")
def improved_agent(request: dict) -> dict:
    """Improved agent endpoint."""
    import sys
    sys.path.insert(0, "/billing")
    from billing_integration import (
        authenticate_api_key,
        check_sufficient_balance,
        log_inference_usage
    )

    # Auth
    api_key = request.get("api_key", "")
    if not api_key:
        return {"error": "API key required"}

    auth_result = authenticate_api_key(api_key)
    if "error" in auth_result:
        return {"error": auth_result["error"]}

    user_id, api_key_id, user_email = auth_result["user_id"], auth_result["api_key_id"], auth_result["email"]

    # Check balance
    balance_check = check_sufficient_balance(user_id)
    if not balance_check["sufficient"]:
        return {"error": balance_check["message"], "balance": balance_check["balance"]}

    user_balance = balance_check["balance"]

    # Get request
    user_request = request.get("request", "")
    if not user_request:
        return {"error": "request is required"}

    # Execute agent
    start_time = time.time()

    try:
        agent = ImprovedBioQLAgent()
        result = agent.generate_code.remote(user_request)

        execution_time = time.time() - start_time

        # Calculate cost
        base_cost = execution_time * 0.0003  # A10G cost per second
        user_cost = base_cost * 1.4  # 40% markup
        profit = user_cost - base_cost

        # Log usage
        log_inference_usage(
            user_id=user_id,
            api_key_id=api_key_id,
            prompt=f"IMPROVED_AGENT: {user_request}",
            code_generated=result.get('code', ''),
            time_seconds=execution_time,
            base_cost=base_cost,
            user_cost=user_cost,
            profit=profit,
            success=result['success'],
            error_message=None
        )

        return {
            **result,
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
            prompt=f"IMPROVED_AGENT: {user_request}",
            code_generated="",
            time_seconds=execution_time,
            base_cost=0.0,
            user_cost=0.0,
            profit=0.0,
            success=False,
            error_message=str(e)
        )

        return {"error": f"Agent failed: {str(e)}"}
