import sys
from PySide6.QtWidgets import QApplication, QDialog, QVBoxLayout, QPushButton, QLabel, QMessageBox,QWidget,QFileDialog

class MessageDialog(QDialog):
    def __init__(self, message):
        super().__init__()

        self.setWindowTitle("Message Dialog")
        
        # Create a layout
        layout = QVBoxLayout()

        # Create a label to show the message
        self.label = QLabel(message)
        layout.addWidget(self.label)

        # Create an OK button
        self.ok_button = QPushButton("OK")
        self.ok_button.clicked.connect(self.accept)  # Close the dialog when clicked
        layout.addWidget(self.ok_button)

        # Set the layout for the dialog
        self.setLayout(layout)

class DialogBox(QWidget):
    
    def __init__(self):
        super().__init__()
        self.user_response = None
        self.file_name = None


    def show_confirmation_dialog(self,message="Are you sure you want to proceed?"):
        # Create the dialog box
        dialog = QMessageBox()
        dialog.setWindowTitle("Confirmation")
        dialog.setText(message)
        dialog.setStandardButtons(QMessageBox.Yes | QMessageBox.No)

        # Execute the dialog and get the result
        result = dialog.exec()

        # Check which button was pressed
        if result == QMessageBox.Yes:
            self.on_yes_pressed()
        else:
            self.on_no_pressed()


    def show_dialog_box(self):
        print('showing the dialog box')
        # Open a QFileDialog to select a CSV file
        dialog = QFileDialog()
        dialogSuccessful = dialog.exec()
        selected_files = dialog.selectedFiles()
        if dialogSuccessful:
            self.file_name = selected_files
            return self.file_name


    def on_yes_pressed(self):
        # print("Yes button pressed: Proceeding with action.")
        self.user_response = True


    def on_no_pressed(self):
        # print("No button pressed: Action canceled.")
        self.user_response = False

class FileDialog(QWidget):
    def __init__(self):
        super().__init__()
        self.file_name = None
    
    
    def show_dialog_box(self):
        print('showing the dialog box')
     # Open a QFileDialog to select a CSV file
        dialog = QFileDialog()
        dialogSuccessful = dialog.exec()
        selected_files = dialog.selectedFiles()
        if dialogSuccessful:
            self.file_name = selected_files

        # if file_name:
        #     try:
        #         # Load the CSV file into a DataFrame
        #         df = pd.read_csv(file_name)

        #         # Convert the DataFrame to a string format and set it to the QTextEdit
        #         self.excel_text_edit.setPlainText(df.to_string(index=False))

        #     except Exception as e:
        #         self.excel_text_edit.setPlainText(f"Error loading CSV: {e}")
