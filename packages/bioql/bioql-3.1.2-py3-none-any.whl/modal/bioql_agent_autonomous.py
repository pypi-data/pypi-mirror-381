"""
BioQL Autonomous Agent - Agente que ACTÚA sobre código
=======================================================
No solo revisa - modifica, mejora, y aplica fixes automáticamente
"""

import modal
import time

billing_volume = modal.Volume.from_name("bioql-billing-db")
model_volume = modal.Volume.from_name("bioql-deepseek")

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

app = modal.App(name="bioql-agent-autonomous", image=image)

MODAL_A10G_COST_PER_SECOND = 0.000305556
PROFIT_MARGIN = 0.40
PRICE_PER_SECOND = MODAL_A10G_COST_PER_SECOND * (1 + PROFIT_MARGIN)


@app.cls(
    gpu="A10G",
    volumes={"/billing": billing_volume, "/model": model_volume},
    scaledown_window=300,
)
class AutonomousAgent:
    """Agente autónomo que modifica código."""

    @modal.enter()
    def load_model(self):
        import torch
        from transformers import AutoTokenizer, AutoModelForCausalLM
        from peft import PeftModel

        print("🤖 Loading Autonomous BioQL Agent...")

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
        print("✅ Autonomous Agent ready")

    @modal.method()
    def fix_and_apply(self, file_content: str, file_path: str, user_instruction: str = None) -> dict:
        """
        Lee código, encuentra problemas, genera fixes, y retorna código corregido.

        Este es el CORE del agente autónomo.
        """
        import torch
        import re

        print(f"\n{'='*60}")
        print(f"🔧 AUTONOMOUS FIX: {file_path}")
        print(f"{'='*60}\n")

        # Step 1: Analyze code
        print("📊 Step 1: Analyzing code...")
        analysis_prompt = f"""### Instruction:
Analyze this BioQL code and identify ALL issues:

```python
{file_content[:1500]}
```

List issues with line numbers and specific problems.

### Issues:
"""

        inputs = self.tokenizer(analysis_prompt, return_tensors="pt").to(self.model.device)

        with torch.no_grad():
            outputs = self.model.generate(
                **inputs,
                max_new_tokens=400,
                temperature=0.3,
                do_sample=True,
                pad_token_id=self.tokenizer.pad_token_id,
                eos_token_id=self.tokenizer.eos_token_id,
            )

        analysis = self.tokenizer.decode(outputs[0], skip_special_tokens=True)

        # Extract issues
        if "### Issues:" in analysis:
            issues_text = analysis.split("### Issues:")[-1].strip()
        else:
            issues_text = analysis.strip()

        print(f"Found issues:\n{issues_text[:300]}...\n")

        # Step 2: Generate fixed code
        print("🔨 Step 2: Generating fixed code...")

        fix_instruction = user_instruction or "Fix all issues, improve code quality, add error handling"

        fix_prompt = f"""### Instruction:
Fix this BioQL code. Issues found:
{issues_text[:500]}

Original code:
```python
{file_content[:1500]}
```

{fix_instruction}

Generate the COMPLETE fixed code.

### Fixed Code:
```python
"""

        inputs = self.tokenizer(fix_prompt, return_tensors="pt").to(self.model.device)

        with torch.no_grad():
            outputs = self.model.generate(
                **inputs,
                max_new_tokens=800,
                temperature=0.2,  # Lower temp for fixes
                do_sample=True,
                pad_token_id=self.tokenizer.pad_token_id,
                eos_token_id=self.tokenizer.eos_token_id,
            )

        fixed_response = self.tokenizer.decode(outputs[0], skip_special_tokens=True)

        # Extract fixed code
        fixed_code = self._extract_code_block(fixed_response)

        if not fixed_code or len(fixed_code) < 50:
            # Fallback: use everything after "### Fixed Code:"
            if "### Fixed Code:" in fixed_response:
                fixed_code = fixed_response.split("### Fixed Code:")[-1].strip()
                fixed_code = fixed_code.replace("```python", "").replace("```", "").strip()

        print(f"Generated {len(fixed_code)} chars of fixed code\n")

        # Step 3: Calculate diff
        print("📝 Step 3: Calculating changes...")
        diff = self._generate_diff(file_content, fixed_code)

        changes_count = len([line for line in diff.split('\n') if line.startswith('+') or line.startswith('-')])
        print(f"Changes: {changes_count} lines modified\n")

        return {
            'success': True,
            'action': 'fix_and_apply',
            'file_path': file_path,
            'original_code': file_content,
            'fixed_code': fixed_code,
            'issues_found': issues_text,
            'diff': diff,
            'changes_count': changes_count,
            'applied': False,  # VSCode will apply
            'reasoning': f'Analyzed {len(file_content)} chars, generated {len(fixed_code)} chars of fixes'
        }

    @modal.method()
    def improve_code(self, file_content: str, file_path: str, focus: str = "quality") -> dict:
        """Mejora código sin cambiar funcionalidad."""
        import torch

        print(f"🎨 IMPROVING CODE: {file_path} (focus: {focus})")

        prompt = f"""### Instruction:
Improve this BioQL code focusing on {focus}:
- Better variable names
- Add docstrings
- Improve structure
- Add type hints
- Better error handling

Original code:
```python
{file_content[:1500]}
```

### Improved Code:
```python
"""

        inputs = self.tokenizer(prompt, return_tensors="pt").to(self.model.device)

        with torch.no_grad():
            outputs = self.model.generate(
                **inputs,
                max_new_tokens=1000,
                temperature=0.3,
                do_sample=True,
                pad_token_id=self.tokenizer.pad_token_id,
                eos_token_id=self.tokenizer.eos_token_id,
            )

        improved = self.tokenizer.decode(outputs[0], skip_special_tokens=True)
        improved_code = self._extract_code_block(improved)

        diff = self._generate_diff(file_content, improved_code)

        return {
            'success': True,
            'action': 'improve_code',
            'file_path': file_path,
            'original_code': file_content,
            'improved_code': improved_code,
            'diff': diff,
            'focus': focus,
            'applied': False
        }

    @modal.method()
    def refactor(self, file_content: str, file_path: str, refactor_type: str = "structure") -> dict:
        """Refactoriza código (estructura, funciones, clases)."""
        import torch

        print(f"♻️  REFACTORING: {file_path} ({refactor_type})")

        refactor_instructions = {
            'structure': 'Break into smaller functions, improve organization',
            'performance': 'Optimize for speed, reduce API calls, use batch operations',
            'readability': 'Simplify logic, add comments, improve naming',
            'security': 'Remove hardcoded secrets, add validation, improve error handling'
        }

        instruction = refactor_instructions.get(refactor_type, refactor_type)

        prompt = f"""### Instruction:
Refactor this BioQL code: {instruction}

Original code:
```python
{file_content[:1500]}
```

### Refactored Code:
```python
"""

        inputs = self.tokenizer(prompt, return_tensors="pt").to(self.model.device)

        with torch.no_grad():
            outputs = self.model.generate(
                **inputs,
                max_new_tokens=1000,
                temperature=0.2,
                do_sample=True,
                pad_token_id=self.tokenizer.pad_token_id,
                eos_token_id=self.tokenizer.eos_token_id,
            )

        refactored = self.tokenizer.decode(outputs[0], skip_special_tokens=True)
        refactored_code = self._extract_code_block(refactored)

        diff = self._generate_diff(file_content, refactored_code)

        return {
            'success': True,
            'action': 'refactor',
            'file_path': file_path,
            'original_code': file_content,
            'refactored_code': refactored_code,
            'diff': diff,
            'refactor_type': refactor_type,
            'applied': False
        }

    def _extract_code_block(self, text: str) -> str:
        """Extrae bloque de código de la respuesta."""
        import re

        # Try to find code block
        code_match = re.search(r'```python\n(.+?)\n```', text, re.DOTALL)
        if code_match:
            return code_match.group(1).strip()

        # Try to find code after marker
        if '### Fixed Code:' in text or '### Improved Code:' in text or '### Refactored Code:' in text:
            for marker in ['### Fixed Code:', '### Improved Code:', '### Refactored Code:']:
                if marker in text:
                    code = text.split(marker)[-1]
                    code = code.replace('```python', '').replace('```', '').strip()
                    return code

        # Fallback: return cleaned text
        return text.replace('```python', '').replace('```', '').strip()

    def _generate_diff(self, original: str, modified: str) -> str:
        """Genera diff simple entre original y modificado."""
        orig_lines = original.split('\n')
        mod_lines = modified.split('\n')

        diff = []
        diff.append(f"--- original")
        diff.append(f"+++ modified")
        diff.append(f"@@ Lines: {len(orig_lines)} -> {len(mod_lines)} @@")

        # Simple line-by-line diff
        max_len = max(len(orig_lines), len(mod_lines))

        for i in range(min(max_len, 50)):  # Limit to 50 lines
            if i < len(orig_lines) and i < len(mod_lines):
                if orig_lines[i] != mod_lines[i]:
                    diff.append(f"- {orig_lines[i]}")
                    diff.append(f"+ {mod_lines[i]}")
            elif i < len(orig_lines):
                diff.append(f"- {orig_lines[i]}")
            elif i < len(mod_lines):
                diff.append(f"+ {mod_lines[i]}")

        return '\n'.join(diff)


@app.function(volumes={"/billing": billing_volume, "/model": model_volume})
@modal.fastapi_endpoint(method="POST")
def agent_act(request: dict) -> dict:
    """Endpoint para agente autónomo."""
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

    user_id = auth_result["user_id"]
    api_key_id = auth_result["api_key_id"]
    user_email = auth_result["email"]
    user_balance = auth_result["balance"]

    # Check balance
    estimated_cost = 15.0 * PRICE_PER_SECOND  # Agent uses more compute
    has_balance, balance_msg = check_sufficient_balance(user_id, estimated_cost)
    if not has_balance:
        return {"error": balance_msg, "balance": user_balance}

    # Extract params
    action_type = request.get("action", "fix_and_apply")
    file_content = request.get("file_content", "")
    file_path = request.get("file_path", "")
    user_instruction = request.get("instruction")
    focus = request.get("focus", "quality")
    refactor_type = request.get("refactor_type", "structure")

    if not file_content:
        return {"error": "file_content is required"}

    # Execute
    start_time = time.time()

    try:
        agent = AutonomousAgent()

        if action_type == "fix_and_apply":
            result = agent.fix_and_apply.remote(file_content, file_path, user_instruction)
        elif action_type == "improve":
            result = agent.improve_code.remote(file_content, file_path, focus)
        elif action_type == "refactor":
            result = agent.refactor.remote(file_content, file_path, refactor_type)
        else:
            return {"error": f"Unknown action: {action_type}"}

        execution_time = time.time() - start_time

        # Calculate costs
        base_cost = execution_time * MODAL_A10G_COST_PER_SECOND
        user_cost = execution_time * PRICE_PER_SECOND
        profit = user_cost - base_cost

        # Log
        log_inference_usage(
            user_id=user_id,
            api_key_id=api_key_id,
            prompt=f"AUTONOMOUS_AGENT: {action_type} on {file_path}",
            code_generated=result.get('fixed_code', result.get('improved_code', result.get('refactored_code', ''))),
            time_seconds=execution_time,
            base_cost=base_cost,
            user_cost=user_cost,
            profit=profit,
            success=result['success'],
            error_message=None
        )

        return {
            **result,
            "model": "bioql-autonomous-agent",
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
            prompt=f"AUTONOMOUS_AGENT: {action_type}",
            code_generated="",
            time_seconds=execution_time,
            base_cost=0.0,
            user_cost=0.0,
            profit=0.0,
            success=False,
            error_message=str(e)
        )

        return {"error": f"Agent failed: {str(e)}"}
