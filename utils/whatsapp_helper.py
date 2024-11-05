from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from time import sleep
import pandas
import urllib
from .message_type import Message
from .ui_helper import MessageDialog,DialogBox
from .contact_numbers import ContactNumber
import pickle
import json
from .button_locators import Locators
import pandas as pd
from .config_helper import Config
class Whatsapp():
    debug = True
    def __init__(self,window_instance):
        self.window_instance = window_instance
        self.driver = False
        self.message_instance = Message()
        self.is_verified = False
        self.is_driver_available = False
        self.custom_message = None
        self.message_types = ["Same Messages for everyone", "Different Messages for Each", "Send Image","Send Image with Same Message","Send Image with Different Message","Send File"]
        self.current_message_selection = None
        self.csv_path =  None
        self.image_path = None
        self.dialogBox_instance = DialogBox()
        self.wait_time = self.window_instance.config_instance.wait_time_spin_box
        self.button_locator_instance = Locators()
        self.sent_numbers_df = pd.DataFrame(columns=['number'])
        self.invalid_number_df = pd.DataFrame(columns=['number'])
        self.not_sent_number_df = pd.DataFrame(columns=['number'])

    def printf(*args):
        if Whatsapp.debug == True:
            print(*args)

    def open_whatsapp(self):

        self.driver = webdriver.Chrome()

        # Set up Chrome options to connect to the debugging port
        # chrome_options = Options()
        # chrome_options.debugger_address = "localhost:9222"
        # # Initialize the driver without starting a new browser instance
        # self.driver = webdriver.Chrome(service=Service(), options=chrome_options)

        self.driver.get('https://web.whatsapp.com')
        self.is_driver_available = True


    def do_scan_QR_code(self):
        if not self.is_verified:
            dialog = MessageDialog("Please Verify the QR code")
            dialog.exec()  # Show the dialog
    
    def open_contact(self,number,message):
        url = 'https://web.whatsapp.com/send?phone=' + str(number) + '&text=' + urllib.parse.quote(message)
        self.driver.get(url)
        self.printf(f'Opening {url}')
    
    def set_message_type(self,message_type):
        self.message_instance.set_message_type(message_type)

    def get_contacts(self):
        try:
            df = ContactNumber.load_csv_to_dataframe(self.csv_path)
        except Exception as e:
            self.show_error_dialog_box(e)
            return False
        else:
            return df
    
    def check_is_driver_available(self):
        if not self.is_driver_available:
            DialogBox().show_confirmation_dialog("Driver is not available so open the whatsapp first.")
            return False
        return True

    def check_csv_path_available(self):
        if not self.csv_path:
            DialogBox().show_confirmation_dialog("csv file is not available Please select the csv fie first.")
            return False
        return True
        
    def check_image_path_available(self):
        if not self.image_path:
            DialogBox().show_confirmation_dialog("image file is not available Please select the fie first.")
            return False
        return True
    

    def send_messages(self):
        response = self.check_is_driver_available()
        if not response:
            return
        
        if self.current_message_selection == None:
            self.dialogBox_instance.show_confirmation_dialog("Please Select the valid option before sending")
            return 
        
        response = self.check_csv_path_available()
        if not response:
            return 
        
        if self.current_message_selection == self.message_types[2] or self.current_message_selection == self.message_types[3] or self.current_message_selection == self.message_types[4]:
            response = self.check_image_path_available()
            if not response:
                return
        
        if self.is_driver_available:
            self.dialogBox_instance.show_confirmation_dialog("Are you sure You want to send Message?")
            if  self.dialogBox_instance.user_response == True:    
                # self.printf('Sending messages')
                # check the message type before sending the message
                self.check_message_type_and_send_message()

            else:
                self.printf("User canceled the Process")
        else:
            self.printf("driver not available")


    def show_error_dialog_box(self,message):
         self.dialogBox_instance.show_confirmation_dialog(str(message))

    def save_cookies(self):
        if self.is_driver_available:
            # Save cookies to a file
            with open("whatsapp_cookies.pkl", "wb") as file:
                pickle.dump(self.driver.get_cookies(), file)
            local_storage = self.driver.execute_script("return window.localStorage;")
            with open("whatsapp_local_storage.json", "w") as file:
                json.dump(local_storage, file)
            self.printf('saved the cookies')

    def load_cookies(self):
        with open("whatsapp_cookies.pkl", "rb") as file:
            cookies = pickle.load(file)
            for cookie in cookies:
                self.driver.add_cookie(cookie)
            self.printf('loaded the cookies')

        # Load local storage from the JSON file
        with open("whatsapp_local_storage.json", "r") as file:
            local_storage = json.load(file)
            for key, value in local_storage.items():
                self.driver.execute_script(f"window.localStorage.setItem('{key}', '{value}');")
        
    def add_details_to_data_frame(self,df,data):
        # columns = ['number', 'reason']
        # data = [123, "Sample reason"]
        self.printf("adding the row to the dataframe")
        new_row = pd.DataFrame([data], columns=['number'])
        temp_df = pd.concat([df, new_row], ignore_index=True)
        return temp_df

    def invalid_number_handler(self,number):
        try:
            invalid_modal_text = "Phone number shared via url is invalid."
            contains = self.button_locator_instance.does_page_contains_text(self.driver,self.wait_time,self.button_locator_instance.invalid_modal_text)
            if contains:
                # store the invalid number in the data frame
                self.invalid_number_df = self.add_details_to_data_frame(self.invalid_number_df,number)
                self.printf("Invalid Numbers")
                self.printf(self.invalid_number_df)
                # skip the current number and go to the next
                # optionally click on okay button
                try:
                    button = self.button_locator_instance.x_path_locator(self.driver,self.wait_time,self.button_locator_instance.invalid_modal_okay_button_value)
                except Exception as e:
                    self.printf("can not click on invalid number modal okay button",e)
                else:
                    button.click()
                    self.printf("closed the invalid number modal")
            else:
                # number is not determined as invalid number but still we will add in not sent
                self.not_sent_number_df = self.add_details_to_data_frame(self.not_sent_number_df,number)
                self.printf("Not sent Numbers")
                self.printf(self.not_sent_number_df)
        except Exception as e:
            self.printf("Error while finding invalid, try catch block",e)

    def check_message_type_and_send_message(self):
        contacts = self.get_contacts()
        if self.current_message_selection == self.message_types[0] or self.current_message_selection == self.message_types[1]:
            static_message = contacts['Message'][0]
            for index, row in contacts.iterrows():
                number = row['Contact No']
                message = row['Message']
                if self.current_message_selection == self.message_types[0]:
                    if self.custom_message:
                        self.printf(f"Row {index}: Contact No = {row['Contact No']}, Message = custom_message_obj")        
                        self.open_contact(number,self.custom_message)
                    else:
                        self.printf(f"Row {index}: Contact No = {row['Contact No']}, Message = {static_message}")        
                        self.open_contact(number,static_message)
                else:
                    self.printf(f"Row {index}: Contact No = {row['Contact No']}, Message = {row['Message']}")        
                    self.open_contact(number,message)
                try:
                    button = self.button_locator_instance.aria_text_locator(self.driver,self.wait_time,self.window_instance.config_instance.send_message_button_text)
                except:
                    self.invalid_number_handler(number)
                else:
                    button.click()
                    sleep(int(self.window_instance.config_instance.sleep_time_spin_box))
                    self.printf(f"Message is sent to the {number}")
                    self.sent_numbers_df = self.add_details_to_data_frame(self.sent_numbers_df,number)


        if self.current_message_selection == self.message_types[2] or self.current_message_selection == self.message_types[3] or self.current_message_selection == self.message_types[4]:
            empty_message = ""
            static_message = contacts['Message'][0]
            for index, row in contacts.iterrows():
                number = row['Contact No']
                message = row['Message']
                if self.current_message_selection == self.message_types[2]:
                    self.printf(f"Row {index}: Contact No = {row['Contact No']}, Message = {empty_message}, image attachment={self.image_path}")        
                    self.open_contact(number,empty_message)
                elif self.current_message_selection == self.message_types[3]:
                     if self.custom_message:
                        self.printf(f"Row {index}: Contact No = {row['Contact No']}, Message = custom_message_obj")        
                        self.open_contact(number,self.custom_message)
                     else:
                        self.printf(f"Row {index}: Contact No = {row['Contact No']}, Message = {static_message}")        
                        self.open_contact(number,static_message)
                else:
                    self.printf(f"Row {index}: Contact No = {row['Contact No']}, Message = {row['Message']}, image attachment = {self.image_path}")        
                    self.open_contact(number,message)
                try:
                    attachment_button_val = "//span[@data-icon='plus']"
                    attachment_button = self.button_locator_instance.x_path_locator(self.driver,self.wait_time,self.window_instance.config_instance.attachment_button_val)
                    sleep(int(self.window_instance.config_instance.sleep_time_spin_box))
                except:                    
                    self.invalid_number_handler(number)
                else:
                    attachment_button.click()
                    # image_box_val = "//input[@accept='image/*,video/mp4,video/3gpp,video/quicktime']"
                    image_attachment_accept_value = "image/*,video/mp4,video/3gpp,video/quicktime"
                    file_attachment_accept_value = "*"
                    try:
                        if self.message_types[4]:
                            button = self.button_locator_instance.find_element_by_attributes(self.driver,self.wait_time,self.window_instance.config_instance.image_attachment_accept_value)
                        else:
                            button = self.button_locator_instance.find_element_by_attributes(self.driver,self.wait_time,self.window_instance.config_instance.file_attachment_accept_value)
                        # button.send_keys(r"C:\Users\darsh\Desktop\nisarg chori\test.zip")
                    except Exception as e:
                        print("cannot find attachment uploading button")
                    else:
                        button.send_keys(self.image_path)
                        sleep(int(self.window_instance.config_instance.sleep_time_spin_box))
                        # send_button_value = f"//*[@data-icon='send']"
                        send_button = self.button_locator_instance.x_path_locator(self.driver,self.wait_time,self.window_instance.config_instance.send_button_value)
                        send_button.click()
                        sleep(int(self.window_instance.config_instance.upload_time_spin_box))