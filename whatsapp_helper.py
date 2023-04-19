import PySimpleGUI as sg
import os.path

msg_type = ['Send text message only', 'Send Image', 'Send Text and Image Both']
# cssText = {'text_color': 'white', 'background_color': 'green'}
# apply using **cssText
cssStatus = {'border': '1px solid white'}
# sg.theme('BlueMono')
buttons_frame = [[sg.Button('Send', disabled=True), sg.Button('Open WhatsApp') ]]


progress_bar = [[sg.ProgressBar(100, orientation='h', expand_x=True, size=(30, 20),  key='-PBAR-'),
    sg.Text('0', key='-OUT-', enable_events=True, font=('Arial Bold', 16), expand_x=True)
     ]]
message_type_list = [[sg.Combo(msg_type, expand_x=True, enable_events=True,
                               readonly=True, default_value=msg_type[0], key='-msg type-')]]
message_sender_column = [
    # [sg.Text('choose Excel file or keep it in the same folder')],
    [sg.Frame('Select Message type', message_type_list),sg.Frame('Sending buttons', buttons_frame)],
    [sg.Frame('Excel file input', [
        [
            sg.In(size=(42, 1), enable_events=True, key='-excel location-'),
            sg.FileBrowse(file_types=[('Excel files', '*.xlsx')])
        ],

        [
            sg.Button('Load Excel'),

        ],
    ])],

    [sg.Frame('Status', [[sg.Listbox(values=[], size=(50, 28), key="-status-")]])],
]
image_frame = [
    [
        sg.In(size=(50, 2), enable_events=True, key='-image location-'),
        sg.FileBrowse(),
    ],
    [sg.Button('Load Image')],
]
time_range = [i for i in range(1,31)]

wait_attachment = [[sg.Text("Attachment "),sg.Spin(time_range, initial_value=10, readonly=True, size=2, enable_events=True, key='-WAIT ATTACHMENT-')]]
invalid_wait = [[sg.Text("Invalid Wait"),sg.Spin(time_range, initial_value=5, readonly=True, size=2, enable_events=True, key='-INVALID WAIT-')]]
upload_wait = [[sg.Text("Upload wait"),sg.Spin(time_range, initial_value=10, readonly=True, size=2, enable_events=True, key='-UPLOAD WAIT-')]]

buttons_frame = [[sg.Frame("Invalid wait",invalid_wait)],[sg.Frame("Upload wait",upload_wait)], ]
output_column = [
    # [sg.Text('Image Location')],
    [sg.Frame('Image Location', image_frame, pad=(0, 10)),sg.Frame("delay timings",buttons_frame)  ],

    [sg.Frame("Progress",progress_bar),sg.Frame("Initial wait",wait_attachment) ],
    
     [sg.Frame('Image Status', [[sg.Listbox(values=[], size=(80, 2),
              key="-image status-", horizontal_scroll=True)],])],
    [sg.Frame('Numbers List', [[sg.Listbox(values=[], size=(80, 20),
              key="-numbers list-", horizontal_scroll=True)],])],
   

]

tab1Layout = [[sg.Column(message_sender_column), sg.Column(output_column)]]


log_number_sent = [
    [sg.Listbox(values=[], size=(50, 28), key="-log number sent-")]]
log_message_window = [[sg.Listbox(values=[], size=(
    80, 28), key="-log message window-", horizontal_scroll=True)]]

tab2Layout = [
    [sg.Frame("Status", log_number_sent), sg.Frame(
        'Send', log_message_window)], [sg.Button('Clear')]
]
#    [sg.Frame('Select Message type',)]


# tab3Layout = [[sg.Image(r'C:/Users/Jagdish Patel/Desktop/whatsapp automation/photo/send.png',subsample=2,key='-image-')]]
# sg.VSeperator(),

layout = [[sg.TabGroup([[sg.Tab('Load Files', tab1Layout), sg.Tab('Send messages', tab2Layout),]])], [sg.Exit()]
          ]



window = sg.Window('WhatsApp messages sender', layout, resizable=True)
excel_path = None
def_excel_path = 'C:/Users/Jagdish Patel/Desktop/whatsapp automation/Recipients data.xlsx'
image_path = None
img_msg = []
excel_msg = []
log = []
log_window_messages = []
# window['Send'].update(disabled=True)


def update_log(log, msg):
    sg.Print(msg)
    log.append(msg)
    window['-status-'].update(log)
    # window['-log number sent-'].update(log)


def update_numbers_list(excel_msg, msg):
    excel_msg.append(msg)
    sg.Print(msg)
    window['-numbers list-'].update(excel_msg)



while True:
    event, values = window.read()
    if event == 'Exit' or event == sg.WIN_CLOSED:
        break
    # if values['-msg type'] == 1:
    #     window['Load Image'].update(disabled=True)

    # loading Image------------------------------------------------------------------------------------------------------------
    elif event == 'Load Image':
        try:
            image_path = values['-image location-']
            window['-image status-'].update(img_msg)
            if image_path != None and image_path != '':
                img_msg = []
                msg = 'Image is provided by User ✅'
                img_msg.append(msg)
                img_msg.append(image_path)
                window['-image status-'].update(img_msg)
            else:
                if (image_path == ''):
                    raise Exception("❌ Sorry, no file selected")
                if (image_path == None):
                    raise Exception("❌ Sorry, file path is none")

        except Exception as e:
            msg = '📁 Image loading failed because '+str(e)
            sg.popup_ok(msg)
            # sg.Print(msg)
            continue

    # Loading excel--------------------------------------------------------------------------------------------------------------
    elif event == 'Load Excel':
        import pandas
        import os

        try:
            excel_path = values['-excel location-']
            window['-numbers list-'].update(excel_msg)
            # sg.Print(excel_path,type(excel_path))
            msg = [excel_path]
            window['-numbers list-'].update(msg)

            # sg.Print('excel_default_path = '+str(excel_path))
            if excel_path != None and excel_path != '':
                excel_msg = []
                msg = 'Sheet is provided by User ✅'
                excel_msg.append(msg)
                excel_msg.append(excel_path)
                # update_log_message_sent(log_window_messages,msg)
                # update_log_message_sent(log_window_messages,excel_path)
                window['-numbers list-'].update(excel_msg)
                excel_data = pandas.read_excel(excel_path)
            else:
                if (excel_path == ''):
                    sg.popup_ok('❌ No file selected')
                    raise Exception("❌ No file selected")

                if (excel_path == None):
                    sg.popup_ok("❌ file path is none")
                    raise Exception("❌ file path is none")

                excel_data = pandas.read_excel('Recipients data.xlsx')
        except Exception as e:
            sg.PopupOK('📁 Excel loading failed because '+str(e))
            # sg.Print('📁 Excel loading failed because '+str(e))
            continue

        numbers = []
        rows = len(excel_data.index)
        # sg.Print("total numbers count = "+str(rows))
        # printing numbers in the display
        for i in range(rows):
            numbers.append(str(i+1)+'. ' + str(excel_data['Contact'][i]))
        rows = len(excel_data.index)
        excel_msg.extend(numbers)
        log_window_messages.extend(numbers)

        msg = "total numbers count = "+str(rows)
        # update_log_message_sent(log_window_messages,msg)
        # update_numbers_list(excel_msg,str(msg))
        window['-numbers list-'].update(excel_msg)
        # update_log_message_sent(log_window_messages,msg)
        msg = excel_data['Message'][0]
        
        excel_msg.append('Message is:'+str(msg))
        window['-numbers list-'].update(excel_msg)

    # Opening whatsapp---------------------------------------------------------------------------------------------
    elif event == 'Open WhatsApp':
        
        # excel_data = pandas.read_excel('Recipients data.xlsx')
        ch = sg.popup_yes_no('Do you wish to continue?', title='YesNo')
        if (ch == 'Yes'):
            from selenium import webdriver
            from selenium.webdriver.support.ui import WebDriverWait
            from selenium.webdriver.support import expected_conditions as EC
            from selenium.webdriver.common.by import By
            from webdriver_manager.chrome import ChromeDriverManager
            from time import sleep
            import pandas
            driver = webdriver.Chrome(ChromeDriverManager().install())
            driver.get('https://web.whatsapp.com')
            # input("Press ENTER after login into Whatsapp Web and your chats are visiable.")
            sleep(2)
            ch = sg.popup_yes_no('Is WhatsApp loaded?', title='YesNo')
            if (ch == 'Yes'):
                window['Open WhatsApp'].update(disabled=True)
                window['Send'].update(disabled=False)
                msg = "Whatsapp is opened in chrome window"
                update_log(log, msg)
        else:
            msg = "Whatsapp is opening canceled ❎ by user"
            update_log(log, msg)
             
    # clear console-----------------------------------------------------------------------
    elif event == 'Clear':
        log_window_messages = []
        window['-log message window-'].update(log_message_window)

    # send button trigger --------------------------------------------------------
    elif event == 'Send':

        # getting type of message from dropdown
        message_type = values['-msg type-']
        # ask user to continue with the choice
        ch = sg.popup_yes_no(
            "Do you want to Continue ✅❎?\nAnd your choice is : "+message_type, title="YesNo")
        if ch == 'Yes':
            try:
                # sending Text messages-------------------------------------------------------------------------------------------------------------------
                if (message_type == msg_type[0]):
                    sg.Print('inside send text messages')
                    log = []
                    try:
                        sg.Print('inside try')
                        if excel_path != None and excel_path != '':
                            pass
                        else:
                            raise Exception('Excel is not loaded 📝')
                        count = 0
                        wait_image = 20
                        wait_attachment = values['-WAIT ATTACHMENT-']
                        invalid_wait_time = values['-INVALID WAIT-']

                        rows = len(excel_data.index)
                        window['-PBAR-'].update(current_count=0,max=rows)
                        # window['-PBAR-'].update(current_count=count)
                        for count in range(rows):
                            window['-PBAR-'].update(current_count=count+1)
                            window['-OUT-'].update(count+1)
                            sent = False
                            if(count==rows):
                                break
                            if(count<rows):
                                try:
                                    url = 'https://web.whatsapp.com/send?phone=' + \
                                    str(excel_data['Contact'][count]) + \
                                            '&text=' + excel_data['Message'][0]
                                    # '❌' '✔️' ' ✅❎📁📝🗄️  ' 
                                    msg = "---------------------------------------------------------"
                                    sg.Print(msg)
                                    msg =url
                                    sg.Print(msg)
                                    msg = str(count+1)+". number is "+str(excel_data['Contact'][count])
                                    sg.Print(msg)
                                    sent = False
                                    is_invalid = False
                                    # It tries 3 times to send a message in case if there any error occurred
                                    driver.get(url)
                                    attempt = 2
                                    while attempt>0:
                                        try:
                                            try:
                                                # try to locate send button for sending messages
                                                msg ='waiting for send button to be clicked max wait '+str(wait_attachment)+" attempt "+str(attempt)
                                                sg.Print(msg)
                                                attempt-=1
                                                
                                                click_btn = WebDriverWait(driver, wait_attachment).until(EC.element_to_be_clickable(
                                                                (By.XPATH, "//button[@data-testid='compose-btn-send']")))
                                                msg = 'successfully located a chat send button'
                                            except:
                                                msg = "error finding chat button "+" attempt "+str(attempt)
                                                sg.Print(msg)  
                                                try:
                                                    msg = "Checking for invalid ❎"
                                                    sg.Print(msg)
                                                    number_invalid_btn = WebDriverWait(driver, invalid_wait_time).until(EC.element_to_be_clickable((By.XPATH, "//button[@data-testid='popup-controls-ok']")))
                                                except:        
                                                    driver.get(url)
                                                    msg = "not found ❎invalid yet so, giving reload to check twice"
                                                    sg.Print(msg)
                                                else:
                                                    number_invalid_btn.click()
                                                    is_invalid = True
                                                    msg = "clicked on invalid button ❎"

                                                    sg.Print(msg)
                                                    msg = 'breaking out of the loop 1, ⭕'
                                                    sg.Print(msg)
                                                    break
                                        
                                        except:
                                            msg = 'not send button and not invalid problem'
                                            sg.Print(msg)
                                            msg = 'breaking out of the loop 2, ⭕⭕'
                                            sg.Print(msg)
                                            break
                                        else:
                                            sleep(2)
                                            click_btn.click()
                                            
                                            sent = True
                                            sg.Print('clicked on send button successfully')
                                            sleep(5)
                                            msg = 'message sent to: ' + str(excel_data['Contact'][count])
                                            sg.Print(msg)
                                            msg = "✔️✔️✔️✔️✔️✔️✔️✔️✔️✔️"
                                            sg.Print(msg)
                                            msg = str(excel_data['Contact'][count]) + '✔️'
                                            sg.Print(msg)
                                            
                                            break
                                except Exception as e:
                                    msg = 'Failed to send message to final exception ' + str(excel_data['Contact'][count]) + str(e)
                                    sg.Print(msg)
                                    msg = "❌❌❌❌❌❌❌❌❌❌"
                                    msg = str(excel_data['Contact'][count]) + '❌'
                                    sg.Print(msg)
                                    msg = 'breaking out of the loop 3, ⭕⭕⭕'
                                    sg.Print(msg)
                                    break
                                finally:
                                    if sent == True:
                                        msg = str(count+1) +". " +str(excel_data['Contact'][count]) + '✔️'
                                        update_log(log, msg)
                                        print(msg)
                                    else:
                                        if is_invalid == True and sent == False:
                                            msg = str(count+1) +". " +str(excel_data['Contact'][count])+" ❎ invalid user ❎" 
                                            update_log(log, msg)
                                        else:
                                            msg = str(count+1) +". " +str(excel_data['Contact'][count]) + '❌'
                                            update_log(log, msg)
                                            print(msg)
                                        
                            
                                msg = "The script executed successfully."+ '✅'
                                print(msg)
                    except Exception as e:
                        msg = "📁 file related problems "+str(e)
                        ch = sg.popup_yes_no(msg + " please solve them first ", title="YesNo")
                        if ch == 'Yes':
                            pass
                        else:
                            pass
                        sg.Print(msg)





    # '❌' '✔️' ' ✅❎📁📝🗄️⭕  ' 

                elif message_type == msg_type[1]:  # sending Images-------------------------------------------------------------------
                    log = []
                    
                    try:
                        if excel_path != None and excel_path != '':
                            pass
                        else:
                            ch = sg.popup_yes_no("Excel is not loaded please select it fist")
                            if ch == 'Yes':
                                pass
                            else:
                                pass
                                            
                            raise Exception('Excel is not loaded 📝')

                        if image_path != None and image_path != '':
                            pass
                        else:
                            ch = sg.popup_yes_no("image is not loaded please select it fist")
                            if ch == 'Yes':
                                pass
                            else:
                                pass
                            raise Exception("image is not loaded 🗄️")

                        count = 0
                        image_upload_time = values['-UPLOAD WAIT-']
                        wait_attachment = values['-WAIT ATTACHMENT-']
                        invalid_wait_time = values['-INVALID WAIT-']

                        rows = len(excel_data.index)
                        window['-PBAR-'].update(current_count=0,max=rows)
                        for count in range(rows):
                            window['-PBAR-'].update(current_count=count+1)
                            window['-OUT-'].update(count+1)
                            
                            if(count==rows):
                                break
                            if(count<rows):
                                try:
                                    url = 'https://web.whatsapp.com/send?phone=' + \
                                    str(excel_data['Contact'][count]) + \
                                            '&text=' 
                                        #                 + excel_data['Message'][0]
                                    
                                    msg="---------------------------------------------------------"
                                     
                                    sg.Print(msg)
                                    msg=url
                                    sg.Print(msg)
                                    msg=str(count+1)+" number is "+str(excel_data['Contact'][count])
                                    sent = False
                                    # It tries 3 times to send a message in case if there any error occurred
                                    driver.get(url)
                                    attempt = 2
                                    while attempt>0:
                                        try:
                                            try:
                                                
                                                # try to locate send button for sending messages
                                                msg='waiting for attachment button to be clicked max wait '+str(wait_attachment)+" attempt "+str(attempt)
                                                sg.Print(msg)
                                                attempt-=1
                                                
                                                attachment_button = WebDriverWait(driver, wait_attachment).until(EC.element_to_be_clickable((By.XPATH, "//span[@data-testid='clip']")))
                                            except:
                                                msg="error finding attachment button "+" attempt "+str(attempt)
                                                sg.Print(msg)
                                                try:
                                                    msg="Checking for invalid"
                                                    sg.Print(msg)
                                                    number_invalid_btn = WebDriverWait(driver, invalid_wait_time).until(EC.element_to_be_clickable((By.XPATH, "//button[@data-testid='popup-controls-ok']")))
                                                except:        
                                                    driver.get(url)
                                                    msg="giving reload"
                                                    sg.Print(msg)
                                                else:
                                                    number_invalid_btn.click()
                                                    is_invalid =  True
                                                    msg="clicked on invalid button"
                                                    sg.Print(msg)
                                                    break
                                            else:
                                                attachment_button.click()
                                                msg='successfully located and clicked attachment button'+" attempt "+str(attempt)
                                                sg.Print(msg)
                                        
                                        except:
                                            msg='not attachment and not invalid problem'
                                            sg.Print(msg)
                                            break
                                        else:
                                            sleep(2)
                                            msg='locating image attach button'
                                            sg.Print(msg)
                                            try:
                                                image_box = driver.find_element(By.XPATH, "//input[@accept='image/*,video/mp4,video/3gpp,video/quicktime']")
                                            except:
                                                msg="can not click on image attach"
                                                sg.Print(msg)
                                            
                                            else:
                                                msg='clicked on image attach button successfully'
                                                sg.Print(msg)
                                                image_box.send_keys(image_path)
                                                msg='image sent successfully'
                                                sg.Print(msg)
                                                click_btn = WebDriverWait(driver, wait_image).until(EC.element_to_be_clickable((By.XPATH, "//div[@class='p357zi0d gndfcl4n ac2vgrno mh8l8k0y k45dudtp i5tg98hk f9ovudaz przvwfww gx1rr48f f8jlpxt4 hnx8ox4h k17s6i4e ofejerhi os0tgls2 g9p5wyxn i0tg5vk9 aoogvgrq o2zu3hjb hftcxtij rtx6r8la e3b81npk oa9ii99z p1ii4mzz']")))
                                                click_btn.click()
                                                msg='successfully clicked the Image send button'
                                                sg.Print(msg)
                                                sent = True
                                                msg='waiting for ' +str(image_upload_time) +' seconds for file upload'
                                                sg.Print(msg)
                                                sleep(image_upload_time)
                                                msg='Image sent to: ' + str(excel_data['Contact'][count])
                                                sg.Print(msg)
                                                msg="^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^"
                                                sg.Print(msg)
                                                break
                                except Exception as e:
                                    msg='Failed to send message to final exception ' +str(excel_data['Contact'][count]) + str(e)
                                    sg.Print(msg)
                                    msg="XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXx"
                                    sg.Print(msg)

                                finally:
                                        if sent == True:
                                            msg = str(count+1) +". " + str(excel_data['Contact'][count]) + '✔️'
                                            update_log(log, msg)
                                             
                                        else:
                                            if is_invalid == True and sent == False:
                                                msg = str(count+1) +". " +str(excel_data['Contact'][count])+" ❎ invalid user ❎" 
                                                sg.Print(msg)
                                                update_log(log, msg)
                                            else:
                                                msg = str(count+1) +". " +str(excel_data['Contact'][count]) + '❌'
                                                update_log(log, msg)
                                                sg.Print(msg)
                                            
                                            
                                

                            msg = "The script executed successfully."+ '✅'
                            sg.Print(msg)
                    except Exception as e:
                        msg="📁 file related problems "+str(e)
                        sg.Print(msg)
                        
                        
                elif message_type == msg_type[2]:  # sending Images with message-------------------------------------------------------------------
                    log = []
                    try:
                        if excel_path != None and excel_path != '':
                            pass
                        else:
                            ch = sg.popup_ok("Excel is not loaded please select it fist")                    
                            raise Exception('Excel is not loaded 📝')

                        if image_path != None and image_path != '':
                            pass
                        else:
                            ch = sg.popup_ok("image is not loaded please select it fist")
                            raise Exception("image is not loaded 🗄️")

                        count = 0
                        image_upload_time = values['-UPLOAD WAIT-']
                        wait_attachment = values['-WAIT ATTACHMENT-']
                        invalid_wait_time = values['-INVALID WAIT-']

                        rows = len(excel_data.index)
                        window['-PBAR-'].update(current_count=0,max=rows)
                        for count in range(rows):
                            window['-PBAR-'].update(current_count=count+1)
                            window['-OUT-'].update(count+1)
                            if(count==rows):
                                break
                            if(count<rows):
                                try:
                                    url = 'https://web.whatsapp.com/send?phone=' + \
                                    str(excel_data['Contact'][count]) + \
                                            '&text='+ excel_data['Message'][0]
                                    
                                    msg="---------------------------------------------------------"
                                     
                                    sg.Print(msg)
                                    msg=url
                                    sg.Print(msg)
                                    msg=str(count+1)+" number is "+str(excel_data['Contact'][count])
                                    sent = False
                                    # It tries 3 times to send a message in case if there any error occurred
                                    driver.get(url)
                                    attempt = 2
                                    while attempt>0:
                                        try:
                                            try:
                                                
                                                # try to locate send button for sending messages
                                                msg='waiting for attachment button to be clicked max wait '+str(wait_attachment)+" attempt "+str(attempt)
                                                sg.Print(msg)
                                                attempt-=1
                                                
                                                attachment_button = WebDriverWait(driver, wait_attachment).until(EC.element_to_be_clickable((By.XPATH, "//span[@data-testid='clip']")))
                                            except:
                                                msg="error finding attachment button "+" attempt "+str(attempt)
                                                sg.Print(msg)
                                                try:
                                                    msg="Checking for invalid"
                                                    sg.Print(msg)
                                                    number_invalid_btn = WebDriverWait(driver, invalid_wait_time).until(EC.element_to_be_clickable((By.XPATH, "//button[@data-testid='popup-controls-ok']")))
                                                except:        
                                                    driver.get(url)
                                                    msg="giving reload"
                                                    sg.Print(msg)
                                                else:
                                                    number_invalid_btn.click()
                                                    is_invalid =  True
                                                    msg="clicked on invalid button"
                                                    sg.Print(msg)
                                                    break
                                            else:
                                                attachment_button.click()
                                                msg='successfully located and clicked attachment button'+" attempt "+str(attempt)
                                                sg.Print(msg)
                                        
                                        except:
                                            msg='not attachment and not invalid problem'
                                            sg.Print(msg)
                                            break
                                        else:
                                            sleep(2)
                                            msg='locating image attach button'
                                            sg.Print(msg)
                                            try:
                                                image_box = driver.find_element(By.XPATH, "//input[@accept='image/*,video/mp4,video/3gpp,video/quicktime']")
                                            except:
                                                msg="can not click on image attach"
                                                sg.Print(msg)
                                            
                                            else:
                                                msg='clicked on image attach button successfully'
                                                sg.Print(msg)
                                                image_box.send_keys(image_path)
                                                msg='image sent successfully'
                                                sg.Print(msg)
                                                click_btn = WebDriverWait(driver, wait_image).until(EC.element_to_be_clickable((By.XPATH, "//div[@class='p357zi0d gndfcl4n ac2vgrno mh8l8k0y k45dudtp i5tg98hk f9ovudaz przvwfww gx1rr48f f8jlpxt4 hnx8ox4h k17s6i4e ofejerhi os0tgls2 g9p5wyxn i0tg5vk9 aoogvgrq o2zu3hjb hftcxtij rtx6r8la e3b81npk oa9ii99z p1ii4mzz']")))
                                                click_btn.click()
                                                msg='successfully clicked the Image send button'
                                                sg.Print(msg)
                                                msg='waiting for ' +str(wait_image) +' seconds for file upload'
                                                sg.Print(msg)
                                                sent = True
                                                sleep(image_upload_time)
                                                msg='Image sent to: ' + str(excel_data['Contact'][count])
                                                sg.Print(msg)
                                                msg="^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^"
                                                sg.Print(msg)
                                                break
                                except Exception as e:
                                    msg='Failed to send message to final exception ' +str(excel_data['Contact'][count]) + str(e)
                                    sg.Print(msg)
                                    msg="XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXx"
                                    sg.Print(msg)

                                finally:
                                        if sent == True:
                                            msg = str(count+1) +". " + str(excel_data['Contact'][count]) + '✔️'
                                            update_log(log, msg)
                                             
                                        else:
                                            if is_invalid == True and sent == False:
                                                msg = str(count+1) +". " +str(excel_data['Contact'][count])+" ❎ invalid user ❎" 
                                                sg.Print(msg)
                                                update_log(log, msg)
                                            else:
                                                msg = str(count+1) +". " +str(excel_data['Contact'][count]) + '❌'
                                                update_log(log, msg)
                                                sg.Print(msg)
                                            
                                            
                                

                            msg = "The script executed successfully."+ '✅'
                            sg.Print(msg)
                    except Exception as e:
                        msg="📁 file related problems "+str(e)
                        sg.Print(msg)
                    













            except Exception as e:
                sg.Print("something is wrong "+str(e))
        else:
            continue


window.close()

# import pandas as pd
# path = file_path
# # path = str('r"'+ str(file_path[1:]))
# sg.Print(path)

# try:
#     df=pd.read_excel(path)
# except:
#     df= pd.read_csv(path)
# df.head

# path = path.replace('\\','/') # replaces backslashes with forward slashes
# path = path[1:len(path)-1] # to remove quote marks

