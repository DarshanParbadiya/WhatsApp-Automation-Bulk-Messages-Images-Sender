# frontPage.py
from UI.ui_index import Ui_MainWindow
from PySide6.QtGui import QAction
from PySide6.QtWidgets import QMainWindow
from utils.whatsapp_helper import Whatsapp
from utils import DialogBox,FileDialog,Config
import configparser
import csv

class MySideBar(QMainWindow, Ui_MainWindow):
    """
    Main application window class for the Whatsapp Helper application.

    Refactored to improve code organization and maintainability by using helper methods
    to group related functionalities within the class.

    Inherits from QMainWindow for windowing functionality and Ui_MainWindow
    for the user interface elements defined in 'UI/ui_index.py'.
    """
    def __init__(self):
        """
        Initializes the MySideBar application window.

        Sets up the UI, window title, and initializes utility instances.
        Organizes initialization and signal connection logic into helper methods
        to improve readability and reduce the length of the __init__ method.
        """
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle("Whatsapp Helper")

        self._init_config_related()  # Initialize configuration related instances and settings
        self._init_whatsapp_related() # Initialize Whatsapp related instances
        self._init_dialog_and_file_dialog() # Initialize dialog and file dialog instances

        self._connect_navigation_buttons() # Connect page navigation buttons
        self._setup_message_type_combobox() # Setup message type combo box
        self._connect_action_buttons() # Connect action buttons (send, save, load, etc.)
        self._connect_report_buttons() # Connect buttons for report generation

    def _init_config_related(self):
        """
        Initializes configuration related instances and settings.

        Creates and configures the Config instance to manage application settings.
        """
        self.config_instance = Config(self)
        self.config_instance.set_config_values()
        self.config_instance.load_config_values()

    def _init_whatsapp_related(self):
        """
        Initializes Whatsapp related instances.

        Creates the Whatsapp instance responsible for handling Whatsapp functionalities.
        """
        self.whatsapp_instance = Whatsapp(self)

    def _init_dialog_and_file_dialog(self):
        """
        Initializes dialog and file dialog instances.

        Creates instances of DialogBox and FileDialog for UI interactions like
        showing dialogs and handling file selections.
        """
        self.file_dialog_instance = FileDialog()
        self.dialogBox_instance = DialogBox()


    def _connect_navigation_buttons(self):
        """
        Connects navigation buttons to their respective page switching functions.

        Sets up button click signals for Whatsapp, Settings, Manage, Timers, and Message page buttons
        to call the switch_to_desired_page method with the corresponding page index.
        """
        self.whatsapp_page_button.clicked.connect(lambda: self.switch_to_desired_page(0))
        self.whatsapp_page_button.setChecked(True)
        self.settings_page_button.clicked.connect(lambda: self.switch_to_desired_page(1))
        self.manage_page_button.clicked.connect(lambda: self.switch_to_desired_page(2))
        self.timers_page_button.clicked.connect(lambda: self.switch_to_desired_page(3))
        self.message_page_button.clicked.connect(lambda: self.switch_to_desired_page(4))

    def _setup_message_type_combobox(self):
        """
        Sets up the message type combo box.

        Populates the combo box with message types from the whatsapp_instance and
        connects the currentIndexChanged signal to the on_selection_change method.
        """
        self.select_message_type_combo_box.addItems(self.whatsapp_instance.message_types)
        self.select_message_type_combo_box.currentIndexChanged.connect(self.on_selection_change)

    def _connect_action_buttons(self):
        """
        Connects action buttons (like send, save, load, etc.) to their handlers.

        Sets up button click signals for various action buttons on the UI,
        connecting them to methods for opening Whatsapp, sending messages,
        saving/loading cookies, loading CSV/image files, and saving custom messages.
        """
        self.open_whatsapp_button.clicked.connect(self.handle_whatsapp_page_button)
        self.send_button.clicked.connect(self.whatsapp_instance.send_messages)

        self.save_cookies.clicked.connect(self.whatsapp_instance.save_cookies)
        self.load_cookies.clicked.connect(self.whatsapp_instance.load_cookies)

        self.load_csv_btn.setCheckable(True)
        self.load_csv_btn.clicked.connect(self.handle_load_csv_button)
        self.load_image_btn.clicked.connect(self.handle_load_image_button)
        self.save_custom_message_button.clicked.connect(self.handle_save_message_button)
        self.save_settings_button.clicked.connect(self.config_instance.save_config)


    def _connect_report_buttons(self):
        """
        Connects report generation buttons to their respective export functions.

        Sets up button click signals for buttons related to exporting reports
        (sent numbers, invalid numbers, not sent numbers) and creating a sample CSV file.
        """
        self.sent_numbers_button.clicked.connect(lambda: self.export_csv_reports("sent_numbers_df"))
        self.invalid_numbers_button.clicked.connect(lambda: self.export_csv_reports("invalid_number_df"))
        self.not_sent_numbers_button.clicked.connect(lambda: self.export_csv_reports("not_sent_number_df"))
        self.create_sample_csv_button.clicked.connect(lambda: self.create_sample_csv("sample.csv"))


    def export_csv_reports(self, report_type):
        """
        Exports a specific report (DataFrame) from the whatsapp_instance to a CSV file.

        Args:
            report_type (str): The name of the attribute in whatsapp_instance that holds the DataFrame
                                 to be exported (e.g., "sent_numbers_df", "invalid_number_df").
        """
        data_frame = getattr(self.whatsapp_instance, report_type, None)

        if data_frame is not None:
            data_frame.to_csv(f'{report_type}_output.csv', index=False)
        else:
            print(f"Error: '{report_type}' is not a valid attribute or not a DataFrame.")


    def create_sample_csv(self, file_name):
        """
        Creates a sample CSV file with predefined headers for contact number and message.

        Args:
            file_name (str): The name of the CSV file to be created.
        """
        header = ["Contact No", "Message"]

        with open(file_name, mode='w', newline='') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(header)

        print(f"Empty CSV file '{file_name}' created with columns: {header}")


    def on_selection_change(self, index):
        """
        Handles the event when the selected item in the message type combo box changes.

        Updates the whatsapp_instance's current_message_selection attribute
        with the newly selected message type.

        Args:
            index (int): The index of the newly selected item in the combo box.
        """
        selected_option = self.select_message_type_combo_box.itemText(index)
        self.whatsapp_instance.current_message_selection = selected_option
        print(f"Selected Option: {selected_option}")


    def handle_load_csv_button(self):
        """
        Handles the click event of the load CSV button.

        Opens a file dialog to allow the user to select a CSV file.
        Sets the selected file path to the excel_text_edit and updates
        the csv_path attribute in the whatsapp_instance.
        """
        file_name = self.dialogBox_instance.show_dialog_box()
        self.excel_text_edit.setPlainText(str(file_name[0]))
        self.whatsapp_instance.csv_path = str(file_name[0])


    def handle_load_image_button(self):
        """
        Handles the click event of the load image button.

        Opens a file dialog to allow the user to select an image file.
        Sets the selected file path to the image_text_edit and updates
        the image_path attribute in the whatsapp_instance.
        """
        file_name = self.dialogBox_instance.show_dialog_box()
        self.image_text_edit.setPlainText(str(file_name[0]))
        self.whatsapp_instance.image_path = str(file_name[0])


    def handle_save_message_button(self):
        """
        Handles the click event of the save custom message button.

        Retrieves the text from the custom_message text edit and updates
        the custom_message attribute in the whatsapp_instance.
        """
        self.whatsapp_instance.custom_message = self.custom_message.toPlainText()
        print("Message saved")


    def switch_to_desired_page(self, index):
        """
        Switches the stacked widget to the page at the specified index.

        This function is used for navigation between different sections of the application UI.

        Args:
            index (int): The index of the page to switch to in the stacked widget.
        """
        print(f"changed to {index}")
        self.stackedWidget.setCurrentIndex(index)


    def handle_whatsapp_page_button(self):
        """
        Handles the click event of the open Whatsapp button.

        Calls the open_whatsapp method of the whatsapp_instance to
        initiate the process of opening Whatsapp in a browser.
        """
        self.whatsapp_instance.open_whatsapp()


    def openDialog(self):
        """
        Opens a custom dialog (potentially for future use or currently unused).

        This method currently imports UI.ui_dialog and instantiates Ui_Dialog,
        but the purpose and usage within the application are not clear from the code.
        It might be a leftover or intended for future dialog implementations.
        """
        from UI.ui_dialog import Ui_Dialog
        dialog_obj = Ui_Dialog(self)
        result = dialog_obj.exec()

        if result == Ui_Dialog.accepted:
            pass