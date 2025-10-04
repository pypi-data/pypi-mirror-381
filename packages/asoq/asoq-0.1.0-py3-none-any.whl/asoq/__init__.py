"""
Asoq: A simple in-memory asynchronous queue.
"""
__version__ = "0.1.0"

# Expose the simplified, singleton-based public API
from .asoq import task, start_worker

