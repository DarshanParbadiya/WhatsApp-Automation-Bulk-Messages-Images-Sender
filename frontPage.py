from UI.ui_index import Ui_MainWindow
from PySide6.QtGui import QAction
from PySide6.QtWidgets import QMainWindow
from utils.whatsapp_helper import Whatsapp
from utils import DialogBox,FileDialog,Config
import configparser
import csv

class MySideBar(QMainWindow,Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle("Whatsapp Helper")
        self.config_instance = Config(self)
        self.config_instance.set_config_values()
        self.config_instance.load_config_values()
        self.whatsapp_instance = Whatsapp(self)
        self.file_dialog_instance = FileDialog()
        self.dialogBox_instance = DialogBox()
        # self.config_instance.mainWindow = self
        # self.config = configparser.ConfigParser()
        # self.config.read('config.ini')
        # self.get_config_values()
        # self.load_config_values()


        # self.whatsapp_page_button.setAutoExclusive(True)
        # self.manage_page_button.setAutoExclusive(True)
        # self.settings_page_button.setAutoExclusive(True)

        self.whatsapp_page_button.clicked.connect(lambda: self.switch_to_desired_page(0))
        self.whatsapp_page_button.setChecked(True)
        self.settings_page_button.clicked.connect(lambda: self.switch_to_desired_page(1))
        self.manage_page_button.clicked.connect(lambda: self.switch_to_desired_page(2))
        self.timers_page_button.clicked.connect(lambda: self.switch_to_desired_page(3))
        self.message_page_button.clicked.connect(lambda: self.switch_to_desired_page(4))
        # when open whatsapp button is clicked


        self.select_message_type_combo_box.addItems(self.whatsapp_instance.message_types)  # Add multiple options at once

 
    # Connect signal to a slot (method) to handle selection change
        self.select_message_type_combo_box.currentIndexChanged.connect(self.on_selection_change)

        self.open_whatsapp_button.clicked.connect(self.handle_whatsapp_page_button)
        self.send_button.clicked.connect(self.whatsapp_instance.send_messages)

        self.save_cookies.clicked.connect(self.whatsapp_instance.save_cookies)
        self.load_cookies.clicked.connect(self.whatsapp_instance.load_cookies)

        self.load_csv_btn.setCheckable(True)
        self.load_csv_btn.clicked.connect(self.handle_load_csv_button)
        self.load_image_btn.clicked.connect(self.handle_load_image_button)
        self.save_custom_message_button.clicked.connect(self.handle_save_message_button)
        # self.save_button.clicked.connect(self.whatsapp_instance.send_messages)

        self.save_settings_button.clicked.connect(self.config_instance.save_config)
        self.sent_numbers_button.clicked.connect(lambda:self.export_csv_reports("sent_numbers_df"))
        self.invalid_numbers_button.clicked.connect(lambda:self.export_csv_reports("invalid_number_df"))
        self.not_sent_numbers_button.clicked.connect(lambda:self.export_csv_reports("not_sent_number_df"))
        self.create_sample_csv_button.clicked.connect(lambda:self.create_sample_csv("sample.csv"))

    def export_csv_reports(self,report_type):
        # if report_type == 
        data_frame = getattr(self.whatsapp_instance, report_type, None)

        # Check if the attribute exists and is a DataFrame
        if data_frame is not None:
            # Assuming the attribute is a DataFrame, export it to CSV
            data_frame.to_csv(f'{report_type}_output.csv', index=False)
        else:
            print(f"Error: '{report_type}' is not a valid attribute or not a DataFrame.")
            self.whatsapp_instance.report_type.to_csv('output.csv', index=False)  # index=False prevents writing row numbers
    
    def create_sample_csv(self,file_name):
        header = ["Contact No", "Message"]

        # Create or overwrite the CSV file
        with open(file_name, mode='w', newline='') as csvfile:
            writer = csv.writer(csvfile)

            # Write the header to the CSV file
            writer.writerow(header)

        print(f"Empty CSV file '{file_name}' created with columns: {header}")


    def on_selection_change(self,index):
        selected_option = self.select_message_type_combo_box.itemText(index)
        self.whatsapp_instance.current_message_selection = selected_option
        print(f"Selected Option: {selected_option}")
        
    # def show_current_selected_items(self):
    #     self.select_message_type_combo_box

    def handle_load_csv_button(self):
        file_name = self.dialogBox_instance.show_dialog_box()
        self.excel_text_edit.setPlainText(str(file_name[0]))
        self.whatsapp_instance.csv_path = str(file_name[0])
        # print(file_name)

    def handle_load_image_button(self):
        file_name = self.dialogBox_instance.show_dialog_box()
        self.image_text_edit.setPlainText(str(file_name[0]))
        self.whatsapp_instance.image_path = str(file_name[0])
        # print(file_name)
        
    def handle_save_message_button(self):
        self.whatsapp_instance.custom_message = self.custom_message.toPlainText()
        print("Message saved")
        
    def switch_to_desired_page(self,index):
        print(f"changed to {index}")
        self.stackedWidget.setCurrentIndex(index)
    
    def handle_whatsapp_page_button(self):
        self.whatsapp_instance.open_whatsapp()

    def openDialog(self):
        from UI.ui_dialog import Ui_Dialog

        dialog_obj = Ui_Dialog(self)
        result = dialog_obj.exec()

        if result == Ui_Dialog.accepted:
            # yes
            pass


