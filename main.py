"""
Main application entry point for the Whatsapp Helper.

This script initializes the PySide6 application, creates the main window,
and starts the event loop.
"""

import sys

from PySide6.QtWidgets import QApplication

from frontPage import MySideBar


def main():
    """
    Initializes and runs the Whatsapp Helper application.
    """
    try:
        app = QApplication(sys.argv)
        window = MySideBar()  # Create an instance of the main window

        window.show()  # Display the main window

        sys.exit(app.exec())  # Start the application event loop
    except Exception as e:
        print(f"An error occurred during application startup: {e}")
        sys.exit(1) # Exit with an error code

if __name__ == "__main__":
    main()