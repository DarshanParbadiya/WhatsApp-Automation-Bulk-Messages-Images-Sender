# main.py
from PySide6.QtWidgets import QApplication
from frontPage import MySideBar
import sys

# Create a Qt application instance.
# QApplication manages the GUI application's control flow and main settings.
app = QApplication(sys.argv)

# Instantiate the main application window, which is a custom sidebar (MySideBar).
# MySideBar is assumed to be defined in 'frontPage.py' and handles the application's front page and sidebar functionalities.
window = MySideBar()

# Show the main application window.
# This makes the window visible to the user.
window.show()

# Start the Qt event loop.
# This line makes the application responsive to user interactions and events.
# The application will continue to run until the event loop is exited (e.g., by closing the main window).
app.exec()