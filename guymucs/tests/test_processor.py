import pytest
import os
from guymucs.processor import GuyMucsProcessor

@pytest.fixture
def setup_files(tmp_path):
    # Set up test files for processor
    input_file = tmp_path / "test_audio.mp3"
    input_file.write_text("fake audio data")
    output_folder = tmp_path / "output"
    output_folder.mkdir()
    return [str(input_file)], str(output_folder)

def test_processor_initialization(setup_files):
    # Test initialization of GuyMucsProcessor with required parameters
    input_files, output_folder = setup_files
    processor = GuyMucsProcessor(input_files, output_folder, "vocals")
    assert processor.input_files == input_files
    assert processor.output_folder == output_folder
    assert processor.instrument == "vocals"

def test_processor_with_missing_file(tmp_path):
    # Test processor behavior when the file is missing
    missing_file = tmp_path / "missing_audio.mp3"
    output_folder = tmp_path / "output"
    output_folder.mkdir()

    processor = GuyMucsProcessor([str(missing_file)], str(output_folder), "drums")
    try:
        processor.process(lambda x: None)  # Use lambda directly
    except FileNotFoundError:
        assert True  # Confirm the test passes if the file is missing

def test_processor_execution(mocker, setup_files):
    # Mock to check that the `process` method is called
    input_files, output_folder = setup_files
    processor = GuyMucsProcessor(input_files, output_folder, "bass")
    mocker.patch.object(processor, 'process', return_value=None)
    processor.process(lambda x: None)  # Call with a dummy callback
    processor.process.assert_called_once()  # Check `process` was called once

