# src/genai_labnote/__init__.py

from .core import ExperimentLogger
from .magic import get_logger as default_logger
from .magic import log_experiment # We import the plain function

def load_ipython_extension(ipython):
    """
    This function is called when the extension is loaded.
    It registers the magic command.
    """
    # This line is now the ONLY place the registration happens.
    ipython.register_magic_function(log_experiment, 'cell')

__all__ = ['ExperimentLogger', 'default_logger', 'load_ipython_extension']