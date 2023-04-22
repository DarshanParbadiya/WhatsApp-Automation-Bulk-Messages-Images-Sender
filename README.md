# WhatsApp-Automation-Bulk-Messages-Sender

This project helps to send bluk whatsapp messages without saving in contacts. Simply put contact numbers into EXCEL sheet, then run this scripts accordingly to your need.

### GUI of this same script can be found in release v1.2
![image](https://user-images.githubusercontent.com/65885245/233774628-1b19f651-b05e-4c8e-a3a7-e34113fc429b.png)
![image](https://user-images.githubusercontent.com/65885245/233775229-8903d511-4b23-4f16-b48b-c00ee567e597.png)


### This project containts script for running above software

## Note

This is only for educational purposes, there are WhatsApp Business APIs available for the same purpose.

[![MIT License](https://img.shields.io/badge/License-MIT-green.svg)](https://choosealicense.com/licenses/mit/)

## How to Use

### 1. Install required modules for these scripts to run

- for script to run please install this packages using the commands given here
- python is required to run below commands and the software itself so install it before using this script

#### 1. Python 3.8: Download it from https://www.python.org/downloads

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

#### 7.Openpyxl: Run in command prompt

```bash
  pip install openpyxl
```

#### 8.pysimplegui: Run in command prompt

```bash
  pip install pysimplegui
```

## 2. Downloading or clone this project

- clone project using below command

```bash
  git clone https://github.com/DarshanParbadiya/WhatsApp-Automation-Bulk-Messages-Sender.git
```

## 3. Running the script

- Run this command using CMD from the same directory where this script is located

```bash
  python whatsapp_helper.py
```
## 4. Instructions to use 
- Use open Whatsapp button to open chrome tab and scan QR code
- this step is only required once then you can load multiple excel file and send all the message again and again. No need to scan QR for next Excel file.
- After doing above step send message button becomes available.
- Load the Excel file and image accodingly.
- Choose type of message to be sent and click on send.
- This also opens debugger window to show which steps are being performed by the software. 
- at the end of the script status of the message will be available in status section. 

## FAQ

#### Question 1 How to install dependencies

Install using cmd which can be opend by searching in start button of windows.

#### Question 2 Scripts are not working now what to do

You only have to change this, because with updates whatsapp may change it's UI.

```bash
attachment_button = WebDriverWait(driver, 35).until(EC.element_to_be_clickable((By.XPATH, "//span[@data-testid='clip']")))
```

in above's code **change (By.XPATH, 'new whatsapp attributes')**
for this you need to know little bit of HTML.  

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
