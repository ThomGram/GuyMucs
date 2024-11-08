import sys
from PyQt5.QtWidgets import QApplication
from guymucs.gui import GuyMucsGUI

def main():
    # Initialize the PyQt5 application
    app = QApplication(sys.argv)
    
    # Create and show the main window
    gui = GuyMucsGUI()
    gui.show()
    
    # Execute the application
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()

