# ui_logic.py

from PySide6.QtUiTools import QUiLoader
from PySide6.QtWidgets import QWidget
from PySide6.QtCore import QFile
import UI.index_ui
from PySide6 import uic

import os


class UILogic(QWidget):
    def __init__(self):
        super().__init__()

        # Load the .ui file
        ui_path = os.path.join(os.path.dirname(__file__), "UI", "index.ui")
        
        uic.loadUi(ui_path, self)

        # another way of importing the ui file
        # ui_file = QFile(ui_path)
        # ui_file.open(QFile.ReadOnly)


        # loader = QUiLoader()
        # self.ui = loader.load(ui_file, self)
        # ui_file.close()

        self.setWindowTitle("Side Bar menu")

        # Set up signal connections and logic here
        # self.setup_connections()

    # def setup_connections(self):
    #     # Access widgets using self.ui.findChild and set up signals
    #     button = self.ui.findChild(QPushButton, "myButton")
    #     button.clicked.connect(self.on_button_click)

    def on_button_click(self):
        print("Button clicked!")
