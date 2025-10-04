"""
BioQL DeepSeek-Coder-1.3B Training
===================================

Fast training of a small but powerful code model specialized in BioQL.

Model: deepseek-ai/deepseek-coder-1.3b-instruct
Size: 1.3B parameters (10x smaller than Qwen)
Training time: ~30 minutes on A100
Quality: Excellent for code generation with reasoning
"""

import modal
import time
from datetime import datetime

# Create volume for storing model
volume = modal.Volume.from_name("bioql-deepseek", create_if_missing=True)

# Training image with all dependencies
image = (
    modal.Image.debian_slim(python_version="3.11")
    .pip_install(
        "torch==2.1.0",
        "transformers==4.37.0",
        "peft==0.7.0",
        "datasets==2.16.0",
        "accelerate==0.25.0",
        "bitsandbytes==0.41.3",
        "scipy==1.11.4",
    )
)

app = modal.App(name="bioql-train-deepseek", image=image)


def generate_bioql_dataset(num_examples=10000):
    """
    Generate high-quality BioQL training examples with reasoning.

    Format:
    {
        "instruction": "User request",
        "reasoning": "Step-by-step thought process",
        "code": "BioQL code"
    }
    """
    examples = []

    # Template categories
    categories = {
        "bell_state": [
            {
                "instruction": "Create a Bell state using BioQL",
                "reasoning": "A Bell state is a maximally entangled 2-qubit state. Steps: 1) Apply Hadamard to qubit 0 to create superposition, 2) Apply CNOT with qubit 0 as control and qubit 1 as target to create entanglement.",
                "code": 'from bioql import quantum\n\nresult = quantum("Create Bell state on 2 qubits", backend="simulator", shots=1000)\nprint(result)'
            },
            {
                "instruction": "Generate an EPR pair with BioQL",
                "reasoning": "An EPR pair is another name for a Bell state. We need to create maximum entanglement between 2 qubits using H and CNOT gates.",
                "code": 'from bioql import quantum\n\n# Create EPR pair (Bell state)\nresult = quantum("Create Bell state", backend="simulator", shots=1024)\nprint("EPR pair results:", result)'
            },
            {
                "instruction": "Make two qubits maximally entangled",
                "reasoning": "Maximum entanglement means creating a Bell state. This requires applying H gate to first qubit, then CNOT between the qubits.",
                "code": 'from bioql import quantum\n\nresult = quantum("Create Bell state on 2 qubits", shots=1000)\nprint(result)'
            },
        ],

        "ghz_state": [
            {
                "instruction": "Create a 3-qubit GHZ state using BioQL",
                "reasoning": "GHZ state is a multi-qubit entangled state. Steps: 1) Apply H to first qubit, 2) Apply CNOT from qubit 0 to qubit 1, 3) Apply CNOT from qubit 0 to qubit 2.",
                "code": 'from bioql import quantum\n\nresult = quantum("Create 3-qubit GHZ state", backend="simulator", shots=1000)\nprint(result)'
            },
            {
                "instruction": "Generate a 4-qubit GHZ state",
                "reasoning": "For a 4-qubit GHZ state, we start with H on qubit 0, then cascade CNOT gates from qubit 0 to all other qubits to create full entanglement.",
                "code": 'from bioql import quantum\n\nresult = quantum("Create 4-qubit GHZ state", shots=2000)\nprint("GHZ state:", result)'
            },
        ],

        "qft": [
            {
                "instruction": "Run Quantum Fourier Transform on 3 qubits",
                "reasoning": "QFT is the quantum version of the discrete Fourier transform. For 3 qubits, we apply controlled rotation gates and Hadamards in a specific pattern, followed by swaps.",
                "code": 'from bioql import quantum\n\nresult = quantum("Run QFT on 3 qubits and measure", backend="simulator", shots=1000)\nprint(result)'
            },
            {
                "instruction": "Apply QFT to 4 qubits and measure",
                "reasoning": "QFT transforms computational basis to frequency basis. We need to apply it to all 4 qubits then measure to see the transformed state.",
                "code": 'from bioql import quantum\n\nresult = quantum("Run QFT on 4 qubits and measure", shots=1024)\nprint("QFT result:", result)'
            },
        ],

        "grover": [
            {
                "instruction": "Run Grover's search algorithm",
                "reasoning": "Grover's algorithm provides quadratic speedup for unstructured search. Steps: 1) Initialize superposition, 2) Apply oracle, 3) Apply diffusion operator, 4) Repeat optimal number of iterations.",
                "code": 'from bioql import quantum\n\nresult = quantum("Run Grover search on 3 qubits", backend="simulator", shots=1000)\nprint(result)'
            },
        ],

        "superposition": [
            {
                "instruction": "Create superposition on 2 qubits",
                "reasoning": "Superposition means equal probability of all states. Apply Hadamard gate to each qubit to create uniform superposition of all 4 basis states.",
                "code": 'from bioql import quantum\n\nresult = quantum("Create superposition on 2 qubits", shots=1000)\nprint(result)'
            },
        ],

        "hardware": [
            {
                "instruction": "Run on IBM quantum hardware",
                "reasoning": "To execute on real IBM quantum computer, we need to specify backend='ibm_quantum' and provide API key for authentication.",
                "code": 'from bioql import quantum\n\nresult = quantum("Create Bell state", backend="ibm_quantum", api_key="your_api_key")\nprint(result)'
            },
            {
                "instruction": "Execute on IonQ",
                "reasoning": "IonQ uses trapped ion technology. We specify backend='ionq' and provide API credentials.",
                "code": 'from bioql import quantum\n\nresult = quantum("Run QFT on 3 qubits", backend="ionq", api_key="your_key")\nprint(result)'
            },
        ],

        "measurement": [
            {
                "instruction": "Create Bell state and measure both qubits",
                "reasoning": "After creating Bell state, measurement will show correlations - if qubit 0 is |0⟩, qubit 1 is |0⟩, and vice versa.",
                "code": 'from bioql import quantum\n\nresult = quantum("Create Bell state and measure", backend="simulator", shots=1024)\nprint(result)'
            },
        ],

        "correct_syntax": [
            {
                "instruction": "Run QFT on 4 qubits",
                "reasoning": "QFT transforms computational basis to frequency basis. The syntax is: quantum(description, backend, shots). NEVER use quantum(gate_name, num_qubits) - that's incorrect!",
                "code": 'from bioql import quantum\n\n# CORRECT syntax:\nresult = quantum("Run QFT on 4 qubits and measure", backend="simulator", shots=1000)\nprint(result)\n\n# WRONG: quantum("QFT", 4)  # This is INCORRECT!'
            },
            {
                "instruction": "Apply Hadamard gate to first qubit",
                "reasoning": "To apply a single gate, describe it in natural language. NEVER use quantum(gate, qubit_number) format.",
                "code": 'from bioql import quantum\n\n# CORRECT:\nresult = quantum("Apply Hadamard to qubit 0", backend="simulator", shots=1000)\nprint(result)'
            },
            {
                "instruction": "Create entanglement between 2 qubits",
                "reasoning": "Entanglement is created with Bell state. Use natural language description, not gate names as function arguments.",
                "code": 'from bioql import quantum\n\n# CORRECT:\nresult = quantum("Create Bell state on 2 qubits", backend="simulator", shots=1000)\nprint(result)\n\n# WRONG examples (DO NOT USE):\n# quantum("Bell", 2)  # INCORRECT!\n# quantum("CNOT", (0, 1))  # INCORRECT!'
            },
            {
                "instruction": "Simulate quantum circuit with superposition",
                "reasoning": "BioQL uses natural language descriptions. The function signature is always: quantum(description_string, backend=..., shots=...)",
                "code": 'from bioql import quantum\n\n# CORRECT:\nresult = quantum("Create superposition on 3 qubits and measure", backend="simulator", shots=1024)\nprint(result)'
            },
        ],

        "docking": [
            {
                "instruction": "Dock ibuprofen to COX-2 protein",
                "reasoning": "Molecular docking uses the dock() function with natural language description, SMILES string, and PDB code.",
                "code": 'from bioql.docking import dock\n\nresult = dock(\n    "dock ibuprofen to COX-2 protein and calculate binding affinity",\n    ligand_smiles="CC(C)Cc1ccc(cc1)[C@@H](C)C(=O)O",\n    protein_pdb="1CX2",\n    backend="simulator",\n    shots=1000\n)\nprint("Binding affinity:", result.score)'
            },
        ],

        "multi_step": [
            {
                "instruction": "Create Bell state, then measure in X basis",
                "reasoning": "For multi-step operations, describe the full sequence in natural language.",
                "code": 'from bioql import quantum\n\nresult = quantum(\n    "Create Bell state on qubits 0 and 1, then measure both qubits in X basis",\n    backend="simulator",\n    shots=1000\n)\nprint(result)'
            },
        ],
    }

    # Generate variations
    for category, base_examples in categories.items():
        for base in base_examples:
            # Add base example
            examples.append(base)

            # Generate variations
            variations = [
                base,  # Original
                {**base, "instruction": base["instruction"].lower()},  # lowercase
                {**base, "instruction": base["instruction"].replace("BioQL", "bioql")},
            ]

            examples.extend(variations[:2])  # Add 2 variations per base

    # Duplicate to reach target size
    while len(examples) < num_examples:
        examples.extend(examples[:min(100, num_examples - len(examples))])

    return examples[:num_examples]


@app.function(
    gpu="A100",  # Fast GPU for quick training
    volumes={"/data": volume},
    timeout=3600,  # 1 hour timeout
)
def train():
    """Train DeepSeek-Coder-1.3B on BioQL examples."""
    import torch
    from transformers import AutoTokenizer, AutoModelForCausalLM, TrainingArguments, Trainer
    from peft import LoraConfig, get_peft_model, TaskType
    from datasets import Dataset

    print("=" * 70)
    print("🚀 BioQL DeepSeek-Coder-1.3B Training")
    print("=" * 70)

    # Delete old model if exists (for retraining)
    import os
    import shutil
    if os.path.exists("/data/final_model"):
        print("\n⚠️  Found existing model at /data/final_model")
        print("Deleting old model for retraining...")
        shutil.rmtree("/data/final_model")
        print("✅ Old model deleted")

    # [1/5] Generate dataset
    print("\n[1/5] Generating BioQL training dataset...")
    examples = generate_bioql_dataset(num_examples=10000)
    print(f"   ✅ Generated {len(examples)} training examples")

    # [2/5] Load model
    print("\n[2/5] Loading DeepSeek-Coder-1.3B-Instruct...")
    model_name = "deepseek-ai/deepseek-coder-1.3b-instruct"

    tokenizer = AutoTokenizer.from_pretrained(model_name, trust_remote_code=True)
    tokenizer.pad_token = tokenizer.eos_token

    model = AutoModelForCausalLM.from_pretrained(
        model_name,
        device_map="auto",
        torch_dtype=torch.bfloat16,
        trust_remote_code=True
    )
    print("   ✅ Model loaded (1.3B parameters)")

    # [3/5] Add LoRA adapters
    print("\n[3/5] Adding LoRA adapters...")
    lora_config = LoraConfig(
        task_type=TaskType.CAUSAL_LM,
        r=16,  # LoRA rank
        lora_alpha=32,
        lora_dropout=0.05,
        target_modules=["q_proj", "k_proj", "v_proj", "o_proj"],
        bias="none"
    )

    model = get_peft_model(model, lora_config)
    trainable = sum(p.numel() for p in model.parameters() if p.requires_grad)
    total = sum(p.numel() for p in model.parameters())
    print(f"   ✅ LoRA ready - Trainable: {trainable:,} / {total:,} params")

    # [4/5] Prepare dataset
    print("\n[4/5] Tokenizing dataset...")

    def format_example(ex):
        """Format example with instruction and response separated."""
        instruction_text = f"""### Instruction:
{ex['instruction']}

### Reasoning:"""

        response_text = f"""{ex['reasoning']}

### Code:
{ex['code']}"""

        return {
            "instruction": instruction_text,
            "response": response_text
        }

    formatted = [format_example(ex) for ex in examples]
    dataset = Dataset.from_list(formatted)

    def tokenize(example):
        """Tokenize with labels only for the response part."""
        # Tokenize instruction
        instruction_tokens = tokenizer(
            example["instruction"],
            truncation=False,
            add_special_tokens=True
        )

        # Tokenize response
        response_tokens = tokenizer(
            example["response"],
            truncation=False,
            add_special_tokens=False
        )

        # Combine input_ids
        input_ids = instruction_tokens["input_ids"] + response_tokens["input_ids"]

        # Create labels: -100 for instruction (ignored), actual tokens for response
        labels = [-100] * len(instruction_tokens["input_ids"]) + response_tokens["input_ids"]

        # Truncate to max_length
        max_length = 512
        if len(input_ids) > max_length:
            input_ids = input_ids[:max_length]
            labels = labels[:max_length]
        else:
            # Pad to max_length
            padding_length = max_length - len(input_ids)
            input_ids = input_ids + [tokenizer.pad_token_id] * padding_length
            labels = labels + [-100] * padding_length

        attention_mask = [1 if token_id != tokenizer.pad_token_id else 0 for token_id in input_ids]

        return {
            "input_ids": input_ids,
            "attention_mask": attention_mask,
            "labels": labels
        }

    dataset = dataset.map(tokenize, remove_columns=["instruction", "response"])
    print(f"   ✅ Dataset tokenized: {len(dataset)} examples")
    print(f"   📋 Training: Model will learn to generate Reasoning + Code from Instruction")

    # [5/5] Train
    print("\n[5/5] Training (30 minutes on A100)...")

    training_args = TrainingArguments(
        output_dir="/data/checkpoints",
        num_train_epochs=3,
        per_device_train_batch_size=8,
        gradient_accumulation_steps=4,
        learning_rate=2e-4,
        warmup_steps=100,
        logging_steps=10,
        save_steps=200,
        save_total_limit=3,
        bf16=True,
        optim="adamw_torch",
        max_grad_norm=0.3,
        report_to="none",
    )

    trainer = Trainer(
        model=model,
        args=training_args,
        train_dataset=dataset,
    )

    start_time = time.time()
    trainer.train()
    training_time = time.time() - start_time

    print(f"\n✅ Training completed in {training_time/60:.1f} minutes!")

    # Save model
    print("\n💾 Saving final model to /data/final_model...")
    model.save_pretrained("/data/final_model")
    tokenizer.save_pretrained("/data/final_model")

    # Validate saved files
    import os
    print("\n🔍 Validating saved model files...")

    # Check critical files
    required_files = ["adapter_config.json", "tokenizer_config.json"]
    for file in required_files:
        path = f"/data/final_model/{file}"
        if os.path.exists(path):
            size = os.path.getsize(path)
            print(f"   ✅ {file} ({size:,} bytes)")
        else:
            print(f"   ❌ MISSING: {file}")
            raise FileNotFoundError(f"Critical file missing: {file}")

    # Check for adapter model (can be .bin or .safetensors)
    has_adapter = False
    for adapter_file in ["adapter_model.bin", "adapter_model.safetensors"]:
        path = f"/data/final_model/{adapter_file}"
        if os.path.exists(path):
            size = os.path.getsize(path)
            print(f"   ✅ {adapter_file} ({size:,} bytes)")
            has_adapter = True

    if not has_adapter:
        print(f"   ❌ MISSING: adapter_model.bin or adapter_model.safetensors")
        raise FileNotFoundError("No adapter model file found!")

    volume.commit()

    # Test model loading
    print("\n🧪 Testing model can be loaded...")
    try:
        from peft import PeftModel
        test_base = AutoModelForCausalLM.from_pretrained(
            model_name,
            device_map="auto",
            torch_dtype=torch.bfloat16,
            trust_remote_code=True
        )
        test_model = PeftModel.from_pretrained(test_base, "/data/final_model")
        print("   ✅ Model loads successfully!")
        del test_model, test_base
        torch.cuda.empty_cache()
    except Exception as e:
        print(f"   ❌ Model loading test failed: {e}")
        raise

    print("\n" + "=" * 70)
    print("✅ TRAINING COMPLETED SUCCESSFULLY!")
    print("=" * 70)
    print(f"Training time: {training_time/60:.1f} minutes")
    print(f"Model saved to: /data/final_model")
    print(f"LoRA adapters: {trainable:,} trainable parameters")
    print("\n📋 Next steps:")
    print("   1. Deploy inference: modal deploy modal/bioql_inference_deepseek.py")
    print("   2. Test endpoint with: curl -X POST https://... -d @test.json")
    print("=" * 70)


@app.local_entrypoint()
def main():
    """Start training."""
    print("\n🚀 Starting BioQL DeepSeek training...")
    print("Expected time: ~30 minutes on A100\n")

    train.remote()

    print("\n✅ Training job submitted!")
    print("Monitor progress at: https://modal.com/apps")
