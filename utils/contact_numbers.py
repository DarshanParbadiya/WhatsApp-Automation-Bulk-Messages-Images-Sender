# utils/contact_numbers.py
import csv
import pandas as pd
from PySide6.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QTextEdit, QFileDialog

class ContactNumber():
    """
    Handles loading contact numbers and messages from CSV and Excel files.

    This class provides static methods to create empty CSV templates and load contact data
    from CSV or Excel files into pandas DataFrames. It supports both .csv and .xlsx file formats.

    Refactored from original 'utils/contact_numbers.py': Docstrings are added for better documentation
    and the load functions are made static methods for better class structure.

    Backward Compatibility: This class remains fully backward compatible as existing code that
    instantiates and uses 'ContactNumber' or calls its methods will continue to function
    without any changes to its API.
    """
    def __init__(self, message_type="Message"):
        """
        Initializes ContactNumber instance. (Currently no specific initialization needed)
        """
        pass # No specific initialization needed for now

    @staticmethod
    def create_empty_csv(file_name):
        """
        Creates an empty CSV file with "Contact No" and "Message" headers.

        This function generates a new CSV file at the specified path with columns
        'Contact No' and 'Message'. This template file can be used to prepare contact data
        for sending WhatsApp messages.

        Args:
            file_name (str): The full path and name for the CSV file to be created.
                              e.g., 'contacts_template.csv' or 'C:/path/to/contacts.csv'.
        """
        # Define the header (column names)
        header = ["Contact No", "Message"]

        # Create or overwrite the CSV file
        with open(file_name, mode='w', newline='') as csvfile:
            writer = csv.writer(csvfile)

            # Write the header to the CSV file
            writer.writerow(header)

        print(f"Empty CSV file '{file_name}' created with columns: {header}") # Confirmation message


    @staticmethod
    def load_csv_to_dataframe(file_name):
        """
        Loads contact data from a CSV file into a pandas DataFrame.

        Reads the CSV file specified by 'file_name' and returns its content as a pandas DataFrame.
        It expects the CSV file to have columns like 'Contact No' and 'Message'.

        Args:
            file_name (str): The path to the CSV file to load.

        Returns:
            pandas.DataFrame: A DataFrame containing the data from the CSV file.
        """
        # Load the CSV file into a DataFrame
        df = pd.read_csv(file_name)
        return df

    @staticmethod
    def load_excel_to_dataframe(file_name):
        """
        Loads contact data from an Excel file into a pandas DataFrame.

        Reads the Excel file specified by 'file_name' and returns its content as a pandas DataFrame.
        It supports .xlsx format and expects columns like 'Contact No' and 'Message'.

        Args:
            file_name (str): The path to the Excel file to load (.xlsx).

        Returns:
            pandas.DataFrame: A DataFrame containing the data from the Excel file.
        """
        df = pd.read_excel(file_name)
        return df

    @staticmethod
    def load_contacts(file_name):
        """
        Loads contact data from a file (CSV or Excel) into a pandas DataFrame.

        This method automatically detects the file type based on the extension (.csv or .xlsx)
        and calls the appropriate loading function (load_csv_to_dataframe or load_excel_to_dataframe).

        Args:
            file_name (str): The path to the contact file (CSV or Excel).

        Returns:
            pandas.DataFrame or None: A DataFrame containing the contact data if loading is successful.
                                      Returns None if the file extension is not recognized
                                      or if there's an error during file loading (more robust error handling can be added).
        """
        extension = ContactNumber.find_extension(file_name) # Determine file extension
        if extension == 'csv': # Load CSV if extension is .csv
            df = ContactNumber.load_csv_to_dataframe(file_name)
            return df
        elif extension == 'xlsx': # Load Excel if extension is .xlsx
            df = ContactNumber.load_excel_to_dataframe(file_name)
            return df
        else:
            print('Provided file is not a supported spreadsheet format (CSV or XLSX)') # Informative message
            return None # Indicate failure to load


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