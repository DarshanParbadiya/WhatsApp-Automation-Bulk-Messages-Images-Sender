
# WhatsApp-Automation-Bulk-Messages-Sender
This project helps to send bluk whatsapp messages without saving in contacts. Simply put contact numbers into EXCEL sheet, then run this scripts accordingly to your need. 

### This project contains two scripts 
- #### 1. script.py : for sending text messages
- #### 2. image.py : for sending images 

## Note
This is only for educational purposes, there are WhatsApp Business APIs available for the same purpose.

[![MIT License](https://img.shields.io/badge/License-MIT-green.svg)](https://choosealicense.com/licenses/mit/)



## How to use


## How to Use

### 1. Install required modules for these scripts to run
for script to run please install this packages using the commands given here

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
* Web Driver: Run in command prompt 
```bash
  pip install webdriver_manager
```

* Openpyxl: Run in command prompt 
```bash
  pip install openpyxl
```


### 2. Using first script for sending text messages
* First to use these scripts there is need to **clone this respiratory** or **download as zip** then extract to desired location
* Run python scripts by this command by **using powershell or cmd** in the same folder where this scripts are located 
-  open **chrome webdriver** which will be  like cmd window, keep it open for this scripts to run. Although it is already included in this respiratory but with changes in chrome this driver will change and might not work in future. In short download it by checking your chrome about section which contains version of your browser
- to send text message use this command
```bash
  python script.py 
```



* The **script opens WhatsApp web** using chrome.
* User needs to **scan QR** code from his/her phone.
* Wait till whatsapp loads 
* **Press enter key** in command prompt to execute further.
* The script hit url with contact number and message from excel sheet.
* On **every number that excel sheet** has **whatsapp web will reload** so don't panic
* Once all the message will be sent **chrome driver will automatically closed.**

Note: steps are the same for sending images **but with slight changes.**

### 3. Using second script for sending messages with images  
- follow above all the steps in addition to those, there is a folder image which will have image that you want to send.
- now in image.py find this line and give path from your PC.

```bash

file_path = 'C:/Users/PCname/Desktop/whatsapp automation/photo/send.jpeg'

```

Note: **windows uses** path like below basically uses backward slash, when you copy path **don't forget to change like above which uses forward slash.**

#### windows path for example looks like this, change it like above.
``` bash
C:\Users\pc\Desktop\whatsapp automation

```

- change path and use this command to run the script
- for sending images use image.py script

```bash
   python image.py 
```
## Acknowledgements

 - [inforkgodara](https://github.com/inforkgodara/whatsapp-bulk-messages-without-saving-contacts#prerequisites)


## Contributing

Contributions are always welcome!

See `contributing.md` for ways to get started.

Please adhere to this project's `code of conduct`.


## Installation

clone project using 

```bash
  git clone https://github.com/DarshanParbadiya/WhatsApp-Automation-Bulk-Messages-Sender.git
```

then install required modules stated in how to use section finally run the scripts 
    
## FAQ

#### Question 1 How to install dependencies

Install using cmd which can be opend by searching in start button of windows.

#### Question 2 Scripts are not working now what to do

You only have to change this, because with updates whatsapp may change it's UI.

``` bash
attachment_button = WebDriverWait(driver, 35).until(EC.element_to_be_clickable((By.XPATH, "//span[@data-testid='clip']")))
```
in above's code **change (By.XPATH, 'new whatsapp attributes')**
for this you need to know little bit of HTML. sry by can't help more than this. I might not change the code but alwayscontributions are always accepted.

#### Question 3 errors due to changes in selenium syntax

follow official documentation to change syntax if it changes in the future.
## Feedback

If you have any feedback, please reach out to us at darshanparbadya@gmail.com


## Features

- Sending bulk messages
- No need to save contacts before sending messaages
- Sending images functionality implemented
- Cross platform


## 🚀 About Me
I'm a full stack developer...
