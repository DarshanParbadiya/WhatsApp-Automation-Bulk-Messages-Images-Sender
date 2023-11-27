import PySimpleGUI as sg
import os.path

msg_type = ['Send text message only', 'Send Image', 'Send Text and Image Both']
# cssText = {'text_color': 'white', 'background_color': 'green'}
# apply using **cssText
cssStatus = {'border': '1px solid white'}
# sg.theme('BlueMono')
buttons_frame = [[sg.Button('Send', disabled=True),
                  sg.Button('Open WhatsApp')]]


progress_bar = [[sg.ProgressBar(100, orientation='h', expand_x=True, size=(27, 20),  key='-PBAR-'),
                 sg.Text('0', key='-OUT-', enable_events=True,
                         font=('Arial Bold', 16), expand_x=True)
                 ]]
message_type_list = [[sg.Combo(msg_type, expand_x=True, enable_events=True,

                               readonly=True, default_value=msg_type[0], key='-msg type-')]]


time_range = [i for i in range(1, 31)]
wait_attachment = [[sg.Text("Attachment "), sg.Spin(
    time_range, initial_value=10, readonly=True, size=2, enable_events=True, key='-WAIT ATTACHMENT-')]]

message_sender_column = [
    # [sg.Text('choose Excel file or keep it in the same folder')],
    [sg.Frame('Select Message type', message_type_list),
     sg.Frame('Sending buttons', buttons_frame)],
    [sg.Frame('Excel file input', [
        [
            sg.In(size=(42, 1), enable_events=True, key='-excel location-',
                  tooltip='Please select Excel file containing Numbers'),
            sg.FileBrowse(file_types=[('Excel files', '*.xlsx')])
        ],

        [
            sg.Button('Load Excel'),

        ],
    ])],
    [sg.Frame("Progress", progress_bar)],
    [sg.Frame('Status', [[sg.Listbox(values=[], size=(50, 28), key="-status-")]])],
]
image_frame = [
    [
        sg.In(size=(50, 2), enable_events=True, key='-image location-',
              tooltip='Please Select Any file that you want to send'),
        sg.FileBrowse(),
    ],
    [sg.Button('Load Image')],
]


features_frame = [[sg.Button('Stop', disabled=True, tooltip='Stop sending Messages'),
                   sg.Button('Export All numbers with Status',
                             disabled=True, tooltip='Export status to csv file.'),

                   ]]

invalid_wait = [[sg.Text("Invalid Wait"), sg.Spin(
    time_range, initial_value=5, readonly=True, size=2, enable_events=True, key='-INVALID WAIT-', tooltip='Time to validate Invalid Number')]]
upload_wait = [[sg.Text("Upload wait"), sg.Spin(
    time_range, initial_value=10, readonly=True, size=2, enable_events=True, key='-UPLOAD WAIT-', tooltip='Time to wait for file Upload')]]

no_of_attempts = [[sg.Text("Attempts"), sg.Spin(
    time_range, initial_value=2, readonly=True, size=3, enable_events=True, key='-ATTEMPTS-')]]

stop = [[sg.Text("set 1 to stop"), sg.Spin(
    time_range, initial_value=2, readonly=True, size=3, enable_events=True, key='-STOP-')]]

buttons_frame = [[sg.Frame("Invalid wait", invalid_wait), sg.Frame(
    "Upload wait", upload_wait), sg.Frame("Initial wait", wait_attachment)], ]

export_frame = [[sg.Button('Export sent Numbers', disabled=True, tooltip='Export status to csv file.'),
                 sg.Button('Export invalid Numbers', disabled=True,
                           tooltip='Export status to csv file.'),
                 sg.Button('Export not sent Numbers', disabled=True, tooltip='Export status to csv file.')]]

output_column = [
    # [sg.Text('Image Location')],
    [sg.Frame("No of attempts", no_of_attempts), sg.Frame('Stop', stop), sg.Frame(
        "Additional Buttons", features_frame)],
    [sg.Frame("Export Buttons",  export_frame)],
    [sg.Frame("Delay timings", buttons_frame)],



    [sg.Frame('Image Location', image_frame, pad=(0, 10))],



    [sg.Frame('Image Status', [[sg.Listbox(values=[], size=(75, 2),
                                           key="-image status-", horizontal_scroll=True)],])],
    [sg.Frame('Numbers List', [[sg.Listbox(values=[], size=(70, 15),
              key="-numbers list-", horizontal_scroll=True)],])],


]
log_number_sent = [
    [sg.Listbox(values=[], size=(50, 28), key="-log number sent-")]]
log_message_window = [[sg.Listbox(values=[], size=(
    80, 28), key="-log message window-", horizontal_scroll=True)]]

tab1Layout = [[sg.Column(message_sender_column), sg.Column(output_column)]]
tab2Layout = [
    [sg.Frame("Status", log_number_sent), sg.Frame(
        'Send', log_message_window)], [sg.Button('Clear')]
]

#    [sg.Frame('Select Message type',)]


# tab3Layout = [[sg.Image(r'C:/Users/Jagdish Patel/Desktop/whatsapp automation/photo/send.png',subsample=2,key='-image-')]]
# sg.VSeperator(),

layout = [[sg.TabGroup([[sg.Tab('Load Files', tab1Layout), sg.Tab('Instructions', tab2Layout),]])], [sg.Exit()]
          ]


window = sg.Window('WhatsApp messages sender', layout, resizable=True)
excel_path = None
def_excel_path = 'C:/Users/Jagdish Patel/Desktop/whatsapp automation/Recipients data.xlsx'
image_path = None
img_msg = []
excel_msg = []
log = []
log_window_messages = []
all_numbers = []
sent_numbers = []
not_sent_numbers = []
invalid_numbers = []
invisible_emoji = '‍'
# window['Send'].update(disabled=True)


def update_all_numbers(new_number, status):
    all_numbers.append([new_number, status])


def update_sent_numbers(new_number, status):
    sent_numbers.append([new_number, status])


def update_not_sent_numbers(new_number, status):
    not_sent_numbers.append([new_number, status])


def update_invalid_numbers(new_number, status):
    invalid_numbers.append([new_number, status])


def update_log(log, msg):
    # sg.Print(msg)
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

    elif event == 'Stop':
        window['Stop'].update(disabled=True)
        sg.Print('Stopping sending messages')
        break

    elif event == 'Export All numbers with Status':
        import pandas as pd
        import numpy as np
        pd.DataFrame(all_numbers).to_csv('All_Numbers.csv',
                                         index_label="Index", header=['Numbers', 'Status'])

    elif event == 'Export sent Numbers':
        import pandas as pd
        import numpy as np
        pd.DataFrame(sent_numbers).to_csv('Sent_Numbers.csv',
                                          index_label="Index", header=['Numbers', 'Status'])

    elif event == 'Export invalid Numbers':
        import pandas as pd
        import numpy as np
        pd.DataFrame(invalid_numbers).to_csv('invalid_numbers.csv',
                                             index_label="Index", header=['Numbers', 'Status'])

    elif event == 'Export not sent Numbers':
        import pandas as pd
        import numpy as np
        pd.DataFrame(not_sent_numbers).to_csv('not_sent_numbers.csv',
                                              index_label="Index", header=['Numbers', 'Status'])

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
        # sg.Printing numbers in the display
        for i in range(rows):
            numbers.append(str(i+2)+'. ' + str(excel_data['Contact'][i]))
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
            # from selenium import webdriver

            import pandas
            # this is used for lower version of selenium
            # driver = webdriver.Chrome(ChromeDriverManager().install())
            driver = webdriver.Chrome()
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

        window['Export All numbers with Status'].update(disabled=False)
        window['Export sent Numbers'].update(disabled=False)
        window['Export invalid Numbers'].update(disabled=False)
        window['Export not sent Numbers'].update(disabled=False)

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
                    all_numbers = [[0, 0]]
                    sent_numbers = [[0, 0]]
                    not_sent_numbers = [[0, 0]]
                    invalid_numbers = [[0, 0]]

                    try:

                        sg.Print('inside try')
                        if excel_path != None and excel_path != '':
                            pass
                        else:
                            raise Exception('Excel is not loaded 📝')

                        is_same_message = True
                        msg = "do you wish to send same message to everyone \n If yes then press yes\n Press no to send everyone different messages"
                        ch = sg.popup_yes_no(
                            msg, title="Please choose message type")
                        if (ch == 'Yes'):
                            is_same_message = True
                            sg.Print("Same message to everyone")
                        else:
                            is_same_message = False
                            sg.Print("different messages for everyone")

                        # count = 0

                        rows = len(excel_data.index)
                        window['-PBAR-'].update(current_count=0, max=rows)

                        window['Stop'].update(disabled=False)

                        try:
                            for count in range(rows):
                                window['-PBAR-'].update(current_count=count+1)
                                window['-OUT-'].update(count+2)

                                wait_attachment = values['-WAIT ATTACHMENT-']
                                invalid_wait_time = values['-INVALID WAIT-']
                                no_of_attempts = values['-ATTEMPTS-']
                                stop_status = values['-STOP-']
                                if (stop_status == 1):
                                    break

                                if (is_same_message == True):
                                    message = excel_data['Message'][0]
                                    msg = "Sending same message to everyone"
                                    sg.Print(msg)
                                else:
                                    message = excel_data['Message'][count]
                                    msg = "Sending different message to everyone"
                                    sg.Print(msg)

                                if (count == rows):
                                    break
                                if (count < rows):

                                    attempt = 0
                                    sg.Print(
                                        "-------------------------------------------------------")
                                    sg.Print('starting to send message to ' +
                                             str(excel_data['Contact'][count]))
                                    sg.Print(
                                        "-------------------------------------------------------")
                                    while attempt < no_of_attempts:
                                        attempt += 1
                                        msg = 'ATTEMPT NO: ' + \
                                            str(attempt) + '⭕⭕⭕'
                                        sg.Print(msg)
                                        try:

                                            url = 'https://web.whatsapp.com/send?phone=' + \
                                                str(excel_data['Contact'][count]) + \
                                                '&text=' + invisible_emoji

                                            # '❌' '✔️' ' ✅❎📁📝🗄️  '

                                            msg = url
                                            sg.Print(msg)
                                            msg = str(count+2)+". number is " + \
                                                str(excel_data['Contact'][count])
                                            sg.Print(msg)
                                            sent = False
                                            is_invalid = False

                                            driver.get(url)
                                            try:
                                                try:

                                                    try:
                                                        msg = 'trying to find input message box wait ' + \
                                                            str(wait_attachment)
                                                        sg.Print(msg)
                                                        message_text_box = WebDriverWait(driver, wait_attachment).until(
                                                            EC.element_to_be_clickable((By.XPATH, "//span[@class='selectable-text copyable-text']")))
                                                    except Exception as e:
                                                        msg = "can not find input message box because" + \
                                                            str(e)

                                                    else:
                                                        sg.Print(
                                                            'message is '+message)
                                                        message_text_box.send_keys(
                                                            message)
                                                        msg = 'successfully loaded the message'
                                                        sg.Print(msg)

                                                    msg = 'waiting for send button to be clicked max wait ' + \
                                                        str(wait_attachment) + \
                                                        " attempt " + \
                                                        str(attempt)

                                                    click_btn = WebDriverWait(driver, wait_attachment).until(EC.element_to_be_clickable(
                                                        (By.XPATH, "//button[@data-testid='compose-btn-send']")))
                                                    msg = 'successfully located a chat send button'

                                                except:

                                                    msg = "error finding chat button " + \
                                                        " attempt " + \
                                                        str(attempt)
                                                    sg.Print(msg)
                                                    try:
                                                        msg = "Checking for invalid waiting " + \
                                                            str(invalid_wait_time) + " ❎"
                                                        sg.Print(msg)
                                                        number_invalid_btn = WebDriverWait(driver, invalid_wait_time).until(
                                                            EC.element_to_be_clickable((By.XPATH, "//button[@data-testid='popup-controls-ok']")))
                                                    except:

                                                        msg = "not found ❎invalid yet so, to check twice second attempt"
                                                        sg.Print(msg)

                                                    else:
                                                        number_invalid_btn.click()
                                                        is_invalid = True
                                                        msg = "clicked on invalid button ❎"

                                                        sg.Print(msg)
                                                        # msg = 'breaking out of the loop 1, ⭕'
                                                        # sg.Print(msg)
                                                        break

                                            except:
                                                driver.get(url)
                                                sleep(5)
                                                msg = 'not send button and not invalid problem'
                                                sg.Print(msg)
                                            else:
                                                sleep(2)
                                                click_btn.click()

                                                sent = True
                                                sg.Print(
                                                    'clicked on send button successfully')
                                                sleep(5)
                                                msg = 'message sent to: ' + \
                                                    str(excel_data['Contact'][count])
                                                sg.Print(msg)
                                                msg = "✔️✔️✔️✔️✔️✔️✔️✔️✔️✔️"
                                                sg.Print(msg)
                                                msg = str(
                                                    excel_data['Contact'][count]) + '✔️'
                                                sg.Print(msg)

                                                break
                                        except Exception as e:
                                            msg = 'Failed to send message to final exception ' + \
                                                str(excel_data['Contact']
                                                    [count]) + str(e)
                                            sg.Print(msg)
                                            # msg = "❌❌❌❌❌❌❌❌❌❌"
                                            # msg = str(excel_data['Contact'][count]) + '❌' + 'ATTEMPT ' +str(attempt)
                                            # sg.Print(msg)
                                            # msg = 'breaking out of the loop 3, ⭕⭕⭕'
                                            # sg.Print(msg)
                                            # msg = 'value of attempt is '+str(attempt)
                                            # sg.Print(msg)
                                            # msg = "GOING FOR ANOTHER ATTEMPT"

                                        else:
                                            msg = "The script executed successfully." + '✅'
                                            sg.Print(msg)

                                        finally:
                                            if sent == True:
                                                if (attempt == 1):
                                                    msg = str(
                                                        count+2) + ". " + str(excel_data['Contact'][count]) + '✔️'

                                                else:
                                                    all_numbers.pop()
                                                    sent_numbers.pop()
                                                    msg = str(
                                                        count+2) + ". " + str(excel_data['Contact'][count]) + ' ATTEMPT '+str(attempt) + '✔️'
                                                update_log(log, msg)
                                                sg.Print(msg)
                                                update_all_numbers(
                                                    str(excel_data['Contact'][count]), 'Sent')
                                                update_sent_numbers(
                                                    str(excel_data['Contact'][count]), 'Sent')

                                            else:
                                                if is_invalid == True and sent == False:
                                                    if (attempt == 1):
                                                        msg = str(count+2) + ". " + str(
                                                            excel_data['Contact'][count]) + " ❎ invalid user ❎"
                                                    else:
                                                        all_numbers.pop()
                                                        invalid_numbers.pop()
                                                        msg = str(count+2) + ". " + str(
                                                            excel_data['Contact'][count]) + ' ATTEMPT '+str(attempt)+" ❎ invalid user ❎"
                                                    update_log(log, msg)
                                                    sg.Print(msg)

                                                    update_all_numbers(
                                                        str(excel_data['Contact'][count]), 'Invalid')
                                                    update_invalid_numbers(
                                                        str(excel_data['Contact'][count]), 'Invalid')
                                                else:
                                                    if (attempt == 1):
                                                        msg = msg = str(
                                                            count+2) + ". " + str(excel_data['Contact'][count]) + '❌'
                                                    else:
                                                        all_numbers.pop()
                                                        not_sent_numbers.pop()
                                                        msg = str(
                                                            count+2) + ". " + str(excel_data['Contact'][count]) + ' ATTEMPT '+str(attempt) + '❌'
                                                    update_log(log, msg)
                                                    sg.Print(msg)
                                                    update_all_numbers(
                                                        str(excel_data['Contact'][count]), 'Not Sent')
                                                    update_not_sent_numbers(
                                                        str(excel_data['Contact'][count]), 'Not Sent')

                        except:
                            msg = "could not complete all the numbers"
                            sg.Print(msg)
                        else:
                            msg = "The script executed successfully with all the numbers" + '✅'
                            sg.Print(msg)
                    except Exception as e:
                        msg = "📁 file related problems "+str(e)
                        ch = sg.popup_yes_no(
                            msg + " please solve them first ", title="YesNo")
                        if ch == 'Yes':
                            pass
                        else:
                            pass
                        sg.Print(msg)

    # '❌' '✔️' ' ✅❎📁📝🗄️⭕  '

                # sending Images-------------------------------------------------------------------

                elif message_type == msg_type[1]:
                    log = []
                    all_numbers = [[0, 0]]
                    sent_numbers = [[0, 0]]
                    not_sent_numbers = [[0, 0]]
                    invalid_numbers = [[0, 0]]
                    try:
                        if excel_path != None and excel_path != '':
                            pass
                        else:
                            ch = sg.popup_yes_no(
                                "Excel is not loaded please select it fist")
                            if ch == 'Yes':
                                pass
                            else:
                                pass

                            raise Exception('Excel is not loaded 📝')

                        if image_path != None and image_path != '':
                            pass
                        else:
                            ch = sg.popup_yes_no(
                                "image is not loaded please select it fist")
                            if ch == 'Yes':
                                pass
                            else:
                                pass
                            raise Exception("image is not loaded 🗄️")

                        sg.Print(no_of_attempts)
                        rows = len(excel_data.index)
                        window['-PBAR-'].update(current_count=0, max=rows)

                        window['Stop'].update(disabled=False)

                        try:
                            for count in range(rows):
                                window['-PBAR-'].update(current_count=count+1)
                                window['-OUT-'].update(count+2)

                                image_upload_time = values['-UPLOAD WAIT-']
                                wait_attachment = values['-WAIT ATTACHMENT-']
                                invalid_wait_time = values['-INVALID WAIT-']
                                no_of_attempts = values['-ATTEMPTS-']
                                stop_status = values['-STOP-']
                                if (stop_status == 1):
                                    break

                                if (count == rows):
                                    break
                                if (count < rows):
                                    attempt = 0
                                    sg.Print(
                                        "-------------------------------------------------------")
                                    sg.Print('starting to send message to ' +
                                             str(excel_data['Contact'][count]))

                                    while attempt < no_of_attempts:
                                        attempt += 1
                                        msg = 'ATTEMPT NO:'+str(attempt)
                                        sg.Print(msg)
                                        try:

                                            url = 'https://web.whatsapp.com/send?phone=' + \
                                                str(excel_data['Contact'][count])
                                            msg = url
                                            sg.Print(msg)
                                            msg = str(count+1)+" number is " + \
                                                str(excel_data['Contact'][count])
                                            sent = False

                                            driver.get(url)

                                            try:  # validate user and locate attachment button
                                                try:  # try to locate attachment button for sending messages
                                                    msg = 'waiting for attachment button to be clicked max wait ' + \
                                                        str(wait_attachment) + \
                                                        " attempt " + \
                                                        str(attempt)
                                                    sg.Print(msg)
                                                    attachment_button = WebDriverWait(driver, wait_attachment).until(
                                                        EC.element_to_be_clickable((By.XPATH, "//span[@data-testid='clip']")))
                                                except:  # can not locate so checking invalid and terminate if yes
                                                    msg = "error finding attachment button " + \
                                                        " attempt " + \
                                                        str(attempt)
                                                    sg.Print(msg)

                                                    try:  # check invalid
                                                        msg = "Checking for invalid ❎"
                                                        sg.Print(msg)
                                                        number_invalid_btn = WebDriverWait(driver, invalid_wait_time).until(
                                                            EC.element_to_be_clickable((By.XPATH, "//button[@data-testid='popup-controls-ok']")))
                                                    except:

                                                        msg = "not found ❎invalid yet so, to check twice second attempt"
                                                        sg.Print(msg)

                                                    else:
                                                        number_invalid_btn.click()
                                                        is_invalid = True
                                                        msg = "clicked on invalid button ❎"

                                                        sg.Print(msg)
                                                        msg = 'breaking out of the loop 1, ⭕'
                                                        sg.Print(msg)
                                                        break

                                                else:  # click on an attachment button
                                                    attachment_button.click()
                                                    msg = 'successfully located and clicked attachment button' + \
                                                        " attempt " + \
                                                        str(attempt)
                                                    sg.Print(msg)

                                            except:  # not invalid user and unable to located attachment button
                                                msg = 'not attachment and not invalid problem so trying for another attempt'
                                                sg.Print(msg)

                                            else:  # clicked on attachment button
                                                sleep(2)
                                                msg = 'locating image attach button'
                                                sg.Print(msg)
                                                try:  # locating image attach button
                                                    image_box = driver.find_element(
                                                        By.XPATH, "//input[@accept='image/*,video/mp4,video/3gpp,video/quicktime']")
                                                except:  # unable to find image attach button
                                                    msg = "can not click on image attach so going for another attempt"
                                                    sg.Print(msg)
#
                                                else:
                                                    msg = 'located image attach button successfully'
                                                    sg.Print(msg)
                                                    image_box.send_keys(
                                                        image_path)
                                                    msg = 'image loaded successfully'
                                                    sg.Print(msg)
                                                    # ----------------image loaded successfully -------------------
                                                    click_btn = WebDriverWait(driver, image_upload_time).until(EC.element_to_be_clickable(
                                                        (By.XPATH, "//div[@class='p357zi0d gndfcl4n ac2vgrno mh8l8k0y k45dudtp i5tg98hk f9ovudaz przvwfww gx1rr48f f8jlpxt4 hnx8ox4h k17s6i4e ofejerhi os0tgls2 g9p5wyxn i0tg5vk9 aoogvgrq o2zu3hjb hftcxtij rtx6r8la e3b81npk oa9ii99z p1ii4mzz']")))
                                                    click_btn.click()
                                                    msg = 'successfully clicked the Image send button'
                                                    sg.Print(msg)
                                                    sent = True
                                                    msg = 'waiting for ' + \
                                                        str(image_upload_time) + \
                                                        ' seconds for file upload'
                                                    sg.Print(msg)
                                                    sleep(image_upload_time)
                                                    msg = 'Image sent to: ' + \
                                                        str(excel_data['Contact'][count])
                                                    sg.Print(msg)
                                                    msg = "✔️✔️✔️✔️✔️✔️✔️✔️✔️✔️"
                                                    sg.Print(msg)
                                                    break
                                        except Exception as e:
                                            msg = 'Failed to send message to final exception ' + \
                                                str(excel_data['Contact']
                                                    [count]) + " " + str(e)
                                            sg.Print(msg)
                                            msg = "❌❌❌❌❌❌❌❌❌❌"
                                            sg.Print(msg)

                                        finally:
                                            if sent == True:
                                                if (attempt == 1):
                                                    msg = str(
                                                        count+2) + ". " + str(excel_data['Contact'][count]) + '✔️'
                                                else:
                                                    all_numbers.pop()
                                                    sent_numbers.pop()
                                                    msg = str(
                                                        count+2) + ". " + str(excel_data['Contact'][count]) + ' ATTEMPT '+str(attempt) + '✔️'
                                                update_log(log, msg)
                                                sg.Print(msg)
                                                update_all_numbers(
                                                    str(excel_data['Contact'][count]), 'Sent')
                                                update_sent_numbers(
                                                    str(excel_data['Contact'][count]), 'Sent')
                                            else:
                                                if is_invalid == True and sent == False:
                                                    if (attempt == 1):
                                                        msg = str(count+2) + ". " + str(
                                                            excel_data['Contact'][count]) + " ❎ invalid user ❎"
                                                    else:
                                                        all_numbers.pop()
                                                        invalid_numbers.pop()
                                                        msg = str(count+2) + ". " + str(
                                                            excel_data['Contact'][count]) + ' ATTEMPT '+str(attempt)+" ❎ invalid user ❎"
                                                    update_log(log, msg)
                                                    sg.Print(msg)
                                                    update_all_numbers(
                                                        str(excel_data['Contact'][count]), 'Invalid')
                                                    update_invalid_numbers(
                                                        str(excel_data['Contact'][count]), 'Invalid')

                                                else:
                                                    if (attempt == 1):
                                                        msg = msg = str(
                                                            count+2) + ". " + str(excel_data['Contact'][count]) + '❌'
                                                    else:
                                                        all_numbers.pop()
                                                        not_sent_numbers.pop()
                                                        msg = str(
                                                            count+2) + ". " + str(excel_data['Contact'][count]) + ' ATTEMPT '+str(attempt) + '❌'
                                                    update_log(log, msg)
                                                    sg.Print(msg)
                                                    update_all_numbers(
                                                        str(excel_data['Contact'][count]), 'Not Sent')
                                                    update_not_sent_numbers(
                                                        str(excel_data['Contact'][count]), 'Not Sent')

                        except:
                            msg = "could not complete all the numbers"
                        else:
                            msg = "The script executed successfully with all the numbers" + '✅'
                            sg.Print(msg)
                    except Exception as e:
                        msg = "📁 file related problems "+str(e)
                        sg.Print(msg)

                # sending Images with message-------------------------------------------------------------------
                elif message_type == msg_type[2]:
                    log = []
                    all_numbers = [[0, 0]]
                    sent_numbers = [[0, 0]]
                    not_sent_numbers = [[0, 0]]
                    invalid_numbers = [[0, 0]]
                    try:
                        if excel_path != None and excel_path != '':
                            pass
                        else:
                            ch = sg.popup_yes_no(
                                "Excel is not loaded please select it fist")
                            if ch == 'Yes':
                                pass
                            else:
                                pass

                            raise Exception('Excel is not loaded 📝')

                        if image_path != None and image_path != '':
                            pass
                        else:
                            ch = sg.popup_yes_no(
                                "image is not loaded please select it fist")
                            if ch == 'Yes':
                                pass
                            else:
                                pass
                            raise Exception("image is not loaded 🗄️")

                        is_same_message = True
                        msg = "do you wish to send same message to everyone \n If yes then press yes\n Press no to send everyone different messages"
                        ch = sg.popup_yes_no(
                            msg, title="Please choose message type")
                        if (ch == 'Yes'):
                            is_same_message = True
                            sg.Print("Same message to everyone")
                        else:
                            is_same_message = False
                            sg.Print("different messages for everyone")

                        count = 0

                        rows = len(excel_data.index)
                        window['-PBAR-'].update(current_count=0, max=rows)

                        window['Stop'].update(disabled=False)

                        try:
                            for count in range(rows):
                                window['-PBAR-'].update(current_count=count+1)
                                window['-OUT-'].update(count+2)

                                image_upload_time = values['-UPLOAD WAIT-']
                                wait_attachment = values['-WAIT ATTACHMENT-']
                                invalid_wait_time = values['-INVALID WAIT-']
                                no_of_attempts = values['-ATTEMPTS-']

                                stop_status = values['-STOP-']
                                if (stop_status == 1):
                                    break

                                if (is_same_message == True):
                                    sg.Print('sending the same message')
                                    message = excel_data['Message'][0]
                                else:
                                    message = excel_data['Message'][count]
                                    sg.Print('sending : '+message)

                                if (count == rows):
                                    break
                                if (count < rows):
                                    attempt = 0
                                    sg.Print(
                                        "-------------------------------------------------------")
                                    sg.Print('starting to send message to ' +
                                             str(excel_data['Contact'][count]))
                                    while attempt < 2:
                                        attempt += 1
                                        msg = 'ATTEMPT NO:'+str(attempt)
                                        sg.Print(msg)

                                        try:
                                            url = 'https://web.whatsapp.com/send?phone=' + \
                                                str(excel_data['Contact'][count]) + \
                                                '&text=' + invisible_emoji

                                            msg = url
                                            sg.Print(msg)
                                            msg = str(count+1)+" number is " + \
                                                str(excel_data['Contact'][count])
                                            sent = False
                                            # It tries 3 times to send a message in case if there any error occurred
                                            driver.get(url)

                                            try:  # validate user and locate attachment button
                                                try:  # try to locate attachment button for sending messages
                                                    try:  # trying to load the message
                                                        msg = 'trying to find input message box wait ' + \
                                                            str(wait_attachment)
                                                        sg.Print(msg)
                                                        message_text_box = WebDriverWait(driver, wait_attachment).until(
                                                            EC.element_to_be_clickable((By.XPATH, "//span[@class='selectable-text copyable-text']")))
                                                    except Exception as e:
                                                        msg = "can not find input message box because" + \
                                                            str(e)

                                                        sg.Print(msg)
                                                        try:
                                                            msg = "Checking for invalid ❎"
                                                            sg.Print(msg)
                                                            number_invalid_btn = WebDriverWait(driver, invalid_wait_time).until(
                                                                EC.element_to_be_clickable((By.XPATH, "//button[@data-testid='popup-controls-ok']")))
                                                        except:

                                                            msg = "not found ❎invalid yet so, to check twice second attempt"
                                                            sg.Print(msg)

                                                        else:
                                                            number_invalid_btn.click()
                                                            is_invalid = True
                                                            msg = "clicked on invalid button ❎"

                                                            sg.Print(msg)
                                                            msg = 'Not going for second attempt because of invalid, ⭕'
                                                            sg.Print(msg)
                                                            break

                                                    else:
                                                        sg.Print(
                                                            'message is '+message)
                                                        message_text_box.send_keys(
                                                            message)
                                                        msg = 'successfully loaded the message'
                                                        sg.Print(msg)

                                                    msg = 'waiting for attachment button to be clicked max wait ' + \
                                                        str(wait_attachment) + \
                                                        " attempt " + \
                                                        str(attempt)
                                                    sg.Print(msg)
                                                    attachment_button = WebDriverWait(driver, wait_attachment).until(
                                                        EC.element_to_be_clickable((By.XPATH, "//span[@data-testid='clip']")))
                                                except:  # can not locate so checking invalid and terminate if yes
                                                    msg = "error finding attachment button " + \
                                                        " attempt " + \
                                                        str(attempt)
                                                    sg.Print(msg)

                                                    try:  # check invalid
                                                        msg = "Checking for invalid ❎"
                                                        sg.Print(msg)
                                                        number_invalid_btn = WebDriverWait(driver, invalid_wait_time).until(
                                                            EC.element_to_be_clickable((By.XPATH, "//button[@data-testid='popup-controls-ok']")))
                                                    except:

                                                        msg = "not found ❎invalid yet so, to check twice second attempt"
                                                        sg.Print(msg)

                                                    else:
                                                        number_invalid_btn.click()
                                                        is_invalid = True
                                                        msg = "clicked on invalid button ❎"

                                                        sg.Print(msg)
                                                        msg = 'breaking out of the loop 1, ⭕'
                                                        sg.Print(msg)
                                                        break

                                                else:  # click on an attachment button
                                                    attachment_button.click()
                                                    msg = 'successfully located and clicked attachment button' + \
                                                        " attempt " + \
                                                        str(attempt)
                                                    sg.Print(msg)

                                            except:  # not invalid user and unable to located attachment button
                                                msg = 'not attachment and not invalid problem so trying for another attempt'
                                                sg.Print(msg)

                                            else:  # clicked on attachment button
                                                sleep(2)
                                                msg = 'locating image attach button'
                                                sg.Print(msg)
                                                try:  # locating image attach button
                                                    image_box = driver.find_element(
                                                        By.XPATH, "//input[@accept='image/*,video/mp4,video/3gpp,video/quicktime']")
                                                except:  # unable to find image attach button
                                                    msg = "can not click on image attach so going for another attempt"
                                                    sg.Print(msg)
                                                else:
                                                    msg = 'located image attach button successfully'
                                                    sg.Print(msg)
                                                    image_box.send_keys(
                                                        image_path)
                                                    msg = 'image loaded successfully'
                                                    sg.Print(msg)
                                                    # ----------------image loaded successfully -------------------
                                                    click_btn = WebDriverWait(driver, image_upload_time).until(EC.element_to_be_clickable(
                                                        (By.XPATH, "//div[@class='p357zi0d gndfcl4n ac2vgrno mh8l8k0y k45dudtp i5tg98hk f9ovudaz przvwfww gx1rr48f f8jlpxt4 hnx8ox4h k17s6i4e ofejerhi os0tgls2 g9p5wyxn i0tg5vk9 aoogvgrq o2zu3hjb hftcxtij rtx6r8la e3b81npk oa9ii99z p1ii4mzz']")))
                                                    click_btn.click()
                                                    msg = 'successfully clicked the Image send button'
                                                    sg.Print(msg)
                                                    sent = True
                                                    msg = 'waiting for ' + \
                                                        str(image_upload_time) + \
                                                        ' seconds for file upload'
                                                    sg.Print(msg)
                                                    sleep(image_upload_time)
                                                    msg = 'Image sent to: ' + \
                                                        str(excel_data['Contact'][count])
                                                    sg.Print(msg)
                                                    msg = "✔️✔️✔️✔️✔️✔️✔️✔️✔️✔️"
                                                    sg.Print(msg)
                                                    break
                                        except Exception as e:
                                            msg = 'Failed to send message to final exception ' + \
                                                str(excel_data['Contact']
                                                    [count]) + str(e)
                                            sg.Print(msg)
                                            msg = "❌❌❌❌❌❌❌❌❌❌"
                                            sg.Print(msg)

                                        finally:
                                            if sent == True:
                                                if (attempt == 1):
                                                    msg = str(
                                                        count+2) + ". " + str(excel_data['Contact'][count]) + '✔️'
                                                else:
                                                    all_numbers.pop()
                                                    sent_numbers.pop()
                                                    msg = str(
                                                        count+2) + ". " + str(excel_data['Contact'][count]) + ' ATTEMPT '+str(attempt) + '✔️'
                                                update_log(log, msg)
                                                sg.Print(msg)
                                                update_all_numbers(
                                                    str(excel_data['Contact'][count]), 'Sent')
                                                update_sent_numbers(
                                                    str(excel_data['Contact'][count]), 'Sent')

                                            else:
                                                if is_invalid == True and sent == False:
                                                    if (attempt == 1):
                                                        msg = str(count+2) + ". " + str(
                                                            excel_data['Contact'][count]) + " ❎ invalid user ❎"
                                                    else:
                                                        all_numbers.pop()
                                                        invalid_numbers.pop()
                                                        msg = str(count+2) + ". " + str(
                                                            excel_data['Contact'][count]) + ' ATTEMPT '+str(attempt)+" ❎ invalid user ❎"
                                                    update_log(log, msg)
                                                    sg.Print(msg)
                                                    update_all_numbers(
                                                        str(excel_data['Contact'][count]), 'Invalid')
                                                    update_invalid_numbers(
                                                        str(excel_data['Contact'][count]), 'Invalid')

                                                else:
                                                    if (attempt == 1):
                                                        msg = msg = str(
                                                            count+2) + ". " + str(excel_data['Contact'][count]) + '❌'
                                                    else:
                                                        all_numbers.pop()
                                                        not_sent_numbers.pop()
                                                        msg = str(
                                                            count+2) + ". " + str(excel_data['Contact'][count]) + ' ATTEMPT '+str(attempt) + '❌'
                                                    update_log(log, msg)
                                                    sg.Print(msg)
                                                    update_all_numbers(
                                                        str(excel_data['Contact'][count]), 'Not Sent')
                                                    update_not_sent_numbers(
                                                        str(excel_data['Contact'][count]), 'Not Sent')

                        except:
                            msg = "could not complete all the numbers"
                        else:
                            msg = "The script executed successfully with all the numbers" + '✅'
                            sg.Print(msg)
                    except Exception as e:
                        msg = "📁 file related problems "+str(e)
                        sg.Print(msg)

            except Exception as e:
                sg.Print("something is wrong "+str(e))
        else:
            continue


window.close()
