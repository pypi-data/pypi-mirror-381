"""
BioQL VS Code Assistant
========================

Intelligent code assistant for BioQL in VS Code.

Provides:
- Code completion
- Code generation from natural language
- Error detection and fixing
- Documentation generation
- Quantum circuit optimization suggestions
"""

import os
from pathlib import Path
from typing import Optional, Dict, Any, List
import json

try:
    from loguru import logger
except ImportError:
    import logging
    logger = logging.getLogger(__name__)


class BioQLCodeAssistant:
    """
    BioQL intelligent code assistant for VS Code.

    Can run:
    1. Locally (with quantized model on Mac)
    2. Via Modal API (remote GPU)
    3. Via Ollama (local optimized)

    Example:
        >>> assistant = BioQLCodeAssistant(mode="local")
        >>> code = assistant.complete("Create a Bell state")
        >>> print(code)
    """

    def __init__(
        self,
        mode: str = "local",  # "local", "modal", "ollama"
        model_path: Optional[str] = None,
        modal_url: Optional[str] = None
    ):
        """
        Initialize BioQL code assistant.

        Args:
            mode: Running mode ("local", "modal", "ollama")
            model_path: Path to local model (for local mode)
            modal_url: Modal API URL (for modal mode)
        """
        self.mode = mode
        self.model_path = model_path or self._default_model_path()
        self.modal_url = modal_url
        self.model = None

        logger.info(f"BioQLCodeAssistant initialized in {mode} mode")

        if mode == "local":
            self._init_local()
        elif mode == "modal":
            self._init_modal()
        elif mode == "ollama":
            self._init_ollama()

    def _default_model_path(self) -> str:
        """Get default model path."""
        # Use newly trained model from Modal
        bioql_root = Path(__file__).parent.parent.parent
        return str(bioql_root / "models" / "bioql-lora-v1" / "final_model")

    def _init_local(self):
        """Initialize local model with BioQL LoRA v1."""
        try:
            import torch
            from transformers import AutoTokenizer, AutoModelForCausalLM
            from peft import PeftModel

            logger.info("Loading BioQL LoRA v1 (trained on 10K examples, 3 epochs)...")

            # Base model
            base_model = "Qwen/Qwen2.5-7B-Instruct"

            # Load tokenizer
            self.tokenizer = AutoTokenizer.from_pretrained(
                base_model,
                trust_remote_code=True
            )

            # Load base model
            logger.info("Loading base model...")
            model = AutoModelForCausalLM.from_pretrained(
                base_model,
                torch_dtype=torch.float16,
                device_map="auto",
                trust_remote_code=True,
                low_cpu_mem_usage=True
            )

            # Load LoRA adapter (BioQL v1)
            logger.info(f"Loading LoRA adapter from {self.model_path}...")
            self.model = PeftModel.from_pretrained(
                model,
                self.model_path,
                torch_dtype=torch.float16
            )

            logger.info("✅ BioQL LoRA v1 loaded successfully!")

        except Exception as e:
            logger.error(f"Failed to load model: {e}")
            logger.info("Falling back to template mode")
            self.mode = "template"

    def _init_modal(self):
        """Initialize Modal API client."""
        logger.info("Using Modal API for inference")
        # Will use requests to call Modal endpoint

    def _init_ollama(self):
        """Initialize Ollama client."""
        try:
            import requests
            # Check if Ollama is running
            response = requests.get("http://localhost:11434/api/tags")
            if response.status_code == 200:
                logger.info("✅ Connected to Ollama")
            else:
                logger.warning("Ollama not running")
        except Exception as e:
            logger.error(f"Cannot connect to Ollama: {e}")

    def complete(
        self,
        prompt: str,
        max_length: int = 300,
        temperature: float = 0.7
    ) -> str:
        """
        Generate BioQL code from natural language.

        Args:
            prompt: Natural language description
            max_length: Maximum code length
            temperature: Sampling temperature

        Returns:
            Generated BioQL code

        Example:
            >>> assistant = BioQLCodeAssistant()
            >>> code = assistant.complete("Create a Bell state")
        """
        if self.mode == "local":
            return self._complete_local(prompt, max_length, temperature)
        elif self.mode == "modal":
            return self._complete_modal(prompt, max_length, temperature)
        elif self.mode == "ollama":
            return self._complete_ollama(prompt, max_length, temperature)
        else:
            return self._complete_template(prompt)

    def _complete_local(self, prompt: str, max_length: int, temperature: float) -> str:
        """Complete using local model."""
        import torch

        # Format prompt for code generation
        formatted_prompt = f"""Generate BioQL code for the following task:

Task: {prompt}

Code:
"""

        inputs = self.tokenizer(formatted_prompt, return_tensors="pt")

        with torch.no_grad():
            outputs = self.model.generate(
                **inputs,
                max_new_tokens=max_length,
                temperature=temperature,
                do_sample=True,
                pad_token_id=self.tokenizer.eos_token_id
            )

        generated = self.tokenizer.decode(outputs[0], skip_special_tokens=True)

        # Extract only the code part
        if "Code:" in generated:
            code = generated.split("Code:")[-1].strip()
        else:
            code = generated

        return code

    def _complete_modal(self, prompt: str, max_length: int, temperature: float) -> str:
        """Complete using Modal API."""
        import requests

        if not self.modal_url:
            logger.error("Modal URL not configured")
            return self._complete_template(prompt)

        try:
            response = requests.post(
                self.modal_url,
                json={
                    "prompt": prompt,
                    "max_length": max_length,
                    "temperature": temperature
                },
                timeout=30
            )

            if response.status_code == 200:
                return response.json()["code"]
            else:
                logger.error(f"Modal API error: {response.status_code}")
                return self._complete_template(prompt)

        except Exception as e:
            logger.error(f"Error calling Modal API: {e}")
            return self._complete_template(prompt)

    def _complete_ollama(self, prompt: str, max_length: int, temperature: float) -> str:
        """Complete using Ollama."""
        import requests

        try:
            response = requests.post(
                "http://localhost:11434/api/generate",
                json={
                    "model": "bioql",  # Your custom model name
                    "prompt": f"Generate BioQL code: {prompt}",
                    "stream": False
                },
                timeout=30
            )

            if response.status_code == 200:
                return response.json()["response"]
            else:
                return self._complete_template(prompt)

        except Exception as e:
            logger.error(f"Ollama error: {e}")
            return self._complete_template(prompt)

    def _complete_template(self, prompt: str) -> str:
        """Fallback: template-based generation."""
        templates = {
            "bell": '''from bioql import quantum

# Create a Bell state
result = quantum(
    "Create a Bell state",
    api_key="your_api_key",
    backend="simulator",
    shots=1000
)

print(f"Results: {result.counts}")
''',
            "qft": '''from bioql import quantum

# Quantum Fourier Transform
result = quantum(
    "Run QFT on 4 qubits",
    api_key="your_api_key",
    backend="simulator",
    shots=1000
)

print(f"QFT results: {result.counts}")
''',
            "protein": '''from bioql import quantum

# Protein folding simulation
result = quantum(
    "Simulate protein folding",
    api_key="your_api_key",
    backend="simulator",
    shots=1000
)

print(f"Folding: {result.bio_interpretation}")
''',
            "docking": '''from bioql.docking import dock

# Molecular docking between ligand and receptor
result = dock(
    receptor="protein.pdb",  # Path to receptor PDB file
    ligand_smiles="CC(=O)OC1=CC=CC=C1C(=O)O",  # Ligand SMILES
    backend="auto",  # auto, vina, or quantum
    output_dir="docking_results"
)

if result.success:
    print(f"✅ Docking Score: {result.score} kcal/mol")
    print(f"Backend used: {result.backend}")
    print(f"Results saved to: {result.results_json}")
else:
    print(f"❌ Docking failed: {result.error_message}")
''',
            "ibuprofen_cox1": '''from bioql.docking import dock

# Ibuprofen-COX1 docking
# COX1 (Cyclooxygenase-1) - NSAID target enzyme
# Ibuprofen - Common NSAID pain reliever

result = dock(
    receptor="cox1.pdb",  # Download from PDB: 1EQG, 3N8X, or 1Q4G
    ligand_smiles="CC(C)Cc1ccc(cc1)C(C)C(=O)O",  # Ibuprofen SMILES
    backend="auto",  # Automatically selects best available backend
    output_dir="ibuprofen_cox1_docking",
    exhaustiveness=8,  # Search thoroughness
    num_modes=9  # Number of binding poses
)

if result.success:
    print(f"✅ Ibuprofen-COX1 docking successful!")
    print(f"Binding affinity: {result.score} kcal/mol")
    print(f"Backend: {result.backend}")
    print(f"Job ID: {result.job_id}")
    print(f"Results: {result.results_json}")

    if result.poses:
        print(f"\\nFound {len(result.poses)} binding poses")
        for i, pose in enumerate(result.poses[:3], 1):
            print(f"  Pose {i}: {pose.get('score', 'N/A')} kcal/mol")
else:
    print(f"❌ Docking failed: {result.error_message}")
    print("Note: Make sure cox1.pdb exists. Download from RCSB PDB (ID: 1EQG)")
'''
        }

        # Simple keyword matching
        prompt_lower = prompt.lower()

        if "bell" in prompt_lower or "epr" in prompt_lower:
            return templates["bell"]
        elif "qft" in prompt_lower or "fourier" in prompt_lower:
            return templates["qft"]
        elif "protein" in prompt_lower or "fold" in prompt_lower:
            return templates["protein"]
        elif ("ibuprofen" in prompt_lower and "cox" in prompt_lower) or \
             ("ibuprofen" in prompt_lower and "cox1" in prompt_lower):
            return templates["ibuprofen_cox1"]
        elif "dock" in prompt_lower:
            return templates["docking"]
        else:
            return templates["bell"]  # Default

    def fix_code(self, code: str, error: str) -> str:
        """
        Fix BioQL code errors.

        Args:
            code: Broken code
            error: Error message

        Returns:
            Fixed code
        """
        prompt = f"Fix this BioQL code:\n\n{code}\n\nError: {error}\n\nFixed code:"
        return self.complete(prompt)

    def explain_code(self, code: str) -> str:
        """
        Explain what BioQL code does.

        Args:
            code: BioQL code

        Returns:
            Explanation
        """
        prompt = f"Explain this BioQL code:\n\n{code}"
        return self.complete(prompt, max_length=200)

    def optimize_circuit(self, code: str) -> str:
        """
        Suggest optimizations for quantum circuit.

        Args:
            code: BioQL code

        Returns:
            Optimized code
        """
        prompt = f"Optimize this BioQL quantum circuit:\n\n{code}"
        return self.complete(prompt)


# Singleton instance for VS Code extension
_assistant_instance: Optional[BioQLCodeAssistant] = None


def get_assistant(mode: str = "local") -> BioQLCodeAssistant:
    """Get singleton assistant instance."""
    global _assistant_instance

    if _assistant_instance is None:
        _assistant_instance = BioQLCodeAssistant(mode=mode)

    return _assistant_instance


def quick_complete(prompt: str, mode: str = "local") -> str:
    """
    Quick code completion helper.

    Example:
        >>> from bioql.llm.vscode_assistant import quick_complete
        >>> code = quick_complete("Create a Bell state")
        >>> print(code)
    """
    assistant = get_assistant(mode)
    return assistant.complete(prompt)
