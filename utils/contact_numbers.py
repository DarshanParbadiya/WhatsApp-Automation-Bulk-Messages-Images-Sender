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

    def load_excel_to_dataframe(file_name):
        df = pd.read_excel(file_name)
        return df

    def load_contacts(file_name):
        extension = ContactNumber.find_extension(file_name)
        if extension == 'csv':
            df = pd.read_csv(file_name)
            return df
        elif extension == 'xlsx':
            df = pd.read_excel(file_name)
            return df
        else:
            print('Provided file is not spreadsheet')

    @staticmethod
    def find_extension(file_name):
        """
        Extracts and returns the file extension from a given file path.

        Parameters:
        file_path (str): The full file path.

        Returns:
        str: The file extension without the leading dot, or an empty string if no extension is found.
        """
        import os
        # Extract the file extension using os.path.splitext
        _, extension = os.path.splitext(file_name)
        # Return the extension without the leading dot
        return extension.lstrip('.')
    
       
        
 