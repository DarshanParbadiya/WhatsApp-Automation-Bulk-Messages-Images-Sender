# WhatsApp-Automation-Bulk-Messages-Sender

This project helps to send bluk whatsapp messages without saving in contacts. Simply put contact numbers into CSV flile, then run this scripts accordingly to your need.

### GUI of this same script can be found in release v1.4 : [Download from here](https://github.com/DarshanParbadiya/WhatsApp-Automation-Bulk-Messages-Images-Sender/releases/tag/v1.4)

Exported CSV will be present in the same folder where this software is located.
![image](https://github.com/user-attachments/assets/681271eb-cd8c-4cbd-ae59-0f76ce9cdd5f)

#### Different messages types list : choose one of the options from here.
![image](https://github.com/user-attachments/assets/b4cea075-0cce-4475-9beb-37a77fd79655)

![image](https://github.com/user-attachments/assets/1a9d23e7-a307-4a6d-b3e1-07a092e37dc4)




### This project containts script for running above software

## Note

This is only for educational purposes, there are WhatsApp Business APIs available for the same purpose.

[![MIT License](https://img.shields.io/badge/License-MIT-green.svg)](https://choosealicense.com/licenses/mit/)

## How to Use

### 1. Install required modules for these scripts to run

- for script to run please install this packages using the commands given here
- python is required to run below commands and the software itself so install it before using this script

```bash
  pip install -r requirements.txt
```
- you can skip steps from 3 if you are install dependencies using requirements.txt

#### 1. Python 3.11: Download it from https://www.python.org/downloads

#### 2. Chrome : Download it from https://chrome.google.com

#### 3. Pandas : Run in command prompt

```bash
  pip install pandas
```

#### 4. Xlrd : Run in command prompt

```bash
  pip install xlrd
```

#### 5. Selenium: Run in command prompt

```bash
pip install selenium
```

#### 6. Web Driver: Run in command prompt

```bash
  pip install webdriver_manager
```


## 2. Downloading or clone this project

- clone project using below command

```bash
  git clone https://github.com/DarshanParbadiya/WhatsApp-Automation-Bulk-Messages-Sender.git
```

## 3. Running the script

- Run this command using CMD from the same directory where this script is located

```bash
  python main.py
```
## 4. Instructions to use 
- Use open Whatsapp button to open chrome tab and scan QR code
- this step is only required once then you can load multiple excel file and send all the message again and again. No need to scan QR for next Excel file.
- After doing above step send message button becomes available.
- Load the Excel file and image accodingly.
- Choose type of message to be sent and click on send.
- This also opens debugger window to show which steps are being performed by the software. 
- at the end of the script status of the message will be available in status section.

## updating the script when whatsapp web interface changes
 ![image](https://github.com/user-attachments/assets/9035b99e-76bf-43d6-a2e3-bd3b3e207ad9)
change this values accordingly when whatsappweb html tags and classes gets changed.

## Troubleshooting  

![image](https://github.com/user-attachments/assets/f8410d8f-fb56-4e6b-b1cd-9416af3ce6e2)


If whatsapp web is working slow and shows loading chat in your computer then change initial wait 

## FAQ

#### Question 1 How to install dependencies

Install using cmd which can be opened by searching in start button of windows.

#### Question 2 Scripts are not working now what to do

You only have to change this, because with updates whatsapp may change it's UI.

#### Question 3 errors due to changes in selenium syntax

follow official documentation to change syntax if it changes in the future.

## Feedback

If you have any feedback, please reach out to us at darshanparbadiya@gmail.com

## Features

- Sending bulk messages
- Sending same or different message choice
- No need to save contacts before sending messaages
- Sending images with or without text.
- Cross platform

## 🚀 About Me

I'm a full stack developer...
