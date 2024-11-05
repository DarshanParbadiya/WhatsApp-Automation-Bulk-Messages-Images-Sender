import csv
import pandas as pd
from PySide6.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QTextEdit, QFileDialog

class ContactNumber():
    def __init__(self,message_type="Message"):
        pass

    def create_empty_csv(file_name):
        # Define the header (column names)
        header = ["Contact No", "Message"]

        # Create or overwrite the CSV file
        with open(file_name, mode='w', newline='') as csvfile:
            writer = csv.writer(csvfile)

            # Write the header to the CSV file
            writer.writerow(header)

        print(f"Empty CSV file '{file_name}' created with columns: {header}")


    def load_csv_to_dataframe(file_name):
        # Load the CSV file into a DataFrame
        df = pd.read_csv(file_name)
        return df
    
    
       
        
 