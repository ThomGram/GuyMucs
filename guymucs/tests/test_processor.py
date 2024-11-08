import pytest
from guymucs.processor import GuyMucsProcessor
import os

@pytest.fixture
def setup_files(tmp_path):
    # Crée un fichier audio fictif dans un dossier temporaire pour les tests
    input_file = tmp_path / "test_audio.mp3"
    input_file.touch()
    output_folder = tmp_path / "output"
    output_folder.mkdir()
    return [str(input_file)], str(output_folder)

def test_processor_initialization(setup_files):
    input_files, output_folder = setup_files
    processor = GuyMucsProcessor(input_files, output_folder)

    # Vérifie que les fichiers et dossiers sont correctement initialisés
    assert processor.input_files == input_files
    assert processor.output_folder == output_folder

def test_processor_with_missing_file(tmp_path):
    # Teste le comportement du processeur lorsque le fichier est manquant
    missing_file = tmp_path / "missing_audio.mp3"
    output_folder = tmp_path / "output"
    output_folder.mkdir()

    processor = GuyMucsProcessor([str(missing_file)], str(output_folder))
    with pytest.raises(FileNotFoundError):
        processor.process()

def test_processor_execution(mocker, setup_files):
    input_files, output_folder = setup_files
    processor = GuyMucsProcessor(input_files, output_folder)

    # Mock de la méthode principale de séparation pour éviter un appel réel
    mocker.patch("demucs.separate.main")

    # Exécute la méthode de traitement sans erreur
    processor.process()
    demucs.separate.main.assert_called_once_with(["-o", output_folder, input_files[0]])

