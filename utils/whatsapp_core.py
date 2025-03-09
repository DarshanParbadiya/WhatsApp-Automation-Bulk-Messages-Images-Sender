# utils/whatsapp_core.py
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from .message_type import Message
from .ui_helper import MessageDialog, DialogBox
from .button_locators import Locators
import pandas as pd
import urllib
import pickle
import json
from time import sleep  # Import sleep here as it's used within core logic


class WhatsappCore:  # Renamed to WhatsappCore to distinguish from helper, and to better reflect its role
    """
    Core class containing the main logic for WhatsApp Web automation.

    This class encapsulates the core functionalities for interacting with WhatsApp Web using
    Selenium, including opening contacts, sending messages (text, images, files), handling
    invalid numbers, and managing cookies.

    Refactored from 'utils/whatsapp_helper.py': This class now contains the core logic,
    with driver setup moved to 'whatsapp_driver_setup.py' and data handling to
    'whatsapp_data_handler.py'. The 'Whatsapp' class in 'whatsapp_helper.py' now acts
    as a higher-level helper, delegating core operations to this class.

    Backward Compatibility: This class is used internally within 'utils/whatsapp_helper.py'
    and does not directly affect backward compatibility of the 'Whatsapp' class API.
    """
    debug = True

    def __init__(self, window_instance):
        """
        Initializes the WhatsappCore instance.

        Args:
            window_instance: An instance of the main application window (e.g., MySideBar),
                             used to access UI elements and configuration settings.
        """
        self.window_instance = window_instance
        self.driver = False  # Selenium WebDriver instance, initialized in open_whatsapp
        self.message_instance = Message()
        self.is_verified = False
        self.is_driver_available = False
        self.custom_message = None
        self.message_types = ["Same Messages for everyone", "Different Messages for Each", "Send Image",
                              "Send Image with Same Message", "Send Image with Different Message",
                              "Send File"]
        self.current_message_selection = None
        self.csv_path = None
        self.image_path = None
        self.dialogBox_instance = DialogBox()
        self.wait_time = self.window_instance.config_instance.wait_time_spin_box
        self.button_locator_instance = Locators()
        self.sent_numbers_df = pd.DataFrame(columns=['number'])
        self.invalid_number_df = pd.DataFrame(columns=['number'])
        self.not_sent_number_df = pd.DataFrame(columns=['number'])

    @staticmethod
    def printf(*args):
        """
        Prints debug messages if debug mode is enabled.
        """
        if WhatsappCore.debug == True:  # Use WhatsappCore for static method call
            print(*args)

    def open_whatsapp(self):
        """
        Opens WhatsApp Web in a Chrome browser instance.

        Utilizes WhatsappDriverSetup to initialize the WebDriver. Sets the driver instance
        and updates the 'is_driver_available' flag.
        """
        from .whatsapp_driver_setup import WhatsappDriverSetup  # Local import to avoid circular dependency

        driver_setup = WhatsappDriverSetup()  # Instance of driver setup class
        single_instance_config = (
                    self.window_instance.config_instance.single_instance == "True")  # Get single instance config
        self.driver = driver_setup.setup_driver(
            single_instance=single_instance_config)  # Setup driver using driver setup class
        self.driver.get('https://web.whatsapp.com')  # Navigate to WhatsApp Web
        self.is_driver_available = True

    def do_scan_QR_code(self):
        """
        Displays a dialog box prompting the user to scan the QR code.
        """
        if not self.is_verified:
            dialog = MessageDialog("Please Verify the QR code")
            dialog.exec()  # Show the dialog

    def open_contact(self, number, message):
        """
        Opens a WhatsApp chat for a given contact number with a pre-filled message.

        Navigates the WebDriver to the WhatsApp Web URL for sending a message
        to the specified phone number. URL encodes the message.

        Args:
            number (str): The recipient's phone number.
            message (str): The message to pre-fill in the chat input.
        """
        url = 'https://web.whatsapp.com/send?phone=' + str(number) + '&text=' + urllib.parse.quote(message)
        self.driver.get(url)  # Navigate to WhatsApp Web URL
        WhatsappCore.printf(f'Opening {url}')  # Use WhatsappCore for static method call

    def set_message_type(self, message_type):
        """
        Sets the message type using the Message instance.

        Args:
            message_type (str): The type of message to be sent.
        """
        self.message_instance.set_message_type(message_type)

    def check_is_driver_available(self):
        """
        Checks if the Selenium WebDriver instance is available.

        Returns:
            bool: True if driver is available, False otherwise.
        """
        if not self.is_driver_available:
            DialogBox().show_confirmation_dialog("Driver is not available so open the whatsapp first.")
            return False
        return True

    def check_csv_path_available(self):
        """
        Checks if a CSV file path is specified.

        Returns:
            bool: True if CSV path is available, False otherwise.
        """
        if not self.csv_path:
            DialogBox().show_confirmation_dialog("csv file is not available Please select the csv fie first.")
            return False
        return True

    def check_image_path_available(self):
        """
        Checks if an image file path is specified when needed.

        Returns:
            bool: True if image path is available (when required), False otherwise.
        """
        if not self.image_path:
            DialogBox().show_confirmation_dialog("image file is not available Please select the fie first.")
            return False
        return True

    def send_messages(self):
        """
        Initiates the process of sending WhatsApp messages.

        Validates inputs, prompts user confirmation, and then calls the appropriate
        method to send messages based on the selected message type.
        """
        if not self._validate_inputs():  # Validate inputs before sending
            return

        self.dialogBox_instance.show_confirmation_dialog(
            "Are you sure You want to send Message?")  # Confirmation dialog
        if self.dialogBox_instance.user_response == True:
            WhatsappCore.printf('Sending messages')  # Use WhatsappCore for static method call
            self.check_message_type_and_send_message()  # Delegate message sending based on type
        else:
            WhatsappCore.printf("User canceled the Process")  # Use WhatsappCore for static method call

    def _validate_inputs(self):
        """
        Validates necessary inputs before sending messages.

        Returns:
            bool: True if all validations pass, False otherwise.
        """
        if not self.check_is_driver_available():  # Check driver availability
            return False
        if self.current_message_selection is None:  # Check message type selection
            self.dialogBox_instance.show_confirmation_dialog("Please Select the valid option before sending")
            return False
        if not self.check_csv_path_available():  # Check CSV file path availability
            return False
        if self.current_message_selection in [self.message_types[2], self.message_types[3],
                                              self.message_types[4]]:  # Check image path for image message types
            if not self.check_image_path_available():
                return False
        return True

    def show_error_dialog_box(self, message):
        """
        Displays an error dialog box with the given message.

        Args:
            message (str): The error message to display.
        """
        self.dialogBox_instance.show_confirmation_dialog(str(message))

    def save_cookies(self):
        """
        Saves browser cookies and local storage to files for session persistence.
        """
        if self.is_driver_available:
            self._save_session_cookies()  # Delegate cookie saving
            WhatsappCore.printf('saved the cookies')  # Use WhatsappCore for static method call

    def _save_session_cookies(self):
        """
        Helper method to save cookies and local storage to files.
        """
        with open("whatsapp_cookies.pkl", "wb") as file:  # Save cookies using pickle
            pickle.dump(self.driver.get_cookies(), file)
        local_storage = self.driver.execute_script("return window.localStorage;")  # Get local storage from browser
        with open("whatsapp_local_storage.json", "w") as file:  # Save local storage as JSON
            json.dump(local_storage, file)

    def load_cookies(self):
        """
        Loads browser cookies and local storage from files to restore session.
        """
        self._load_session_cookies()  # Delegate cookie loading
        WhatsappCore.printf('loaded the cookies')  # Use WhatsappCore for static method call

    def _load_session_cookies(self):
        """
        Helper method to load cookies and local storage from files.
        """
        try:
            with open("whatsapp_cookies.pkl", "rb") as file:  # Load cookies from pickle file
                cookies = pickle.load(file)
                for cookie in cookies:
                    self.driver.add_cookie(cookie)  # Add cookies to WebDriver
            WhatsappCore.printf('loaded the cookies from pkl file')  # Use WhatsappCore for static method call
        except FileNotFoundError:
            WhatsappCore.printf(
                "Cookies file not found. Skipping cookie loading.")  # Use WhatsappCore for static method call

        try:
            with open("whatsapp_local_storage.json", "r") as file:  # Load local storage from JSON file
                local_storage = json.load(file)
                for key, value in local_storage.items():
                    self.driver.execute_script(
                        f"window.localStorage.setItem('{key}', '{value}');")  # Set local storage in browser
            WhatsappCore.printf('loaded local storage from json')  # Use WhatsappCore for static method call
        except FileNotFoundError:
            WhatsappCore.printf(
                "Local storage file not found. Skipping local storage loading.")  # Use WhatsappCore for static method call

    def invalid_number_handler(self, number):
        """
        Handles scenarios where a phone number is identified as invalid by WhatsApp.

        Args:
            number (str): The phone number identified as invalid.
        """
        from .whatsapp_data_handler import WhatsappDataHandler  # Local import to avoid circular dependency

        data_handler = WhatsappDataHandler()  # Instance of data handler class
        try:
            contains_invalid_modal_text = self.button_locator_instance.does_page_contains_text(
                self.driver, self.wait_time, self.button_locator_instance.invalid_modal_text)  # Check for invalid modal
            if contains_invalid_modal_text:
                self.invalid_number_df = data_handler.add_details_to_data_frame(self.invalid_number_df,
                                                                                number)  # Add to invalid numbers DataFrame
                WhatsappCore.printf("Invalid Numbers")  # Use WhatsappCore for static method call
                WhatsappCore.printf(self.invalid_number_df)  # Use WhatsappCore for static method call
                try:  # Try to click 'Okay' button on the modal
                    okay_button = self.button_locator_instance.x_path_locator(
                        self.driver, self.wait_time, self.button_locator_instance.invalid_modal_okay_button_value)
                except Exception as e:
                    WhatsappCore.printf("cannot click on invalid number modal okay button",
                                        e)  # Use WhatsappCore for static method call
                else:
                    okay_button.click()  # Click 'Okay' to close the modal
                    WhatsappCore.printf("closed the invalid number modal")  # Use WhatsappCore for static method call
            else:  # If invalid modal is not found
                self.not_sent_number_df = data_handler.add_details_to_data_frame(self.not_sent_number_df,
                                                                                 number)  # Add to not-sent numbers DataFrame
                WhatsappCore.printf("Not sent Numbers")  # Use WhatsappCore for static method call
                WhatsappCore.printf(self.not_sent_number_df)  # Use WhatsappCore for static method call
        except Exception as e:
            WhatsappCore.printf("Error in invalid_number_handler", e)  # Use WhatsappCore for static method call

    def check_message_type_and_send_message(self):
        """
        Orchestrates message sending based on the selected message type.
        """
        from .contact_numbers import ContactNumber  # Local import to avoid circular dependency

        contacts = self.get_contacts()  # Load contacts from CSV
        message_type = self.current_message_selection  # Get selected message type
        message_types = self.message_types  # Get message types list (for easier access)

        if message_type in [message_types[0], message_types[1]]:  # Text message types
            self._send_text_messages(contacts)  # Delegate to text message sending
        elif message_type in [message_types[2], message_types[3], message_types[4]]:  # Image message types
            self._send_image_messages(contacts)  # Delegate to image message sending

    def _send_text_messages(self, contacts):
        """
        Sends text-based messages to contacts.

        Args:
            contacts (pandas.DataFrame): DataFrame containing contact details and messages.
        """
        from .whatsapp_data_handler import WhatsappDataHandler  # Local import

        data_handler = WhatsappDataHandler()  # Instance of data handler
        static_message = contacts['Message'][
            0] if not contacts.empty and 'Message' in contacts else ""  # Default message
        for index, row in contacts.iterrows():  # Iterate over contacts
            number = row['Contact No']  # Get phone number
            message = row['Message'] if 'Message' in row else static_message  # Get message (specific or static)
            message_to_send = ""  # Initialize message to send

            if self.current_message_selection == self.message_types[0]:  # "Same message" type
                message_to_send = self.custom_message if self.custom_message else static_message  # Use custom or static message
                WhatsappCore.printf(
                    f"Row {index}: Contact No = {number}, Message = {message_to_send}")  # Use WhatsappCore for static method call
            else:  # "Different messages" type
                message_to_send = message  # Use message from CSV
                WhatsappCore.printf(
                    f"Row {index}: Contact No = {number}, Message = {message_to_send}")  # Use WhatsappCore for static method call

            self.open_contact(number, message_to_send)  # Open chat with contact
            sent_successfully = self._click_send_button(number)  # Click send button and check for success

            if sent_successfully:  # If message was sent successfully
                sleep(int(self.window_instance.config_instance.sleep_time_spin_box))  # Wait before next message
                WhatsappCore.printf(f"Message is sent to the {number}")  # Use WhatsappCore for static method call
                self.sent_numbers_df = data_handler.add_details_to_data_frame(self.sent_numbers_df,
                                                                              number)  # Add to sent numbers report

    def _send_image_messages(self, contacts):
        """
        Sends image/file messages to contacts.

        Args:
            contacts (pandas.DataFrame): DataFrame containing contact details and messages.
        """
        from .whatsapp_data_handler import WhatsappDataHandler  # Local import

        data_handler = WhatsappDataHandler()  # Instance of data handler
        empty_message = ""  # Empty message for image-only messages
        static_message = contacts['Message'][
            0] if not contacts.empty and 'Message' in contacts else ""  # Default message
        for index, row in contacts.iterrows():  # Iterate over contacts
            number = row['Contact No']  # Get contact number
            message = row['Message'] if 'Message' in row else static_message  # Get message (specific or static)
            message_to_send = ""  # Initialize message to send

            if self.current_message_selection == self.message_types[2]:  # "Send Image" type
                message_to_send = empty_message  # No text message for image-only
                WhatsappCore.printf(
                    f"Row {index}: Contact No = {number}, Message = {empty_message}, image attachment={self.image_path}")  # Use WhatsappCore for static method call
            elif self.current_message_selection == self.message_types[3]:  # "Send Image with Same Message"
                message_to_send = self.custom_message if self.custom_message else static_message  # Custom or static message
                WhatsappCore.printf(
                    f"Row {index}: Contact No = {number}, Message = {message_to_send}")  # Use WhatsappCore for static method call
            elif self.current_message_selection == self.message_types[4]:  # "Send Image with Different Message"
                message_to_send = message  # Message from CSV
                WhatsappCore.printf(
                    f"Row {index}: Contact No = {number}, Message = {message_to_send}, image attachment = {self.image_path}")  # Use WhatsappCore for static method call

            self.open_contact(number, message_to_send)  # Open chat with contact
            attachment_button_clicked = self._click_attachment_button(number)  # Click attachment button

            if attachment_button_clicked:  # If attachment button click was successful
                is_file_attachment = (self.current_message_selection == self.message_types[
                    5])  # Check if it's file attachment type
                attachment_uploaded = self._upload_attachment(number, is_file_attachment)  # Upload attachment

                if attachment_uploaded:  # If attachment upload was successful
                    send_button_clicked = self._click_media_send_button(number)  # Click media send button

                    if send_button_clicked:  # If media send button click was successful
                        sleep(
                            int(self.window_instance.config_instance.upload_time_spin_box))  # Wait for upload to complete
                        self.sent_numbers_df = data_handler.add_details_to_data_frame(self.sent_numbers_df,
                                                                                      number)  # Add to sent numbers report

    def _click_send_button(self, number):
        """
        Clicks the send button for text messages.

        Args:
            number (str): Contact number associated with the message.

        Returns:
            bool: True if send button was clicked, False otherwise (e.g., invalid number).
        """
        try:
            send_button = self.button_locator_instance.aria_text_locator(
                self.driver, self.wait_time,
                self.window_instance.config_instance.send_message_button_text)  # Locate send button
        except:
            self.invalid_number_handler(number)  # Handle invalid number scenario
            return False  # Indicate send failure
        else:
            send_button.click()  # Click send button
            return True  # Indicate send success

    def _click_attachment_button(self, number):
        """
        Clicks the attachment button (plus icon).

        Args:
            number (str): Contact number associated with the message.

        Returns:
            bool: True if button was clicked, False otherwise (e.g., invalid number).
        """
        try:
            attachment_button = self.button_locator_instance.x_path_locator(
                self.driver, self.wait_time,
                self.window_instance.config_instance.attachment_button_val)  # Locate attachment button
            sleep(int(self.window_instance.config_instance.sleep_time_spin_box))  # Wait for button to be interactable
        except:
            self.invalid_number_handler(number)  # Handle invalid number scenario
            return False  # Indicate click failure
        else:
            attachment_button.click()  # Click attachment button
            return True  # Indicate click success

    def _upload_attachment(self, number, is_file_attachment):
        """
        Uploads an image or file attachment.

        Args:
            number (str): Contact number associated with the message.
            is_file_attachment (bool): True if uploading a file, False for image.

        Returns:
            bool: True if upload was initiated, False otherwise (e.g., button not found).
        """
        try:
            accept_value = self.window_instance.config_instance.file_attachment_accept_value if is_file_attachment else self.window_instance.config_instance.image_attachment_accept_value
            attachment_input_button = self.button_locator_instance.find_element_by_attributes(
                self.driver, self.wait_time, accept_value)  # Locate attachment input
        except Exception as e:
            WhatsappCore.printf(
                f"Cannot find attachment uploading button: {e}")  # Use WhatsappCore for static method call
            return False  # Indicate upload initiation failure
        else:
            attachment_input_button.send_keys(self.image_path)  # Send file path to input
            sleep(int(self.window_instance.config_instance.sleep_time_spin_box))  # Wait for upload to start
            return True  # Indicate upload initiation success

    def _click_media_send_button(self, number):
        """
        Clicks the send button after uploading media (image/file).

        Args:
            number (str): Contact number associated with the message.

        Returns:
            bool: True if button was clicked, False otherwise (e.g., button not found).
        """
        try:
            send_button = self.button_locator_instance.x_path_locator(
                self.driver, self.wait_time,
                self.window_instance.config_instance.send_button_value)  # Locate media send button
            send_button.click()  # Click media send button
            return True  # Indicate click success
        except:
            WhatsappCore.printf(
                "cannot find send button after uploading the attachment")  # Use WhatsappCore for static method call
            return False  # Indicate click failure