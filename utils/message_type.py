
from enum import Enum


class Message: 
    def __init__(self):
        self.message_type = None
        self.data = None
        self.message_types = ["Same Messages for everyone", "Different Messages for Each", "Send Image","Send Image with Same Message","Send Image with Different Message"]

    def send_message(self,contacts):
        if type == self.message_type[0]:
            message = str(contacts['Message'][0])
            print(message)
        for index, row in contacts.iterrows():
            print(f"Row {index}: Contact No = {row['Contact No']}, Message = {row['Message']}")        




# class Color(Enum):
#     MESSAGE = 1
#     GREEN = 2
#     BLUE = 3

# # Accessing Enum Members
# print(Color.none)             # Output: Color.RED
# print(Color.GREEN)           # Output: Color.GREEN
# print(Color.BLUE.name)       # Output: 'BLUE'
# print(Color.BLUE.value)      # Output: 3

# # Looping through Enum Members
# for color in Color:
#     print(color)