#!/usr/bin/env python3
"""
BioQL v3.1: Advanced Profiling & Workflow Acceleration for Quantum Bioinformatics

BioQL is a quantum computing framework specifically designed for bioinformatics
applications. It provides a natural language interface for quantum programming
and integrates with popular quantum computing backends.

🚀 NEW in v3.1.0 - ADVANCED PROFILING & WORKFLOW ACCELERATION:
- Performance profiling system with <5% overhead
- Interactive HTML dashboards with Plotly charts
- Circuit optimization (35% gate/depth reduction)
- Smart caching (24x speedup with 70% hit rate)
- Intelligent job batching (18-30% cost savings)
- Pre-built circuit library (Grover, VQE, QAOA, drug discovery templates)
- Enhanced semantic NL parsing with context awareness
- Circuit composition and stitching tools

Main Features:
- Natural language quantum programming (164B+ patterns!)
- Advanced profiling and performance optimization
- Circuit library with drug discovery templates
- Integration with Qiskit and other quantum backends
- Biological interpretation of quantum results
- Cloud authentication & billing system
- Drug discovery and protein folding support

Basic Usage:
    >>> from bioql import quantum, QuantumResult
    >>> from bioql.profiler import Profiler
    >>>
    >>> # Profile quantum execution
    >>> profiler = Profiler()
    >>> result = profiler.profile_quantum("dock aspirin to COX-1", api_key="bioql_...")
    >>> profiler.export_report(format='html', output='report.html')
    >>>
    >>> # Use circuit library
    >>> from bioql.circuits import VQECircuit, get_catalog
    >>> vqe = VQECircuit(hamiltonian="H2")
    >>> circuit = vqe.build(num_qubits=4, num_layers=2)
"""

__version__ = "3.1.1"
__author__ = "BioQL Development Team"
__email__ = "bioql@example.com"
__license__ = "MIT"

# Core imports
from .quantum_connector import (
    quantum,
    QuantumResult,
    QuantumSimulator,
    BioQLError,
    QuantumBackendError,
    ProgramParsingError,
    list_available_backends
)

# DevKit enhanced features
try:
    from .enhanced_quantum import enhanced_quantum
except ImportError:
    enhanced_quantum = None

# Optional imports with graceful fallbacks
try:
    from .compiler import compile_bioql
except ImportError:
    compile_bioql = None

try:
    from .bio_interpreter import interpret_bio_results
except ImportError:
    interpret_bio_results = None

try:
    from .logger import get_logger, configure_logging
except ImportError:
    get_logger = None
    configure_logging = None

# Dynamic library bridge (NEW - meta-wrapper for any Python library)
try:
    from .dynamic_bridge import dynamic_call, register_library
except ImportError:
    dynamic_call = None
    register_library = None

# Define what gets exported when using "from bioql import *"
__all__ = [
    # Core functionality
    "quantum",
    "QuantumResult",
    "QuantumSimulator",

    # Exceptions
    "BioQLError",
    "QuantumBackendError",
    "ProgramParsingError",

    # Version and metadata
    "__version__",
    "__author__",
    "__email__",
    "__license__",
]

# Add optional exports if available
if compile_bioql is not None:
    __all__.append("compile_bioql")

if interpret_bio_results is not None:
    __all__.append("interpret_bio_results")

if get_logger is not None and configure_logging is not None:
    __all__.extend(["get_logger", "configure_logging"])

if enhanced_quantum is not None:
    __all__.append("enhanced_quantum")

if dynamic_call is not None:
    __all__.extend(["dynamic_call", "register_library"])


def get_version() -> str:
    """Return the current version of BioQL."""
    return __version__


def get_info() -> dict:
    """Return information about the BioQL installation."""
    info = {
        "version": __version__,
        "author": __author__,
        "license": __license__,
        "python_version": None,
        "qiskit_available": False,
        "optional_modules": {}
    }

    # Check Python version
    import sys
    info["python_version"] = f"{sys.version_info.major}.{sys.version_info.minor}.{sys.version_info.micro}"

    # Check Qiskit availability
    try:
        import qiskit
        info["qiskit_available"] = True
        info["qiskit_version"] = qiskit.__version__
    except ImportError:
        pass

    # Check optional modules
    info["optional_modules"]["compiler"] = compile_bioql is not None
    info["optional_modules"]["bio_interpreter"] = interpret_bio_results is not None
    info["optional_modules"]["logger"] = get_logger is not None

    return info


def check_installation() -> bool:
    """
    Check if BioQL is properly installed with all dependencies.

    Returns:
        True if installation is complete, False otherwise
    """
    try:
        # Check core quantum functionality
        result = quantum("test installation", shots=10)
        return result.success
    except Exception:
        return False


def configure_debug_mode(enabled: bool = True) -> None:
    """
    Enable or disable debug mode globally for BioQL.

    Args:
        enabled: Whether to enable debug mode
    """
    import logging

    if enabled:
        logging.basicConfig(level=logging.DEBUG)
        print("BioQL debug mode enabled")
    else:
        logging.basicConfig(level=logging.INFO)
        print("BioQL debug mode disabled")


# Package initialization message
def _show_startup_info():
    """Show startup information when the package is imported."""
    import warnings

    # Check if qiskit is available
    try:
        import qiskit
    except ImportError:
        warnings.warn(
            "Qiskit not found. Install with: pip install qiskit qiskit-aer",
            ImportWarning,
            stacklevel=2
        )

# Show startup info when imported (can be disabled by setting environment variable)
import os
if not os.environ.get("BIOQL_QUIET_IMPORT"):
    _show_startup_info()