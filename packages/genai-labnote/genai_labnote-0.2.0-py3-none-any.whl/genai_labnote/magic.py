# src/genai_labnote/magic.py

from IPython import get_ipython
# from IPython.core.magic import register_cell_magic 
from .core import ExperimentLogger

# (The get_logger function remains the same)
_logger_instance = None

def get_logger():
    global _logger_instance
    if _logger_instance is None:
        _logger_instance = ExperimentLogger()
    return _logger_instance

def log_experiment(line, cell):
    """
    Magic command to log the contents of a cell.
    """
    shell = get_ipython()
    if shell is None:
        print("This magic command can only be used in an IPython environment (like Jupyter or Colab).")
        return

    logger = get_logger()
    result = shell.run_cell(cell)
    
    output = str(result.result)
    if result.error_in_exec:
        output += f"\nERROR: {result.error_in_exec}"
    
    logger.log(code=cell, output=output, notes=line)