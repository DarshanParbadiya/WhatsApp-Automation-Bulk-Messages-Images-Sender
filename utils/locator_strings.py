# utils/locator_strings.py
# Locator Strings for UI Elements

class LocatorStrings():
    """
    Class to hold locator strings (XPath, CSS selectors, etc.) for UI elements.

    This centralizes the storage of locators, making it easier to manage and update
    them in one place. This class is instantiated in classes that need to access these locators.

    Refactored: Locator strings were moved from 'utils/button_locators.py' to this file
    to improve modularity and separation of concerns.
    """
    def __init__(self):
        """
        Initializes the LocatorStrings class with default locator values.
        """
        # Locator for the attachment button (plus icon)
        self.attachment_button_val = "//span[@data-icon='plus']"
        # Locator for the image/video file input box (potentially unused, kept for possible future use)
        # self.image_box_val = "//input[@accept='image/*,video/mp4,video/3gpp,video/quicktime']"
        # Accept attribute value for image and video attachments
        self.image_attachment_accept_value = "image/*,video/mp4,video/3gpp,video/quicktime"
        # Accept attribute value for file attachments (all types)
        self.file_attachment_accept_value = "*"
        # Text content of the "Send" message button
        self.send_message_button_text = "Send"
        # Locator for the "Send" button (send icon)
        self.send_button_value = f"//*[@data-icon='send']"
        # Text content of the invalid phone number modal dialog
        self.invalid_modal_text = "Phone number shared via url is invalid."
        # Class attribute for the "Okay" button in the invalid phone number modal
        self.invalid_modal_okay_button_class ="x889kno x1a8lsjc xbbxn1n xxbr6pl x1n2onr6 x1rg5ohu xk50ysn x1f6kntn xyesn5m x1z11no5 xjy5m1g x1mnwbp6 x4pb5v6 x178xt8z xm81vs4 xso031l xy80clv x13fuv20 xu3j5b3 x1q0q8m5 x26u7qi x1v8p93f xogb00i x16stqrj x1ftr3km x1hl8ikr xfagghw x9dyr19 x9lcvmn xbtce8p x14v0smp xo8ufso xcjl5na x1k3x3db xuxw1ft xv52azi"
        # Locator for the "Okay" button in the invalid phone number modal
        self.invalid_modal_okay_button_value = f"//*[@class='{self.invalid_modal_okay_button_class}']"