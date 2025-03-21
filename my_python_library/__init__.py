# File: /my-python-library/my-python-library/my_python_library/__init__.py
from .module import *  # Import all public classes and functions from module.py

__all__ = [name for name in dir() if not name.startswith('_')]  # Expose public API elements