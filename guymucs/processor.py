import os
from demucs import separate
from PyQt5.QtCore import pyqtSignal
import pkg_resources

class GuyMucsProcessor:
    def __init__(self, input_files, output_folder, instrument):
        """
        Initializes the processor with input files, output folder, and selected instrument.
        
        :param input_files: List of input audio files
        :param output_folder: Folder to store output files
        :param instrument: Selected instrument to separate (vocals, drums, bass, or other)
        """
        self.input_files = input_files
        self.output_folder = output_folder
        self.instrument = instrument

    def get_files_path(self):
        """
        Returns the path to files.txt, needed by Demucs.
        
        :return: Path to files.txt in the demucs package
        """
        # Use pkg_resources to dynamically locate files.txt
        return pkg_resources.resource_filename('demucs.remote', 'files.txt')

    def process(self, progress_callback):
        """
        Processes each input file, separates the chosen instrument, and updates progress.
        
        :param progress_callback: Callback function to update progress in the GUI
        """
        # Ensure output directories exist
        instrument_path = os.path.join(self.output_folder, f"{self.instrument}_only")
        other_path = os.path.join(self.output_folder, "accompaniment")
        os.makedirs(instrument_path, exist_ok=True)
        os.makedirs(other_path, exist_ok=True)

        # Loop through each input file and perform separation
        for i, file in enumerate(self.input_files):
            # Run Demucs to separate the selected instrument and other components
            output_dir = os.path.join(self.output_folder, "htdemucs_output")
            os.makedirs(output_dir, exist_ok=True)

            # Setting up Demucs command with the specific instrument
            if self.instrument == "vocals":
                demucs_args = ["-n", "htdemucs", "-o", output_dir, file]
            else:
                demucs_args = ["-n", "htdemucs", "-o", output_dir, "--two-stems", self.instrument, file]

            # Execute Demucs command
            separate.main(demucs_args)

            # Move separated files to their respective folders
            base_name = os.path.splitext(os.path.basename(file))[0]
            instrument_file = os.path.join(output_dir, base_name, f"{self.instrument}.wav")
            other_file = os.path.join(output_dir, base_name, f"no_{self.instrument}.wav")

            if os.path.exists(instrument_file):
                os.rename(instrument_file, os.path.join(instrument_path, f"{base_name}_{self.instrument}.wav"))

            # Combine other components to form the accompaniment track
            other_components = ["vocals", "drums", "bass", "other"]
            other_components.remove(self.instrument)  # Exclude the chosen instrument
            combined_other_path = os.path.join(other_path, f"{base_name}_accompaniment.wav")
            self.combine_audio_files(output_dir, base_name, other_components, combined_other_path)

            # Update progress in GUI
            progress_callback(int((i + 1) / len(self.input_files) * 100))  # Directly call instead of emit


    def combine_audio_files(self, output_dir, base_name, components, output_path):
        """
        Combines the specified audio components into one file for the accompaniment.
        
        :param output_dir: Directory where separated audio files are stored
        :param base_name: Base name of the audio track
        :param components: List of components to combine (e.g., drums, bass, etc.)
        :param output_path: Path for the combined output file
        """
        from pydub import AudioSegment

        # Initialize an empty AudioSegment to combine other components
        combined_audio = None
        for component in components:
            component_file = os.path.join(output_dir, base_name, f"{component}.wav")
            if os.path.exists(component_file):
                audio_segment = AudioSegment.from_wav(component_file)
                combined_audio = audio_segment if combined_audio is None else combined_audio.overlay(audio_segment)

        # Export the combined accompaniment track
        if combined_audio:
            combined_audio.export(output_path, format="wav")

