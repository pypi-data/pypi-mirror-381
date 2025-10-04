"""
BioQL Code Templates
====================

Template-based code generation for common BioQL patterns.
Falls back to CodeLlama for complex requests.
"""

BIOQL_TEMPLATES = {
    # Bell state templates
    "bell": """from bioql import quantum

# Create Bell state
result = quantum("Create Bell state on 2 qubits", backend="simulator", shots=1000)
print(result)
""",

    # GHZ state templates
    "ghz": """from bioql import quantum

# Create {n}-qubit GHZ state
result = quantum("Create {n}-qubit GHZ state", backend="simulator", shots=1000)
print(result)
""",

    # QFT templates
    "qft": """from bioql import quantum

# Run Quantum Fourier Transform
result = quantum("Run QFT on {n} qubits and measure", backend="simulator", shots=1000)
print(result)
""",

    # Grover templates
    "grover": """from bioql import quantum

# Run Grover's algorithm
result = quantum("Run Grover search on {n} qubits", backend="simulator", shots=1000)
print(result)
""",

    # Measurement templates
    "measure": """from bioql import quantum

# Create and measure quantum state
result = quantum("{description}", backend="simulator", shots=1000)
print(result)
""",

    # IBM Quantum execution
    "ibm": """from bioql import quantum

# Run on IBM Quantum hardware
result = quantum("{description}", backend="ibm_quantum", api_key="your_api_key")
print(result)
""",

    # IonQ execution
    "ionq": """from bioql import quantum

# Run on IonQ hardware
result = quantum("{description}", backend="ionq", api_key="your_api_key")
print(result)
""",
}


def match_template(prompt):
    """
    Match user prompt to a BioQL template.

    Returns: (template_code, confidence) or (None, 0.0)
    """
    prompt_lower = prompt.lower()

    # Bell state patterns
    if any(word in prompt_lower for word in ["bell", "entangle", "epr"]):
        return BIOQL_TEMPLATES["bell"], 0.9

    # GHZ state patterns
    if "ghz" in prompt_lower:
        # Extract number of qubits
        import re
        match = re.search(r'(\d+)\s*qubit', prompt_lower)
        n = match.group(1) if match else "3"
        return BIOQL_TEMPLATES["ghz"].format(n=n), 0.9

    # QFT patterns
    if any(word in prompt_lower for word in ["qft", "fourier", "quantum fourier"]):
        import re
        match = re.search(r'(\d+)\s*qubit', prompt_lower)
        n = match.group(1) if match else "4"
        return BIOQL_TEMPLATES["qft"].format(n=n), 0.9

    # Grover patterns
    if "grover" in prompt_lower:
        import re
        match = re.search(r'(\d+)\s*qubit', prompt_lower)
        n = match.group(1) if match else "3"
        return BIOQL_TEMPLATES["grover"].format(n=n), 0.85

    # IBM Quantum execution
    if "ibm" in prompt_lower or "real hardware" in prompt_lower:
        return BIOQL_TEMPLATES["ibm"].format(description=prompt), 0.8

    # IonQ execution
    if "ionq" in prompt_lower:
        return BIOQL_TEMPLATES["ionq"].format(description=prompt), 0.8

    # Generic measurement
    if any(word in prompt_lower for word in ["measure", "run", "execute", "simulate"]):
        return BIOQL_TEMPLATES["measure"].format(description=prompt), 0.7

    # No template match
    return None, 0.0


def generate_bioql_code(prompt, use_templates=True, confidence_threshold=0.7):
    """
    Generate BioQL code from prompt.

    Args:
        prompt: Natural language description
        use_templates: Whether to use template matching
        confidence_threshold: Minimum confidence to use template

    Returns:
        (code, method) where method is "template" or "model"
    """
    if use_templates:
        template_code, confidence = match_template(prompt)

        if template_code and confidence >= confidence_threshold:
            return template_code.strip(), "template"

    # Fall back to model
    return None, "model"
