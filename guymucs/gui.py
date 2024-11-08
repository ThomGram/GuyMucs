import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QFileDialog, QLabel, QMessageBox, QComboBox, QProgressBar
from guymucs.processor import GuyMucsProcessor
from PyQt5.QtCore import QThread, pyqtSignal

class SeparationThread(QThread):
    # Signal to update progress
    progress = pyqtSignal(int)

    def __init__(self, processor):
        super().__init__()
        self.processor = processor

    def run(self):
        # Run the separation process
        self.processor.process(self.progress)

class GuyMucsGUI(QWidget):
    def __init__(self):
        super().__init__()
        self.input_files = []
        self.output_folder = ""
        self.selected_instrument = "vocals"
        self.initUI()

    def initUI(self):
        layout = QVBoxLayout()

        # Label for selected input files
        self.input_label = QLabel("Selected audio files: None")
        layout.addWidget(self.input_label)
        
        # Label for selected output folder
        self.output_label = QLabel("Output folder: None")
        layout.addWidget(self.output_label)

        # Button to select input audio files
        self.select_input_btn = QPushButton("Select audio files")
        self.select_input_btn.clicked.connect(self.select_input_files)
        layout.addWidget(self.select_input_btn)

        # Button to select output folder
        self.select_output_btn = QPushButton("Select output folder")
        self.select_output_btn.clicked.connect(self.select_output_folder)
        layout.addWidget(self.select_output_btn)

        # Dropdown to select instrument to separate
        self.instrument_selector = QComboBox()
        self.instrument_selector.addItems(["vocals", "drums", "bass", "other"])
        self.instrument_selector.currentTextChanged.connect(self.set_instrument)
        layout.addWidget(self.instrument_selector)

        # Button to start separation
        self.run_btn = QPushButton("Start separation")
        self.run_btn.clicked.connect(self.run_separation)
        layout.addWidget(self.run_btn)

        # Progress bar
        self.progress_bar = QProgressBar()
        layout.addWidget(self.progress_bar)

        # Window settings
        self.setLayout(layout)
        self.setWindowTitle('GuyMucs - Audio Separation GUI')
        self.setGeometry(100, 100, 400, 300)

    def set_instrument(self, text):
        # Update selected instrument
        self.selected_instrument = text

    def select_input_files(self):
        # Open dialog to select audio files
        files, _ = QFileDialog.getOpenFileNames(self, "Select audio files")
        if files:
            self.input_files = files
            self.input_label.setText(f"Selected audio files: {', '.join(files)}")

    def select_output_folder(self):
        # Open dialog to select output folder
        folder = QFileDialog.getExistingDirectory(self, "Select output folder")
        if folder:
            self.output_folder = folder
            self.output_label.setText(f"Output folder: {folder}")

    def run_separation(self):
        # Check that input files and output folder are selected
        if not self.input_files:
            QMessageBox.warning(self, "Error", "Please select at least one audio file.")
            return
        if not self.output_folder:
            QMessageBox.warning(self, "Error", "Please select an output folder.")
            return

        # Initialize processor with selected instrument
        processor = GuyMucsProcessor(self.input_files, self.output_folder, self.selected_instrument)

        # Setup the separation thread and start it
        self.thread = SeparationThread(processor)
        self.thread.progress.connect(self.progress_bar.setValue)
        self.thread.finished.connect(self.on_separation_finished)
        self.thread.start()

    def on_separation_finished(self):
        # Show message when separation is complete
        QMessageBox.information(self, "Success", "Audio separation completed.")

