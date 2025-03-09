I want your help to imporve config of this project 
related files that uses config 
utils/config_helper.py
frontPage.py : here it creates config object and creates as it's property so that when other ojbects need it, they can utilize from it's property
utils/whatsapp_helper.py : it uses the property created in the frontPage.py for it's purpose, 
how to have nice mangement of this configurations

; config.ini
[Database]
host = newhost.example.com
port = 5432
username = user
password = pass

[API]
endpoint = https://api.example.com
timeout = 60

[Attachments]
image_attachment_accept_value = image/*,video/mp4,video/3gpp,video/quicktime
file_attachment_accept_value = *

[Modals]
invalid_modal_text = Phone number shared via url is invalid.
invalid_modal_okay_button_class = x889kno x1a8lsjc xbbxn1n xxbr6pl x1n2onr6 x1rg5ohu xk50ysn x1f6kntn xyesn5m x1z11no5 xjy5m1g x1mnwbp6 x4pb5v6 x178xt8z xm81vs4 xso031l xy80clv x13fuv20 xu3j5b3 x1q0q8m5 x26u7qi x1v8p93f xogb00i x16stqrj x1ftr3km x1hl8ikr xfagghw x9dyr19 x9lcvmn xbtce8p x14v0smp xo8ufso xcjl5na x1k3x3db xuxw1ft xv52azi

[Buttons]
attachment_button_val = //span[@data-icon='plus']
image_attachment_accept_value = image/*,video/mp4,video/3gpp,video/quicktime
file_attachment_accept_value = *
send_message_button_text = Send
send_button_value = //*[@data-icon='send']
invalid_modal_text = Phone number shared via url is invalid.
invalid_modal_okay_button_class = x889kno x1a8lsjc xbbxn1n xxbr6pl x1n2onr6 x1rg5ohu xk50ysn x1f6kntn xyesn5m x1z11no5 xjy5m1g x1mnwbp6 x4pb5v6 x178xt8z xm81vs4 xso031l xy80clv x13fuv20 xu3j5b3 x1q0q8m5 x26u7qi x1v8p93f xogb00i x16stqrj x1ftr3km x1hl8ikr xfagghw x9dyr19 x9lcvmn xbtce8p x14v0smp xo8ufso xcjl5na x1k3x3db xuxw1ft xv52azi

[Timers]
wait = 10
upload_wait = 5
sleep_time = 2

[Chrome]
single_instance = False



import configparser

class Config():
    def __init__(self,window_instance):
        self.window_instance = window_instance
        self.config = configparser.ConfigParser()
        self.config.read('config.ini')
        # self.invalid_modal_okay_button_class = None

    def set_config_values(self):
        # Access values from each section
        self.attachment_button_val = self.config['Buttons']['attachment_button_val']
        self.send_button_value = self.config['Buttons']['send_button_value']
        self.send_message_button_text = self.config['Buttons']['send_message_button_text']

        self.image_attachment_accept_value = self.config['Attachments']['image_attachment_accept_value']
        self.file_attachment_accept_value = self.config['Attachments']['file_attachment_accept_value']

        self.invalid_modal_text = self.config['Modals']['invalid_modal_text']
        self.invalid_modal_okay_button_class = self.config['Modals']['invalid_modal_okay_button_class']

        self.wait_time_spin_box = self.config['Timers']['wait']
        self.upload_time_spin_box = self.config['Timers']['upload_wait']
        self.sleep_time_spin_box = self.config['Timers']['sleep_time']
        self.single_instance = self.config['Chrome']['single_instance']

        # print(attachment_button_val)
        # print(send_button_value)
        # print(send_message_button_text)
        # print(image_attachment_accept_value)
        # print(file_attachment_accept_value)
        # print(invalid_modal_text)
        # print(invalid_modal_okay_button_class)

    def save_config(self):
        # print(self.invalid_model_text.toPlainText())
        self.config['Buttons']['attachment_button_val'] = self.window_instance.attachment_button_val.toPlainText()
        self.config['Buttons']['send_button_value'] = self.window_instance.send_button_value.toPlainText()
        self.config['Buttons']['send_message_button_text'] = self.window_instance.send_message_button_text.toPlainText()

        self.config['Attachments']['image_attachment_accept_value']= self.window_instance.image_attachment_accept_value.toPlainText()
        self.config['Attachments']['file_attachment_accept_value']= self.window_instance.file_attachment_accept_value.toPlainText()

        self.config['Modals']['invalid_modal_text']= self.window_instance.invalid_modal_text.toPlainText()
        self.config['Modals']['invalid_modal_okay_button_class']= self.window_instance.invalid_modal_okay_button_class.toPlainText()
        
        self.config['Timers']['wait'] = str(self.window_instance.wait_time_spin_box.value())
        self.config['Timers']['upload_wait'] = str(self.window_instance.upload_time_spin_box.value())
        self.config['Timers']['sleep_time'] = str(self.window_instance.sleep_time_spin_box.value())
                # Write changes back to file
        with open('config.ini', 'w') as configfile:
            self.config.write(configfile)        

    def load_config_values(self):
        attachment_button_val = self.config['Buttons']['attachment_button_val']
        send_button_value = self.config['Buttons']['send_button_value']
        send_message_button_text = self.config['Buttons']['send_message_button_text']

        image_attachment_accept_value = self.config['Attachments']['image_attachment_accept_value']
        file_attachment_accept_value = self.config['Attachments']['file_attachment_accept_value']

        invalid_modal_text = self.config['Modals']['invalid_modal_text']
        invalid_modal_okay_button_class = self.config['Modals']['invalid_modal_okay_button_class']

        wait_time_spin_box = self.config['Timers']['wait']
        upload_time_spin_box = self.config['Timers']['upload_wait']
        sleep_time_spin_box = self.config['Timers']['sleep_time']


        self.window_instance.invalid_modal_text.setPlainText(str(invalid_modal_text))
        self.window_instance.invalid_modal_okay_button_class.setPlainText(str(invalid_modal_okay_button_class))
        self.window_instance.attachment_button_val.setPlainText(str(attachment_button_val))
        self.window_instance.send_message_button_text.setPlainText(str(send_message_button_text))
        self.window_instance.send_button_value.setPlainText(str(send_button_value))
        self.window_instance.image_attachment_accept_value.setPlainText(str(image_attachment_accept_value))
        self.window_instance.file_attachment_accept_value.setPlainText(str(file_attachment_accept_value))
        self.window_instance.wait_time_spin_box.setValue(int(wait_time_spin_box))
        self.window_instance.upload_time_spin_box.setValue(int(upload_time_spin_box))
        self.window_instance.sleep_time_spin_box.setValue(int(sleep_time_spin_box))


# frontPage.py
"""
Main window class for the Whatsapp Helper application.

This module defines the MySideBar class, which inherits from QMainWindow and Ui_MainWindow.
It handles the main application logic, including UI interactions, configuration,
and communication with the Whatsapp helper utilities.
"""

import csv

from PySide6.QtWidgets import QMainWindow

from UI.ui_index import Ui_MainWindow
from utils import DialogBox, FileDialog, Config  # Updated import
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

        self.save_settings_button.clicked.connect(self.handle_save_settings) # updated
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

    def handle_save_settings(self):
        """Handles saving the current settings to the config file."""
        self.config_manager.update_from_ui(self)

# utils/whatsapp_helper.py
"""
This module provides the Whatsapp class, which handles interactions with
WhatsApp Web using Selenium WebDriver. It includes functionality for opening
WhatsApp, sending messages, handling attachments, and managing cookies.
"""

import json
import pickle
import urllib
from time import sleep

import pandas as pd
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager

from .button_locators import Locators
from .contact_numbers import ContactNumber
from .message_type import Message
from .ui_helper import DialogBox, MessageDialog


class Whatsapp:
    """
    A class to automate WhatsApp Web interactions.

    This class provides methods for opening WhatsApp, sending messages,
    handling attachments, and managing cookies.
    """

    debug = True

    def __init__(self, window_instance):
        """
        Initializes the Whatsapp instance.

        Args:
            window_instance: An instance of the main application window.
        """
        self.window_instance = window_instance
        self.driver = False
        self.message_instance = Message()
        self.is_verified = False
        self.is_driver_available = False
        self.custom_message = None
        self.message_types = ["Same Messages for everyone", "Different Messages for Each", "Send Image",
                              "Send Image with Same Message", "Send Image with Different Message", "Send File"]
        self.current_message_selection = None
        self.csv_path = None
        self.image_path = None
        self.dialogBox_instance = DialogBox()
        self.wait_time = self.window_instance.config_instance.wait_time_spin_box
        self.button_locator_instance = Locators()
        self.sent_numbers_df = pd.DataFrame(columns=['number'])
        self.invalid_number_df = pd.DataFrame(columns=['number'])
        self.not_sent_number_df = pd.DataFrame(columns=['number'])

    def printf(*args):
        """Prints debug messages if debugging is enabled."""
        if Whatsapp.debug:
            print(*args)

    def open_whatsapp(self):
        """Opens WhatsApp Web in a Chrome browser."""
        if self.window_instance.config_instance.single_instance == "True":
            self.printf('single Instance is on')
            chrome_options = Options()
            chrome_options.debugger_address = "localhost:9222"
            self.driver = webdriver.Chrome(service=Service(), options=chrome_options)
        else:
            self.driver = webdriver.Chrome()
        self.driver.get('https://web.whatsapp.com')
        self.is_driver_available = True

    def do_scan_QR_code(self):
        """Displays a dialog to prompt the user to scan the QR code."""
        if not self.is_verified:
            dialog = MessageDialog("Please Verify the QR code")
            dialog.exec()

    def open_contact(self, number, message):
        """Opens a WhatsApp chat with the specified number and message."""
        url = 'https://web.whatsapp.com/send?phone=' + str(number) + '&text=' + urllib.parse.quote(message)
        self.driver.get(url)
        self.printf(f'Opening {url}')

    def set_message_type(self, message_type):
        """Sets the message type."""
        self.message_instance.set_message_type(message_type)

    def get_contacts(self):
        """Loads contact data from the specified CSV or Excel file."""
        try:
            print(self.csv_path)
            df = ContactNumber.load_contacts(self.csv_path)
        except Exception as e:
            self.show_error_dialog_box(e)
            return False
        else:
            return df

    def check_is_driver_available(self):
        """Checks if the WebDriver instance is available."""
        if not self.is_driver_available:
            DialogBox().show_confirmation_dialog("Driver is not available so open the whatsapp first.")
            return False
        return True

    def check_csv_path_available(self):
        """Checks if the CSV file path is available."""
        if not self.csv_path:
            DialogBox().show_confirmation_dialog("csv file is not available Please select the csv fie first.")
            return False
        return True

    def check_image_path_available(self):
        """Checks if the image file path is available."""
        if not self.image_path:
            DialogBox().show_confirmation_dialog("image file is not available Please select the fie first.")
            return False
        return True

    def send_messages(self):
        """Sends messages to contacts based on the selected message type."""
        response = self.check_is_driver_available()
        if not response:
            return

        if self.current_message_selection is None:
            self.dialogBox_instance.show_confirmation_dialog("Please Select the valid option before sending")
            return

        response = self.check_csv_path_available()
        if not response:
            return

        if self.current_message_selection in [self.message_types[2], self.message_types[3], self.message_types[4]]:
            response = self.check_image_path_available()
            if not response:
                return

        if self.is_driver_available:
            self.dialogBox_instance.show_confirmation_dialog("Are you sure You want to send Message?")
            if self.dialogBox_instance.user_response:
                self.check_message_type_and_send_message()
            else:
                self.printf("User canceled the Process")
        else:
            self.printf("driver not available")

    def show_error_dialog_box(self, message):
        """Displays an error dialog with the specified message."""
        self.dialogBox_instance.show_confirmation_dialog(str(message))

    def save_cookies(self):
        """Saves cookies and local storage to files."""
        if self.is_driver_available:
            with open("whatsapp_cookies.pkl", "wb") as file:
                pickle.dump(self.driver.get_cookies(), file)
            local_storage = self.driver.execute_script("return window.localStorage;")
            with open("whatsapp_local_storage.json", "w") as file:
                json.dump(local_storage, file)
            self.printf('saved the cookies')

    def load_cookies(self):
        """Loads cookies and local storage from files."""
        with open("whatsapp_cookies.pkl", "rb") as file:
            cookies = pickle.load(file)
            for cookie in cookies:
                self.driver.add_cookie(cookie)
            self.printf('loaded the cookies')

        with open("whatsapp_local_storage.json", "r") as file:
            local_storage = json.load(file)
            for key, value in local_storage.items():
                self.driver.execute_script(f"window.localStorage.setItem('{key}', '{value}');")

    def add_details_to_data_frame(self, df, data):
        """Adds a row to the specified DataFrame."""
        self.printf("adding the row to the dataframe")
        new_row = pd.DataFrame([data], columns=['number'])
        temp_df = pd.concat([df, new_row], ignore_index=True)
        return temp_df

    def invalid_number_handler(self, number):
        """Handles invalid phone numbers."""
        try:
            contains = self.button_locator_instance.does_page_contains_text(self.driver, self.wait_time,
                                                                          self.button_locator_instance.invalid_modal_text)
            if contains:
                self.invalid_number_df = self.add_details_to_data_frame(self.invalid_number_df, number)
                self.printf("Invalid Numbers")
                self.printf(self.invalid_number_df)
                try:
                    button = self.button_locator_instance.x_path_locator(self.driver, self.wait_time,
                                                                      self.button_locator_instance.invalid_modal_okay_button_value)
                except Exception as e:
                    self.printf("can not click on invalid number modal okay button", e)
                else:
                    button.click()
                    self.printf("closed the invalid number modal")
            else:
                self.not_sent_number_df = self.add_details_to_data_frame(self.not_sent_number_df, number)
                self.printf("Not sent Numbers")
                self.printf(self.not_sent_number_df)
        except Exception as e:
            self.printf("Error while finding invalid, try catch block", e)