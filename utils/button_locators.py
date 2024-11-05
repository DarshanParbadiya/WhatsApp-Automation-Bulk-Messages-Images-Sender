from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

class Locators():
    def __init__(self):
        self.attachment_button_val = "//span[@data-icon='plus']"
        # self.image_box_val = "//input[@accept='image/*,video/mp4,video/3gpp,video/quicktime']"
        self.image_attachment_accept_value = "image/*,video/mp4,video/3gpp,video/quicktime"
        self.file_attachment_accept_value = "*"
        self.send_message_button_text = "Send"
        self.send_button_value = f"//*[@data-icon='send']"
        self.invalid_modal_text = "Phone number shared via url is invalid."
        self.invalid_modal_okay_button_class ="x889kno x1a8lsjc xbbxn1n xxbr6pl x1n2onr6 x1rg5ohu xk50ysn x1f6kntn xyesn5m x1z11no5 xjy5m1g x1mnwbp6 x4pb5v6 x178xt8z xm81vs4 xso031l xy80clv x13fuv20 xu3j5b3 x1q0q8m5 x26u7qi x1v8p93f xogb00i x16stqrj x1ftr3km x1hl8ikr xfagghw x9dyr19 x9lcvmn xbtce8p x14v0smp xo8ufso xcjl5na x1k3x3db xuxw1ft xv52azi"
        self.invalid_modal_okay_button_value = f"//*[@class='{self.invalid_modal_okay_button_class}']"

    def aria_text_locator(self,driver,wait_time,label_value):
        try:
            button = WebDriverWait(driver, wait_time).until(EC.presence_of_element_located((By.XPATH, f'//button[@aria-label="{label_value}"]')))
        except:
            print(f"{button} from aria text not found")
            return False
        else:
            return button
        
    
    def x_path_locator(self,driver,wait_time,path):

        try:
            button = WebDriverWait(driver, wait_time).until(EC.presence_of_element_located((By.XPATH, path)))
        except:
            print(f"{button} not found on the page")
            return False
        else:
            print(f'{path} is found on the web page')
            return button
        
    def does_page_contains_text(self,driver,wait_time,label):
        try:
            element = WebDriverWait(driver, wait_time).until(
                EC.presence_of_element_located((By.XPATH, f"//*[contains(text(), '{label}')]"))
            )
        except:
            print("number is not found as invalid")
            return False
        else:
            if element:
                print("The text 'Phone number shared via url is invalid.' is present on the page.")
            return True

    def find_element_by_attributes(self,driver, wait_time,accept_value):
        try:
            # "image/*,video/mp4,video/3gpp,video/quicktime"
            # or *
            element = driver.find_element(By.XPATH, f"//input[@accept='{accept_value}']")
            # driver.execute_script("arguments[0].style.display = 'block';", element)
            # element = WebDriverWait(driver, wait_time).until(
            #     EC.presence_of_element_located((By.XPATH, f"//input[@accept='{accept_value}']"))
            # )
        except Exception as e:
            print(f"Attachment button with {accept_value}:accept values not found: {e}")
            return None
        else:
            return element

        