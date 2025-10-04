"""
BioQL Inference Server - DeepSeek-Coder-1.3B Fine-tuned
========================================================

Uses the fine-tuned DeepSeek-Coder-1.3B model trained specifically on BioQL.
Includes reasoning capabilities and proper BioQL syntax generation.
"""

import modal
import time

# Create volume references
billing_volume = modal.Volume.from_name("bioql-billing-db")
model_volume = modal.Volume.from_name("bioql-deepseek")

# Image with inference dependencies
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

app = modal.App(name="bioql-inference-deepseek", image=image)

# Pricing Configuration
MODAL_A10G_COST_PER_SECOND = 0.000305556  # $1.10/hour
PROFIT_MARGIN = 0.40  # 40% markup
PRICE_PER_SECOND = MODAL_A10G_COST_PER_SECOND * (1 + PROFIT_MARGIN)


@app.cls(
    gpu="A10G",
    volumes={
        "/billing": billing_volume,
        "/model": model_volume
    },
    scaledown_window=300,
)
class BioQLInference:
    """BioQL code generation with fine-tuned DeepSeek model."""

    @modal.enter()
    def load_model(self):
        """Load fine-tuned DeepSeek model on container start."""
        import torch
        from transformers import AutoTokenizer, AutoModelForCausalLM
        from peft import PeftModel

        print("=" * 70)
        print("🔄 Loading fine-tuned DeepSeek-Coder-1.3B...")
        print("=" * 70)

        base_model_name = "deepseek-ai/deepseek-coder-1.3b-instruct"

        # Load tokenizer
        self.tokenizer = AutoTokenizer.from_pretrained(base_model_name)

        # CRITICAL: Set pad token to match training configuration
        if self.tokenizer.pad_token is None:
            self.tokenizer.pad_token = self.tokenizer.eos_token
            print(f"⚙️  Set pad_token = eos_token")

        print(f"✅ Tokenizer loaded")
        print(f"   EOS token: {self.tokenizer.eos_token} (ID: {self.tokenizer.eos_token_id})")
        print(f"   PAD token: {self.tokenizer.pad_token} (ID: {self.tokenizer.pad_token_id})")

        # Load base model
        base_model = AutoModelForCausalLM.from_pretrained(
            base_model_name,
            device_map="auto",
            torch_dtype=torch.bfloat16
        )
        print(f"✅ Base model loaded: {base_model_name}")

        # Load LoRA adapters with error handling
        import os
        if not os.path.exists("/model/final_model"):
            raise FileNotFoundError(
                "❌ /model/final_model not found! "
                "Run training first: modal run training/TRAIN_DEEPSEEK.py"
            )

        # Check for required files (adapter can be .bin or .safetensors)
        if not os.path.exists("/model/final_model/adapter_config.json"):
            raise FileNotFoundError(
                "❌ adapter_config.json not found in /model/final_model\n"
                "Training may have failed. Retrain the model."
            )

        has_adapter = (
            os.path.exists("/model/final_model/adapter_model.bin") or
            os.path.exists("/model/final_model/adapter_model.safetensors")
        )
        if not has_adapter:
            raise FileNotFoundError(
                "❌ No adapter model file found in /model/final_model\n"
                "Expected: adapter_model.bin or adapter_model.safetensors\n"
                "Training may have failed. Retrain the model."
            )

        self.model = PeftModel.from_pretrained(
            base_model,
            "/model/final_model",
            torch_dtype=torch.bfloat16
        )

        # Set model to eval mode
        self.model.eval()

        # Verify LoRA loading
        trainable = sum(p.numel() for p in self.model.parameters() if p.requires_grad)
        total = sum(p.numel() for p in self.model.parameters())
        print(f"✅ LoRA adapters loaded from /model/final_model")
        print(f"   Trainable params: {trainable:,}")
        print(f"   Total params: {total:,}")
        print(f"   Trainable %: {100 * trainable / total:.2f}%")
        print("=" * 70)

    @modal.method()
    def generate(
        self,
        prompt: str,
        max_length: int = 500,  # Increased for more verbose output
        temperature: float = 0.7,
        include_reasoning: bool = True,
        top_p: float = 0.95,  # Nucleus sampling for diversity
        repetition_penalty: float = 1.1  # Avoid repetition
    ) -> dict:
        """Generate BioQL code with reasoning from natural language."""
        import torch

        start_time = time.time()

        # Format prompt with instruction format used in training
        if include_reasoning:
            formatted_prompt = f"""### Instruction:
{prompt}

### Reasoning:
"""
        else:
            formatted_prompt = f"""### Instruction:
{prompt}

### Code:
"""

        inputs = self.tokenizer(formatted_prompt, return_tensors="pt").to(self.model.device)

        generation_start = time.time()
        with torch.no_grad():
            outputs = self.model.generate(
                **inputs,
                max_new_tokens=max_length,
                min_new_tokens=50,  # Force minimum generation
                temperature=temperature,
                top_p=top_p,
                do_sample=True if temperature > 0 else False,
                pad_token_id=self.tokenizer.pad_token_id,  # Use pad_token_id, not eos
                eos_token_id=self.tokenizer.eos_token_id,
                repetition_penalty=repetition_penalty,
                no_repeat_ngram_size=3,  # Avoid repetition
                num_beams=1  # Disable beam search for faster generation
            )
        generation_time = time.time() - generation_start

        generated = self.tokenizer.decode(outputs[0], skip_special_tokens=True)

        # Additional validation
        if not generated or len(generated.strip()) < 10:
            raise ValueError(
                "Model generated empty or very short output. "
                "This suggests the model isn't properly trained or loaded."
            )

        # Debug logging
        print(f"DEBUG - Generated text: {generated[:200]}...")

        # Extract reasoning and code
        reasoning = ""
        code = ""

        if "### Reasoning:" in generated and "### Code:" in generated:
            parts = generated.split("### Reasoning:")
            if len(parts) > 1:
                reasoning_and_code = parts[1]
                if "### Code:" in reasoning_and_code:
                    reasoning_part, code_part = reasoning_and_code.split("### Code:", 1)
                    reasoning = reasoning_part.strip()
                    code = code_part.strip()
        elif "### Code:" in generated:
            code = generated.split("### Code:")[-1].strip()
        else:
            # Fallback: everything after instruction is code
            if "### Instruction:" in generated:
                code = generated.split("### Instruction:")[-1].strip()
            else:
                code = generated.strip()

        total_time = time.time() - start_time

        # Calculate costs
        base_cost = total_time * MODAL_A10G_COST_PER_SECOND
        user_cost = total_time * PRICE_PER_SECOND
        profit = user_cost - base_cost

        return {
            "code": code,
            "reasoning": reasoning,
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


@app.function(volumes={"/billing": billing_volume, "/model": model_volume})
@modal.fastapi_endpoint(method="POST")
def generate_code(request: dict) -> dict:
    """Web endpoint for BioQL code generation with authentication and billing."""
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
    include_reasoning = request.get("include_reasoning", True)

    if not prompt:
        return {"error": "prompt is required"}

    # Generate code
    try:
        inference = BioQLInference()
        result = inference.generate.remote(prompt, max_length, temperature, include_reasoning)

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
            "reasoning": result["reasoning"],
            "prompt": prompt,
            "model": "deepseek-coder-1.3b-bioql-finetuned",
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


@app.cls(
    gpu="A10G",
    volumes={
        "/billing": billing_volume,
        "/model": model_volume
    },
    scaledown_window=300,
)
class BioQLAgent:
    """Agent with tool execution capabilities using the fine-tuned model."""

    @modal.enter()
    def load_model(self):
        """Load the same fine-tuned model."""
        import torch
        from transformers import AutoTokenizer, AutoModelForCausalLM
        from peft import PeftModel

        print("🤖 Loading BioQL Agent with fine-tuned model...")

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

        print("✅ Agent model loaded and ready")

    @modal.method()
    def execute_with_tools(
        self,
        user_request: str,
        workspace_context: dict = None,
        max_iterations: int = 3
    ) -> dict:
        """Execute user request with tool support and multi-turn reasoning."""
        import torch

        workspace_context = workspace_context or {}
        all_actions = []
        context = f"User request: {user_request}\n\n"

        for iteration in range(max_iterations):
            # Build prompt with tool context
            tool_prompt = f"""### Instruction:
You are a coding assistant with access to tools.

{context}

Available tools:
- read_file: Read file content
- write_file: Write to file
- list_files: List directory
- run_python: Execute Python code
- search_code: Search in code

Workspace: {workspace_context.get('workspace', '/workspace')}
Current file: {workspace_context.get('current_file', 'None')}

Respond with tools needed in this format:
TOOL: tool_name
PARAMS: parameters

REASONING: your reasoning
CODE: code if generating

### Response:
"""

            # Call model
            inputs = self.tokenizer(tool_prompt, return_tensors="pt").to(self.model.device)

            with torch.no_grad():
                outputs = self.model.generate(
                    **inputs,
                    max_new_tokens=500,
                    temperature=0.2,
                    top_p=0.95,
                    do_sample=True,
                    pad_token_id=self.tokenizer.pad_token_id,
                    eos_token_id=self.tokenizer.eos_token_id,
                    repetition_penalty=1.1
                )

            response = self.tokenizer.decode(outputs[0], skip_special_tokens=True)

            # Debug: Print model response
            print(f"\n{'='*60}")
            print(f"ITERATION {iteration + 1} - Model Response:")
            print(f"{'='*60}")
            print(response[:500])  # Print first 500 chars
            print(f"{'='*60}\n")

            # Parse and execute tools
            tools = self._parse_tools(response)
            executed_actions = []

            for tool in tools:
                try:
                    result = self._execute_tool(tool['name'], tool['params'], workspace_context)
                    executed_actions.append({
                        'tool': tool['name'],
                        'params': tool['params'],
                        'result': result,
                        'success': True
                    })
                except Exception as e:
                    executed_actions.append({
                        'tool': tool['name'],
                        'params': tool['params'],
                        'error': str(e),
                        'success': False
                    })

            all_actions.extend(executed_actions)

            # Check if complete
            if not tools or "DONE" in response.upper():
                # Extract final reasoning and code
                reasoning = self._extract_section(response, "REASONING")
                code = self._extract_section(response, "CODE")

                return {
                    'success': True,
                    'actions': all_actions,
                    'reasoning': reasoning,
                    'code': code,
                    'iterations': iteration + 1
                }

            # Update context with results
            context += self._format_tool_results(executed_actions)

        return {
            'success': True,
            'actions': all_actions,
            'warning': f'Max iterations ({max_iterations}) reached',
            'iterations': max_iterations
        }

    def _parse_tools(self, response: str) -> list:
        """Extract tool calls from model response - inference-based parsing."""
        import re

        tools = []

        # Try explicit TOOL format first
        pattern = r'TOOL:\s*(\w+)\s+PARAMS:\s*(.+?)(?=TOOL:|REASONING:|CODE:|$)'
        for match in re.finditer(pattern, response, re.DOTALL | re.IGNORECASE):
            tool_name = match.group(1).strip()
            params = match.group(2).strip()
            if tool_name and tool_name != 'tool_name':  # Skip placeholder
                tools.append({'name': tool_name, 'params': params})

        # If no tools found, infer from content
        if not tools:
            # Detect read_file
            if 'read' in response.lower() and 'file' in response.lower():
                file_match = re.search(r'(\w+\.py|\w+/\w+\.py)', response)
                if file_match:
                    tools.append({'name': 'read_file', 'params': file_match.group(1)})

            # Detect list_files
            if 'list' in response.lower() and 'file' in response.lower():
                dir_match = re.search(r'in\s+(\S+)', response)
                params = dir_match.group(1) if dir_match else '.'
                tools.append({'name': 'list_files', 'params': params})

            # Detect run_python (look for code blocks)
            python_code = re.search(r'```python\n(.+?)\n```', response, re.DOTALL)
            if python_code:
                tools.append({'name': 'run_python', 'params': python_code.group(1)})
            elif 'print(' in response:
                # Extract print statement
                print_match = re.search(r'(print\(.+?\))', response)
                if print_match:
                    tools.append({'name': 'run_python', 'params': print_match.group(1)})

            # Detect write_file
            if 'write' in response.lower() or 'create' in response.lower():
                file_match = re.search(r'(\w+\.py)', response)
                if file_match and ('```' in response or 'code' in response.lower()):
                    code_match = re.search(r'```(?:python)?\n(.+?)\n```', response, re.DOTALL)
                    if code_match:
                        tools.append({
                            'name': 'write_file',
                            'params': f"{file_match.group(1)}|{code_match.group(1)}"
                        })

        return tools

    def _execute_tool(self, tool_name: str, params: str, context: dict):
        """Execute a tool in the Modal container."""
        import os
        import subprocess

        workspace = context.get('workspace', '/tmp/workspace')

        if tool_name == 'read_file':
            file_path = os.path.join(workspace, params.strip())
            with open(file_path, 'r') as f:
                return f.read()

        elif tool_name == 'write_file':
            parts = params.split('|', 1)
            if len(parts) < 2:
                raise ValueError("Format: filename|content")

            file_path = os.path.join(workspace, parts[0].strip())
            content = parts[1].strip()

            os.makedirs(os.path.dirname(file_path), exist_ok=True)
            with open(file_path, 'w') as f:
                f.write(content)

            return f"Wrote to {parts[0]}"

        elif tool_name == 'list_files':
            dir_path = os.path.join(workspace, params.strip()) if params.strip() else workspace
            if os.path.exists(dir_path):
                files = os.listdir(dir_path)
                return '\n'.join(files)
            return "Directory not found"

        elif tool_name == 'run_python':
            temp_file = '/tmp/agent_code.py'
            with open(temp_file, 'w') as f:
                f.write(params)

            result = subprocess.run(
                ['python3', temp_file],
                capture_output=True,
                text=True,
                timeout=30
            )

            if result.returncode == 0:
                return result.stdout
            else:
                raise Exception(f"Execution failed: {result.stderr}")

        elif tool_name == 'search_code':
            parts = params.split('|')
            pattern = parts[0].strip()
            search_path = parts[1].strip() if len(parts) > 1 else '.'

            result = subprocess.run(
                ['grep', '-r', '-n', pattern, search_path],
                capture_output=True,
                text=True,
                cwd=workspace
            )

            return result.stdout or "No matches found"

        else:
            raise ValueError(f"Unknown tool: {tool_name}")

    def _extract_section(self, text: str, section: str) -> str:
        """Extract a section from response."""
        import re

        pattern = f"{section}:\\s*(.+?)(?=TOOL:|REASONING:|CODE:|$)"
        match = re.search(pattern, text, re.DOTALL)

        if match:
            return match.group(1).strip()
        return ""

    def _format_tool_results(self, actions: list) -> str:
        """Format tool results for next iteration."""
        result = "\nTool results:\n"
        for action in actions:
            if action['success']:
                result += f"- {action['tool']}: {action['result'][:100]}...\n"
            else:
                result += f"- {action['tool']}: ERROR - {action['error']}\n"
        return result + "\n"


@app.function(volumes={"/billing": billing_volume, "/model": model_volume})
@modal.fastapi_endpoint(method="POST")
def agent_execute(request: dict) -> dict:
    """Web endpoint for agent execution with tools."""
    import sys
    sys.path.insert(0, "/billing")
    from billing_integration import (
        authenticate_api_key,
        check_sufficient_balance,
        log_inference_usage
    )

    # Authenticate
    api_key = request.get("api_key", "")
    if not api_key:
        return {"error": "API key required"}

    auth_result = authenticate_api_key(api_key)
    if "error" in auth_result:
        return {"error": auth_result["error"], "authenticated": False}

    user_id = auth_result["user_id"]
    api_key_id = auth_result["api_key_id"]
    user_email = auth_result["email"]
    user_balance = auth_result["balance"]

    # Estimate cost (agent uses more compute)
    estimated_cost = 10.0 * PRICE_PER_SECOND  # ~10 seconds for agent

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
    user_request = request.get("request", "")
    workspace_context = request.get("workspace_context", {})
    max_iterations = request.get("max_iterations", 3)

    if not user_request:
        return {"error": "request is required"}

    # Execute agent
    start_time = time.time()

    try:
        agent = BioQLAgent()
        result = agent.execute_with_tools.remote(
            user_request,
            workspace_context,
            max_iterations
        )

        execution_time = time.time() - start_time

        # Calculate costs
        base_cost = execution_time * MODAL_A10G_COST_PER_SECOND
        user_cost = execution_time * PRICE_PER_SECOND
        profit = user_cost - base_cost

        # Log usage
        log_inference_usage(
            user_id=user_id,
            api_key_id=api_key_id,
            prompt=f"AGENT: {user_request}",
            code_generated=result.get('code', ''),
            time_seconds=execution_time,
            base_cost=base_cost,
            user_cost=user_cost,
            profit=profit,
            success=result['success'],
            error_message=result.get('warning')
        )

        return {
            "success": result['success'],
            "actions": result['actions'],
            "reasoning": result.get('reasoning', ''),
            "code": result.get('code', ''),
            "iterations": result['iterations'],
            "model": "deepseek-coder-1.3b-bioql-agent",
            "timing": {
                "total_seconds": round(execution_time, 3)
            },
            "cost": {
                "base_cost_usd": round(base_cost, 6),
                "user_cost_usd": round(user_cost, 6),
                "profit_usd": round(profit, 6),
                "profit_margin_percent": PROFIT_MARGIN * 100
            },
            "user": {
                "email": user_email,
                "balance": round(user_balance - user_cost, 6)
            }
        }

    except Exception as e:
        execution_time = time.time() - start_time

        # Log failure
        log_inference_usage(
            user_id=user_id,
            api_key_id=api_key_id,
            prompt=f"AGENT: {user_request}",
            code_generated="",
            time_seconds=execution_time,
            base_cost=0.0,
            user_cost=0.0,
            profit=0.0,
            success=False,
            error_message=str(e)
        )

        return {
            "error": f"Agent execution failed: {str(e)}",
            "authenticated": True
        }
