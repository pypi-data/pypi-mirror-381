import pytest
from genai_labnote.core import ExperimentLogger
import os
import shutil

# Use a temporary directory for test artifacts
TEST_DIR = "temp_test_dir"

@pytest.fixture
def logger():
    """Fixture to create a logger instance in a temporary directory."""
    os.makedirs(TEST_DIR, exist_ok=True)
    logger_instance = ExperimentLogger(storage_path=TEST_DIR)
    yield logger_instance
    # Teardown: remove the directory after the test
    shutil.rmtree(TEST_DIR)


def test_logger_initialization(logger):
    """Test if the logger and its components are initialized."""
    assert logger is not None
    assert logger.store is not None
    assert logger.summarizer is not None
    assert os.path.exists(TEST_DIR)

def test_log_entry(logger):
    """Test adding a log entry. We mock the summary to avoid model dependency."""
    code = "print('hello')"
    output = "hello"
    
    # Mock the summarizer to prevent actual model call
    logger.summarizer.summarize = lambda code, output: "A test summary."
    
    logger.log(code, output)
    
    # Check if files were created
    assert os.path.exists(os.path.join(TEST_DIR, "lab_notes.jsonl"))
    assert os.path.exists(os.path.join(TEST_DIR, "lab_notes.index"))

    # Check if the log was added
    all_logs = logger.show_all()
    assert len(all_logs) == 1
    assert all_logs.iloc[0]['summary'] == "A test summary."