#frontPage.py
"""
Main window class for the Whatsapp Helper application.

This module defines the MySideBar class, which inherits from QMainWindow and Ui_MainWindow.
It handles the main application logic, including UI interactions, configuration,
and communication with the Whatsapp helper utilities.
"""

import csv

from PySide6.QtWidgets import QMainWindow

from UI.ui_index import Ui_MainWindow
from utils import DialogBox, FileDialog, Config
from utils.whatsapp_helper import Whatsapp


class MySideBar(QMainWindow, Ui_MainWindow):
    """
    Main application window for the Whatsapp Helper.

    This class manages the UI, configuration, and Whatsapp functionality.
    """

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle("Whatsapp Helper")
        # Load and set configuration values
        self.config_instance = Config(self)
        self.config_instance.set_config_values()
        self.config_instance.load_config_values()

        # Initialize helper instances
        self.whatsapp_instance = Whatsapp(self)
        self.file_dialog_instance = FileDialog()
        self.dialogBox_instance = DialogBox()


        # Setup UI connections and initial states
        self._setup_ui_connections()
        self._initialize_message_type_combobox()
        self.whatsapp_page_button.setChecked(True)  # Set default page

    def _setup_ui_connections(self):
        """Connects UI elements to their respective event handlers."""
        self.whatsapp_page_button.clicked.connect(lambda: self.switch_to_desired_page(0))
        self.settings_page_button.clicked.connect(lambda: self.switch_to_desired_page(1))
        self.manage_page_button.clicked.connect(lambda: self.switch_to_desired_page(2))
        self.timers_page_button.clicked.connect(lambda: self.switch_to_desired_page(3))
        self.message_page_button.clicked.connect(lambda: self.switch_to_desired_page(4))

        self.open_whatsapp_button.clicked.connect(self.handle_whatsapp_page_button)
        self.send_button.clicked.connect(self.whatsapp_instance.send_messages)

        self.save_cookies.clicked.connect(self.whatsapp_instance.save_cookies)
        self.load_cookies.clicked.connect(self.whatsapp_instance.load_cookies)

        self.load_csv_btn.setCheckable(True)
        self.load_csv_btn.clicked.connect(self.handle_load_csv_button)
        self.load_image_btn.clicked.connect(self.handle_load_image_button)
        self.save_custom_message_button.clicked.connect(self.handle_save_message_button)

        self.save_settings_button.clicked.connect(self.config_instance.save_config)
        self.sent_numbers_button.clicked.connect(lambda: self.export_csv_reports("sent_numbers_df"))
        self.invalid_numbers_button.clicked.connect(lambda: self.export_csv_reports("invalid_number_df"))
        self.not_sent_numbers_button.clicked.connect(lambda: self.export_csv_reports("not_sent_number_df"))
        self.create_sample_csv_button.clicked.connect(lambda: self.create_sample_csv("sample.csv"))

    def _initialize_message_type_combobox(self):
        """Initializes the message type combobox with available options."""
        self.select_message_type_combo_box.addItems(self.whatsapp_instance.message_types)
        self.select_message_type_combo_box.currentIndexChanged.connect(self.on_selection_change)

    def export_csv_reports(self, report_type):
        """
        Exports a DataFrame from the Whatsapp instance to a CSV file.

        Args:
            report_type (str): The name of the DataFrame attribute to export.
        """
        data_frame = getattr(self.whatsapp_instance, report_type, None)

        if data_frame is not None:
            data_frame.to_csv(f'{report_type}_output.csv', index=False)
        else:
            print(f"Error: '{report_type}' is not a valid attribute or not a DataFrame.")

    def create_sample_csv(self, file_name):
        """
        Creates a sample CSV file with predefined headers.

        Args:
            file_name (str): The name of the CSV file to create.
        """
        header = ["Contact No", "Message"]

        with open(file_name, mode='w', newline='') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(header)

        print(f"Empty CSV file '{file_name}' created with columns: {header}")

    def on_selection_change(self, index):
        """
        Handles the selection change event of the message type combobox.

        Args:
            index (int): The index of the selected item.
        """
        selected_option = self.select_message_type_combo_box.itemText(index)
        self.whatsapp_instance.current_message_selection = selected_option
        print(f"Selected Option: {selected_option}")

    def handle_load_csv_button(self):
        """Handles the loading of a CSV file for message sending."""
        file_name = self.dialogBox_instance.show_dialog_box()
        if file_name:
            self.excel_text_edit.setPlainText(str(file_name[0]))
            self.whatsapp_instance.csv_path = str(file_name[0])

    def handle_load_image_button(self):
        """Handles the loading of an image file for message sending."""
        file_name = self.dialogBox_instance.show_dialog_box()
        if file_name:
            self.image_text_edit.setPlainText(str(file_name[0]))
            self.whatsapp_instance.image_path = str(file_name[0])

    def handle_save_message_button(self):
        """Handles saving the custom message entered by the user."""
        self.whatsapp_instance.custom_message = self.custom_message.toPlainText()
        print("Message saved")

    def switch_to_desired_page(self, index):
        """
        Switches the stacked widget to the specified page index.

        Args:
            index (int): The index of the page to switch to.
        """
        print(f"changed to {index}")
        self.stackedWidget.setCurrentIndex(index)

    def handle_whatsapp_page_button(self):
        """Handles the opening of the Whatsapp web page."""
        self.whatsapp_instance.open_whatsapp()

    def openDialog(self):
        """Opens a custom dialog (not fully implemented)."""
        from UI.ui_dialog import Ui_Dialog

        dialog_obj = Ui_Dialog(self)
        result = dialog_obj.exec()

        if result == Ui_Dialog.accepted:
            pass