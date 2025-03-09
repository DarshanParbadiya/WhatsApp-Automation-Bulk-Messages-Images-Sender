# utils/whatsapp_helper.py
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from helper import ChromeLauncher
from time import sleep
import pandas
import urllib
from .message_type import Message
from .ui_helper import MessageDialog, DialogBox
from .contact_numbers import ContactNumber
import pickle
import json
from .button_locators import Locators
import pandas as pd
from .config_helper import Config
from .whatsapp_driver_setup import WhatsappDriverSetup
from .whatsapp_core import WhatsappCore # Import WhatsappCore


class Whatsapp(): # Whatsapp class in whatsapp_helper.py now acts as a helper/wrapper
    """
    Helper class to automate WhatsApp Web functionalities, delegating core logic to WhatsappCore.

    This class acts as a higher-level interface for WhatsApp automation, handling input validation
    and delegating the core WebDriver interactions and message sending logic to the WhatsappCore class.

    Refactored from previous 'utils/whatsapp_helper.py': Core logic is moved to 'utils/whatsapp_core.py',
    and this class now primarily focuses on input validation and delegation.

    Backward Compatibility: This class remains fully backward compatible as existing code that
    instantiates and uses 'Whatsapp' will continue to function without any changes to its API.
    """
    debug = True

    def __init__(self, window_instance):
        """
        Initializes the Whatsapp helper instance.

        Args:
            window_instance: An instance of the main application window (e.g., MySideBar).
        """
        self.window_instance = window_instance
        self.whatsapp_core = WhatsappCore(window_instance) # Instantiate WhatsappCore, delegate core logic to it
        self.driver = self.whatsapp_core.driver # Access driver from WhatsappCore (though driver setup is in core)
        self.message_instance = self.whatsapp_core.message_instance
        self.is_verified = self.whatsapp_core.is_verified
        self.is_driver_available = self.whatsapp_core.is_driver_available
        self.custom_message = self.whatsapp_core.custom_message
        self.message_types = self.whatsapp_core.message_types
        self.current_message_selection = self.whatsapp_core.current_message_selection
        self.csv_path = self.whatsapp_core.csv_path
        self.image_path = self.whatsapp_core.image_path
        self.dialogBox_instance = self.whatsapp_core.dialogBox_instance
        self.wait_time = self.whatsapp_core.wait_time
        self.button_locator_instance = self.whatsapp_core.button_locator_instance
        self.sent_numbers_df = self.whatsapp_core.sent_numbers_df
        self.invalid_number_df = self.whatsapp_core.invalid_number_df
        self.not_sent_number_df = self.whatsapp_core.not_sent_number_df


    def printf(*args):
        if Whatsapp.debug == True:
            print(*args)

    def open_whatsapp(self):
        """
        Opens WhatsApp Web, delegating to WhatsappCore.
        """
        self.whatsapp_core.open_whatsapp() # Delegate to core class
        self.driver = self.whatsapp_core.driver # Keep driver instance in sync
        self.is_driver_available = self.whatsapp_core.is_driver_available # Keep driver availability flag in sync


    def do_scan_QR_code(self):
        """
        Prompts user to scan QR code, delegating to WhatsappCore.
        """
        self.whatsapp_core.do_scan_QR_code() # Delegate to core class

    def open_contact(self, number, message):
        """
        Opens contact, delegating to WhatsappCore.
        """
        self.whatsapp_core.open_contact(number, message) # Delegate to core class

    def set_message_type(self, message_type):
        """
        Sets message type, delegating to WhatsappCore.
        """
        self.whatsapp_core.set_message_type(message_type) # Delegate to core class

    def get_contacts(self):
        """
        Gets contacts from CSV, delegating to WhatsappCore (indirectly via validation and data loading).
        """
        return self.whatsapp_core.get_contacts() # Delegate to core class (data loading handled there)

    def _validate_driver_availability(self):
        """
        Validates driver availability, delegating to WhatsappCore (indirectly via core's method).
        """
        return self.whatsapp_core.check_is_driver_available() # Delegate to core class for validation

    def _validate_csv_path(self):
        """
        Validates CSV path, delegating to WhatsappCore (indirectly via core's method).
        """
        return self.whatsapp_core.check_csv_path_available() # Delegate validation to core class

    def _validate_image_path(self):
        """
        Validates image path, delegating to WhatsappCore (indirectly via core's method).
        """
        return self.whatsapp_core.check_image_path_available() # Delegate image path validation to core

    def _validate_inputs(self):
        """
        Validates all inputs before sending, orchestrating validations in WhatsappHelper.
        """
        if not self._validate_driver_availability(): # Validate driver availability
            return False
        if self.current_message_selection is None: # Validate message type selection
            self.dialogBox_instance.show_confirmation_dialog("Please Select the valid option before sending")
            return False
        if not self._validate_csv_path(): # Validate CSV path
            return False
        if self.current_message_selection in [self.message_types[2], self.message_types[3], self.message_types[4]]: # Validate image path if needed
            if not self._validate_image_path():
                return False
        return True


    def send_messages(self):
        """
        Initiates message sending, handling validation and delegating core sending to WhatsappCore.
        """
        if not self._validate_inputs(): # Validate inputs in WhatsappHelper
            return

        self.dialogBox_instance.show_confirmation_dialog("Are you sure You want to send Message?") # Confirmation dialog
        if self.dialogBox_instance.user_response == True:
            Whatsapp.printf('Sending messages') # Use Whatsapp (helper class) for printf
            self.whatsapp_core.send_messages() # Delegate core sending logic to WhatsappCore
        else:
            Whatsapp.printf("User canceled the Process") # Use Whatsapp (helper class) for printf

    def show_error_dialog_box(self, message):
        """
        Shows error dialog, delegating to WhatsappCore's dialog instance.
        """
        self.whatsapp_core.show_error_dialog_box(message) # Delegate to core class's dialog display

    def save_cookies(self):
        """
        Saves cookies, delegating to WhatsappCore.
        """
        self.whatsapp_core.save_cookies() # Delegate cookie saving to core class
        self.printf('saved the cookies') # Use Whatsapp (helper class) for printf

    def load_cookies(self):
        """
        Loads cookies, delegating to WhatsappCore.
        """
        self.whatsapp_core.load_cookies() # Delegate cookie loading to core class
        self.printf('loaded the cookies') # Use Whatsapp (helper class) for printf


    def invalid_number_handler(self, number):
        """
        Handles invalid numbers, delegating to WhatsappCore.
        """
        self.whatsapp_core.invalid_number_handler(number) # Delegate invalid number handling to core class

    def check_message_type_and_send_message(self):
        """
        Delegates message sending orchestration to WhatsappCore.
        """
        self.whatsapp_core.check_message_type_and_send_message() # Delegate message type checking and sending to core class

    def add_details_to_data_frame(self, df, data):
        """
        Adds details to DataFrame, delegating to WhatsappCore (indirectly via data handler in core).
        """
        from .whatsapp_data_handler import WhatsappDataHandler # Local import - same as in WhatsappCore

        data_handler = WhatsappDataHandler() # Instance of data handler (same as in WhatsappCore)
        return data_handler.add_details_to_data_frame(df, data) # Delegate data frame operation to data handler