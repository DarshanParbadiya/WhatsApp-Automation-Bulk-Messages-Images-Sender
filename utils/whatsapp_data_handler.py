import pandas as pd

class WhatsappDataHandler: # Class to encapsulate data handling functions
    @staticmethod
    def add_details_to_data_frame(df, data): # Make it static as it's a utility function, no instance state needed
        new_row = pd.DataFrame([data], columns=['number'])
        temp_df = pd.concat([df, new_row], ignore_index=True)
        return temp_df