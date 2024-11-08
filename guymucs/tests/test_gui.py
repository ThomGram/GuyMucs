import pytest
from guymucs.gui import GuyMucsGUI

@pytest.fixture
def gui(qtbot):
    # Initialize the GUI for testing
    test_gui = GuyMucsGUI()
    qtbot.addWidget(test_gui)
    return test_gui

@pytest.mark.skip(reason="Skip Qt GUI test temporarily for CI debugging")
def test_initial_labels(gui):
    # Check that labels are correctly initialized in English
    assert gui.input_label.text() == "Selected audio files: None"
    assert gui.output_label.text() == "Output folder: None"

@pytest.mark.skip(reason="Skip Qt GUI test temporarily for CI debugging")
def test_select_input_files(mocker, gui):
    # Mock QFileDialog to return a test file
    mocker.patch('PyQt5.QtWidgets.QFileDialog.getOpenFileNames', return_value=(["test_audio.mp3"], ""))
    gui.select_input_files()
    assert gui.input_label.text() == "Selected audio files: test_audio.mp3"

@pytest.mark.skip(reason="Skip Qt GUI test temporarily for CI debugging")
def test_select_output_folder(mocker, gui):
    # Mock QFileDialog to return a test directory
    mocker.patch('PyQt5.QtWidgets.QFileDialog.getExistingDirectory', return_value="/test/output")
    gui.select_output_folder()
    assert gui.output_label.text() == "Output folder: /test/output"

