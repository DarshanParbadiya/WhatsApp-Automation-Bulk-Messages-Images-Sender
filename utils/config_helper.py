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
