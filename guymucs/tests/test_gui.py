import pytest
from guymucs.gui import GuyMucsGUI

@pytest.fixture
def gui(qtbot):
    # Initialiser l'interface pour les tests
    test_gui = GuyMucsGUI()
    qtbot.addWidget(test_gui)
    return test_gui

def test_initial_labels(gui):
    # Vérifie que les labels sont correctement initialisés en anglais
    assert gui.input_label.text() == "Selected audio files: None"
    assert gui.output_label.text() == "Output folder: None"

def test_select_input_files(mocker, gui):
    # Mock QFileDialog pour retourner un fichier de test
    mocker.patch('PyQt5.QtWidgets.QFileDialog.getOpenFileNames', return_value=(["test_audio.mp3"], ""))
    gui.select_input_files()
    assert gui.input_label.text() == "Selected audio files: test_audio.mp3"

def test_select_output_folder(mocker, gui):
    # Mock QFileDialog pour retourner un dossier de test
    mocker.patch('PyQt5.QtWidgets.QFileDialog.getExistingDirectory', return_value="/test/output")
    gui.select_output_folder()
    assert gui.output_label.text() == "Output folder: /test/output"

