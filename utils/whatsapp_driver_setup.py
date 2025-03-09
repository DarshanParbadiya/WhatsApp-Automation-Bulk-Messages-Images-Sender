# utils/whatsapp_driver_setup.py
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from helper import ChromeLauncher # Assuming helper.py is in the same utils directory or accessible. If it is outside utils, adjust import path.

class WhatsappDriverSetup:
    """
    Class to encapsulate Selenium WebDriver setup for WhatsApp Web automation.

    This class provides a static method 'setup_driver' to configure and initialize
    a Chrome WebDriver instance, handling both single-instance and new-instance browser modes.

    Refactored from 'utils/whatsapp_helper.py': Driver setup logic is moved to this class
    to improve modularity and separate concerns related to driver management.

    Backward Compatibility: This class is used internally within 'utils/whatsapp_helper.py' and
    does not directly affect backward compatibility of the 'Whatsapp' class API.
    """
    @staticmethod
    def setup_driver(single_instance=False):
        """
        Sets up and returns a Selenium Chrome WebDriver instance.

        Configures the WebDriver based on the 'single_instance' flag. If True, it attempts
        to connect to an existing Chrome instance in debug mode. If False, it launches a new
        Chrome browser instance.

        Args:
            single_instance (bool, optional): If True, attempts to connect to an existing Chrome
                                              instance (for single instance mode). Defaults to False.

        Returns:
            webdriver.Chrome: A configured Selenium Chrome WebDriver instance.
        """
        if single_instance:
            WhatsappDriverSetup.printf('single Instance is on') # Use class name to call static method
            chrome_options = Options() # Initialize Chrome options
            chrome_options.debugger_address = "localhost:9222" # Set debugger address for connecting to existing instance
            driver = webdriver.Chrome(service=Service(), options=chrome_options) # Initialize driver to connect to existing instance
        else:
            driver = webdriver.Chrome() # Launch a new Chrome browser instance
        return driver

    @staticmethod
    def printf(*args):
        """
        Prints debug messages. (Static method for potential use within this class)

        For simplicity in this module, the debug check is removed but can be added back if needed.
        This method can be moved to a more general utils file if used across multiple modules.
        """
        print(*args)