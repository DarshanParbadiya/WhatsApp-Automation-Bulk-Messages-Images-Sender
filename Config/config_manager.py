# whatsapp_automation/config/config_manager.py
import configparser
import os

class ConfigManager:
    _instance = None  # Singleton instance

    def __new__(cls, config_file="config/config.ini"):
        if cls._instance is None:
            cls._instance = super(ConfigManager, cls).__new__(cls)
            cls._instance.config_file = config_file
            cls._instance.config = configparser.ConfigParser()
            cls._instance.load_config()
        return cls._instance

    def load_config(self):
        if os.path.exists(self.config_file):
            self.config.read(self.config_file)
        else:
            self.create_default_config()

    def create_default_config(self):
        self.config['Database'] = {'host': 'newhost.example.com', 'port': '5432', 'username': 'user', 'password': 'pass'}
        self.config['API'] = {'endpoint': 'https://api.example.com', 'timeout': '60'}
        self.config['Attachments'] = {'image_attachment_accept_value': 'image/*,video/mp4,video/3gpp,video/quicktime', 'file_attachment_accept_value': '*'}
        self.config['Modals'] = {'invalid_modal_text': 'Phone number shared via url is invalid.', 'invalid_modal_okay_button_class': 'x889kno x1a8lsjc xbbxn1n xxbr6pl x1n2onr6 x1rg5ohu xk50ysn x1f6kntn xyesn5m x1z11no5 xjy5m1g x1mnwbp6 x4pb5v6 x178xt8z xm81vs4 xso031l xy80clv x13fuv20 xu3j5b3 x1q0q8m5 x26u7qi x1v8p93f xogb00i x16stqrj x1ftr3km x1hl8ikr xfagghw x9dyr19 x9lcvmn xbtce8p x14v0smp xo8ufso xcjl5na x1k3x3db xuxw1ft xv52azi'}
        self.config['Buttons'] = {'attachment_button_val': '//span[@data-icon=\'plus\']', 'send_message_button_text': 'Send', 'send_button_value': '//*[@data-icon=\'send\']'}
        self.config['Timers'] = {'wait': '10', 'upload_wait': '5', 'sleep_time': '2'}
        self.config['Chrome'] = {'single_instance': 'False'}
        self.save_config()

    def get(self, section, key, fallback=None):
        try:
            return self.config.get(section, key)
        except (configparser.NoSectionError, configparser.NoOptionError):
            return fallback

    def get_int(self, section, key, fallback=0):
        try:
            return self.config.getint(section, key)
        except (configparser.NoSectionError, configparser.NoOptionError, ValueError):
            return fallback

    def get_boolean(self, section, key, fallback=False):
        try:
            return self.config.getboolean(section, key)
        except (configparser.NoSectionError, configparser.NoOptionError, ValueError):
            return fallback

    def set(self, section, key, value):
        if not self.config.has_section(section):
            self.config.add_section(section)
        self.config.set(section, key, str(value))

    def save_config(self):
        with open(self.config_file, 'w') as configfile:
            self.config.write(configfile)