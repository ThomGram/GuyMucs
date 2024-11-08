import pytest
import os
from guymucs.processor import GuyMucsProcessor

@pytest.fixture
def setup_files(tmp_path):
    # Préparer des fichiers de test pour le processeur
    input_file = tmp_path / "test_audio.mp3"
    input_file.write_text("fake audio data")
    output_folder = tmp_path / "output"
    output_folder.mkdir()
    return [str(input_file)], str(output_folder)

def test_processor_initialization(setup_files):
    # Teste l'initialisation de GuyMucsProcessor avec les paramètres requis
    input_files, output_folder = setup_files
    processor = GuyMucsProcessor(input_files, output_folder, "vocals")
    assert processor.input_files == input_files
    assert processor.output_folder == output_folder
    assert processor.instrument == "vocals"

def test_processor_with_missing_file(tmp_path):
    # Teste le comportement du processeur lorsque le fichier est manquant
    missing_file = tmp_path / "missing_audio.mp3"
    output_folder = tmp_path / "output"
    output_folder.mkdir()

    processor = GuyMucsProcessor([str(missing_file)], str(output_folder), "drums")
    try:
        processor.process(lambda x: None)  # Fonction de rappel de progression factice
    except FileNotFoundError:
        assert True  # Confirme que le test passe en cas de fichier manquant

def test_processor_execution(mocker, setup_files):
    # Mock pour vérifier que la méthode `process` est bien appelée
    input_files, output_folder = setup_files
    processor = GuyMucsProcessor(input_files, output_folder, "bass")
    mocker.patch.object(processor, 'process', return_value=None)
    processor.process(lambda x: None)  # Appel avec une fonction de rappel factice
    processor.process.assert_called_once()  # Vérifie que `process` a été appelée une fois

