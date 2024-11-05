from PySide6.QtWidgets import QApplication
from frontPage import MySideBar
import sys

app = QApplication(sys.argv)
window = MySideBar()

window.show()

app.exec()