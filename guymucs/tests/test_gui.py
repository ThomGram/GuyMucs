from guymucs.gui import GuyMucsGUI
from PyQt5.QtWidgets import QApplication
import pytest

@pytest.fixture(scope="module")
def app():
    # Initialisation de l'application pour les tests
    return QApplication([])

@pytest.fixture
def gui(app):
    # Crée une instance de l'interface GUI pour les tests
    return GuyMucsGUI()

def test_initial_labels(gui):
    # Vérifie que les labels sont correctement initialisés
    assert gui.input_label.text() == "Fichiers audio sélectionnés : Aucun"
    assert gui.output_label.text() == "Dossier de sortie : Aucun"

def test_select_input_files(mocker, gui):
    # Mock de la méthode QFileDialog pour simuler la sélection de fichiers
    mocker.patch("PyQt5.QtWidgets.QFileDialog.getOpenFileNames", return_value=(["test_audio.mp3"], ""))
    gui.select_input_files()
    assert gui.input_label.text() == "Fichiers audio sélectionnés : test_audio.mp3"

def test_select_output_folder(mocker, gui):
    # Mock de la méthode QFileDialog pour simuler la sélection d'un dossier de sortie
    mocker.patch("PyQt5.QtWidgets.QFileDialog.getExistingDirectory", return_value="output_folder")
    gui.select_output_folder()
    assert gui.output_label.text() == "Dossier de sortie : output_folder"

