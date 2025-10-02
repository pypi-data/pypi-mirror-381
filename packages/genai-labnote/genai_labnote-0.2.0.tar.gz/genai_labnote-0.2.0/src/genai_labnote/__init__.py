# src/genai_labnote/__init__.py

from .core import ExperimentLogger
from .magic import get_logger as default_logger
from .magic import log_experiment 

def load_ipython_extension(ipython):
    """
    This function is called when the extension is loaded.
    It registers the magic command.
    """
  
    ipython.register_magic_function(log_experiment, 'cell')

__all__ = ['ExperimentLogger', 'default_logger', 'load_ipython_extension']