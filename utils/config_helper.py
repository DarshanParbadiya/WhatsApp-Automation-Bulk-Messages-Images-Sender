# utils/config_helper.py
import configparser


class Config():
    """
    Handles configuration settings for the WhatsApp automation tool using a config.ini file.

    This class is responsible for:
        - Reading configuration values from 'config.ini' at initialization.
        - Providing methods to set and save configuration values back to 'config.ini'.
        - Loading configuration values into the UI elements of the application window.

    Refactored from original 'utils/config_helper.py': Docstrings are added for better documentation,
    and methods are organized for clarity.

    Backward Compatibility: This class remains fully backward compatible as existing code that
    instantiates and uses 'Config' or calls its methods will continue to function
    without any changes to its API.
    """


    def __init__(self, window_instance):
        """
        Initializes the Config instance by reading settings from 'config.ini'.

        Args:
            window_instance: An instance of the main application window (e.g., MySideBar),
                             used to access and update UI elements with config values.
        """
        self.window_instance = window_instance
        self.config = configparser.ConfigParser()  # Initialize config parser
        self.config.read('config.ini')  # Read configuration from 'config.ini'
        # self.invalid_modal_okay_button_class = None # Removed - not directly used as class attribute


    def set_config_values(self):
        """
        Sets configuration values as attributes of the Config instance.

        Reads values from the 'config' parser object and assigns them to instance attributes
        for easy access within the application. These attributes correspond to different
        sections in the 'config.ini' file (e.g., 'Buttons', 'Attachments', 'Modals', 'Timers', 'Chrome').
        """
        # Access values from each section using config parser and set as instance attributes
        self.attachment_button_val = self.config['Buttons']['attachment_button_val']
        self.send_button_value = self.config['Buttons']['send_button_value']
        self.send_message_button_text = self.config['Buttons']['send_message_button_text']

        self.image_attachment_accept_value = self.config['Attachments']['image_attachment_accept_value']
        self.file_attachment_accept_value = self.config['Attachments']['file_attachment_accept_value']

        self.invalid_modal_text = self.config['Modals']['invalid_modal_text']
        self.invalid_modal_okay_button_class = self.config['Modals'][
            'invalid_modal_okay_button_class']  # Note: Class name is stored as string

        self.wait_time_spin_box = self.config['Timers']['wait']
        self.upload_time_spin_box = self.config['Timers']['upload_wait']
        self.sleep_time_spin_box = self.config['Timers']['sleep_time']
        self.single_instance = self.config['Chrome']['single_instance']

        # Debug prints - can be removed in production
        # print(attachment_button_val)
        # print(send_button_value)
        # print(send_message_button_text)
        # print(image_attachment_accept_value)
        # print(file_attachment_accept_value)
        # print(invalid_modal_text)
        # print(invalid_modal_okay_button_class)


    def save_config(self):
        """
        Saves configuration values from UI elements back to the 'config.ini' file.

        Retrieves values from the UI elements in 'window_instance' (e.g., text edits, spin boxes)
        and updates the corresponding sections and keys in the 'config' parser object.
        Finally, writes these updated settings back to the 'config.ini' file.
        """
        # Update config parser with values from UI elements
        self.config['Buttons']['attachment_button_val'] = self.window_instance.attachment_button_val.toPlainText()
        self.config['Buttons']['send_button_value'] = self.window_instance.send_button_value.toPlainText()
        self.config['Buttons']['send_message_button_text'] = self.window_instance.send_message_button_text.toPlainText()

        self.config['Attachments'][
            'image_attachment_accept_value'] = self.window_instance.image_attachment_accept_value.toPlainText()
        self.config['Attachments'][
            'file_attachment_accept_value'] = self.window_instance.file_attachment_accept_value.toPlainText()

        self.config['Modals']['invalid_modal_text'] = self.window_instance.invalid_modal_text.toPlainText()
        self.config['Modals'][
            'invalid_modal_okay_button_class'] = self.window_instance.invalid_modal_okay_button_class.toPlainText()

        # Timers section - values from spin boxes are converted to strings before saving
        self.config['Timers']['wait'] = str(self.window_instance.wait_time_spin_box.value())
        self.config['Timers']['upload_wait'] = str(self.window_instance.upload_time_spin_box.value())
        self.config['Timers']['sleep_time'] = str(self.window_instance.sleep_time_spin_box.value())

        # Write changes back to 'config.ini' file
        with open('config.ini', 'w') as configfile:
            self.config.write(configfile)


    def load_config_values(self):
        """
        Loads configuration values from the 'config.ini' file into the application's UI elements.

        Reads configuration values from the 'config' parser object and sets the text/value
        of corresponding UI elements in 'window_instance'. This function is typically used
        to initialize the UI with saved configuration settings when the application starts.
        """
        # Load values from config parser
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

        # Set loaded values to UI elements in window_instance
        self.window_instance.invalid_modal_text.setPlainText(
            str(invalid_modal_text))  # Set text for invalid modal text edit
        self.window_instance.invalid_modal_okay_button_class.setPlainText(
            str(invalid_modal_okay_button_class))  # Set text for invalid modal button class text edit
        self.window_instance.attachment_button_val.setPlainText(
            str(attachment_button_val))  # Set text for attachment button value text edit
        self.window_instance.send_message_button_text.setPlainText(
            str(send_message_button_text))  # Set text for send message button text edit
        self.window_instance.send_button_value.setPlainText(
            str(send_button_value))  # Set text for send button value text edit
        self.window_instance.image_attachment_accept_value.setPlainText(
            str(image_attachment_accept_value))  # Set text for image attachment accept value text edit
        self.window_instance.file_attachment_accept_value.setPlainText(
            str(file_attachment_accept_value))  # Set text for file attachment accept value text edit
        self.window_instance.wait_time_spin_box.setValue(int(wait_time_spin_box))  # Set value for wait time spin box
        self.window_instance.upload_time_spin_box.setValue(
            int(upload_time_spin_box))  # Set value for upload wait time spin box
        self.window_instance.sleep_time_spin_box.setValue(int(sleep_time_spin_box))  # Set value for s