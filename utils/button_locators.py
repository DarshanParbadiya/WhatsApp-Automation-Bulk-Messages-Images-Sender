# utils/button_locators.py
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

# Refactored and Locator Strings Moved to utils/locator_strings.py for Modularity

class Locators():
    """
    Class for storing and accessing UI element locators using Selenium.

    This class provides methods to locate web elements on a page using various strategies
    (XPath, aria-label, text content, attributes). It utilizes WebDriverWait for handling
    asynchronous page loading and element availability.

    Refactored: Locator strings are now moved to 'utils/locator_strings.py' to improve
    modularity and separation of concerns. This class now primarily focuses on providing
    methods to *use* these locators.

    Backward Compatibility: This class remains backward compatible as existing code that
    instantiates and uses 'Locators' will continue to function without modification.
    """
    def __init__(self):
        """
        Initializes the Locators class.

        Loads locator string values from 'utils.locator_strings' module.
        """
        from utils.locator_strings import LocatorStrings # Import inside __init__ to avoid circular dependency issues if any

        self.locator_strings = LocatorStrings() # Instance of LocatorStrings to access string values

        # Access locator strings from LocatorStrings instance
        self.attachment_button_val = self.locator_strings.attachment_button_val
        # self.image_box_val = self.locator_strings.image_box_val # Potentially unused, kept for compatibility
        self.image_attachment_accept_value = self.locator_strings.image_attachment_accept_value
        self.file_attachment_accept_value = self.locator_strings.file_attachment_accept_value
        self.send_message_button_text = self.locator_strings.send_message_button_text
        self.send_button_value = self.locator_strings.send_button_value
        self.invalid_modal_text = self.locator_strings.invalid_modal_text
        self.invalid_modal_okay_button_class = self.locator_strings.invalid_modal_okay_button_class
        self.invalid_modal_okay_button_value = self.locator_strings.invalid_modal_okay_button_value


    def aria_text_locator(self, driver, wait_time, label_value):
        """
        Locates a button element by its 'aria-label' attribute.

        Uses WebDriverWait to wait for the element to be present on the page.

        Args:
            driver: Selenium WebDriver instance.
            wait_time (int): Maximum time to wait for the element (in seconds).
            label_value (str): The 'aria-label' value of the button to locate.

        Returns:
            WebElement or False: Returns the WebElement if found, otherwise returns False.
        """
        try:
            button = WebDriverWait(driver, wait_time).until(EC.presence_of_element_located((By.XPATH, f'//button[@aria-label="{label_value}"]')))
        except:
            print(f"Button with aria-label '{label_value}' not found")
            return False
        else:
            return button


    def x_path_locator(self, driver, wait_time, path):
        """
        Locates an element by its XPath.

        Uses WebDriverWait to wait for the element to be present on the page.

        Args:
            driver: Selenium WebDriver instance.
            wait_time (int): Maximum time to wait for the element (in seconds).
            path (str): XPath expression to locate the element.

        Returns:
            WebElement or False: Returns the WebElement if found, otherwise returns False.
        """
        try:
            button = WebDriverWait(driver, wait_time).until(EC.presence_of_element_located((By.XPATH, path)))
        except:
            print(f"Element with XPath '{path}' not found on the page")
            return False
        else:
            print(f'XPath "{path}" element found on the web page')
            return button


    def does_page_contains_text(self, driver, wait_time, label):
        """
        Checks if a page contains an element with specific text content.

        Uses WebDriverWait to wait for an element containing the given text to be present.

        Args:
            driver: Selenium WebDriver instance.
            wait_time (int): Maximum time to wait for the element (in seconds).
            label (str): The text content to search for within the page.

        Returns:
            bool: Returns True if an element with the text is found, otherwise False.
        """
        try:
            element = WebDriverWait(driver, wait_time).until(
                EC.presence_of_element_located((By.XPATH, f"//*[contains(text(), '{label}')]"))
            )
        except:
            print(f"Text '{label}' not found on the page")
            return False
        else:
            if element:
                print(f"The text '{label}' is present on the page.") # Confirmation message - can be removed in production
            return True


    def find_element_by_attributes(self, driver, wait_time, accept_value):
        """
        Finds an input element by its 'accept' attribute value.

        This is specifically useful for finding file or image input elements based on
        the types of files they accept.

        Args:
            driver: Selenium WebDriver instance.
            wait_time (int): Maximum time to wait for the element (in seconds).
            accept_value (str): The 'accept' attribute value to search for (e.g., "image/*", "*").

        Returns:
            WebElement or None: Returns the WebElement if found, otherwise None.
        """
        try:
            element = driver.find_element(By.XPATH, f"//input[@accept='{accept_value}']")
        except Exception as e:
            print(f"Attachment input element with accept value '{accept_value}' not found: {e}")
            return None
        else:
            return element