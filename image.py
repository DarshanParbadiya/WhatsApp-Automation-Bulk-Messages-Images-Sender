# Program to send bulk messages through WhatsApp web from an excel sheet without saving contact numbers
# Author @inforkgodara

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep
import pandas

excel_data = pandas.read_excel('Recipients data.xlsx', sheet_name='Recipients')


# =====================================================================
file_path = 'C:/Users/Jagdish Patel/Desktop/whatsapp automation/photo/send.jpeg'
# =====================================================================
count = 0

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get('https://web.whatsapp.com')
input("Press ENTER after login into Whatsapp Web and your chats are visiable.")
for column in excel_data['Contact'].tolist():
    try:
        url = 'https://web.whatsapp.com/send?phone=' + str(excel_data['Contact'][count])
        sent = False
        # It tries 3 times to send a message in case if there any error occurred
        driver.get(url)
        try:
            attachment_button = WebDriverWait(driver, 35).until(
                EC.element_to_be_clickable((By.XPATH, "//span[@data-testid='clip']")))
            attachment_button.click()

        except Exception as e:
            print("Sorry Image could not sent to " + str(excel_data['Contact'][count]))
        else:
            sleep(2)
            image_box = driver.find_element(By.XPATH, "//input[@accept='image/*,video/mp4,video/3gpp,video/quicktime']")
            image_box.send_keys(file_path)
            sleep(5)
            click_btn = WebDriverWait(driver, 35).until(
                EC.element_to_be_clickable((By.XPATH, "//div[@class='p357zi0d gndfcl4n ac2vgrno mh8l8k0y k45dudtp i5tg98hk f9ovudaz przvwfww gx1rr48f f8jlpxt4 hnx8ox4h k17s6i4e ofejerhi os0tgls2 g9p5wyxn i0tg5vk9 aoogvgrq o2zu3hjb hftcxtij rtx6r8la e3b81npk oa9ii99z p1ii4mzz']")))
            click_btn.click()
            sleep(5)
            sent = True
            print('Image sent to: ' + str(excel_data['Contact'][count]))
        count = count + 1
    except Exception as e:
        print('Failed to send Image to ' + str(excel_data['Contact'][count]) + str(e))
driver.quit()
print("The script executed successfully.")
