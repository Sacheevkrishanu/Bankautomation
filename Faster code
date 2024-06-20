import rpa as r
import pyautogui
import smtplib
import time


r.init()

r.url('https://netbanking.hdfcbank.com/netbanking/')

imageLocation = 'C:\\Users\\SACHEEV\\Documents\\Bank statment automation'

r.run(f'explorer "{imageLocation}"')
r.wait()

customerid = 'customerid.jpg'
continuee = 'continue.jpg'
password = 'password.jpg'
password2 = 'password2.jpg'
login = 'login.jpg'
savingsaccount = 'savingsaccount.jpg'
view = 'view.jpg'
printt = 'print this page.jpg'
save = 'save.jpg'
logout = 'logout.jpg'

def locate_and_click(image_file, confidence=0.9, double_click=False, text_to_type=None, timeout=30):
   
    start_time = time.time()
    while time.time() - start_time < timeout:
        location = pyautogui.locateOnScreen(f'{imageLocation}\\{image_file}', confidence=confidence)
        if location:
            center = pyautogui.center(location)
            pyautogui.moveTo(center)
            if double_click:
                pyautogui.doubleClick()
            else:
                pyautogui.click()
            print(f'Clicked on the image file: {image_file}')

            if text_to_type:
                pyautogui.typewrite(text_to_type)
                print(f'Typed text: {text_to_type}')
            return True
        time.sleep(1)
    print(f'Image file {image_file} not found on the screen within timeout period.')
    return False

# Use the locate_and_click function to automate the login and other operations
if locate_and_click(customerid, double_click=True, text_to_type='xxxxxxx'):
    pyautogui.press('enter')
    if locate_and_click(password, text_to_type='xxxxxx') or locate_and_click(password2, text_to_type='xxxxxxx'):
        if locate_and_click(login):
            if locate_and_click(savingsaccount):
                if locate_and_click(view):
                    if locate_and_click(printt):
                        if locate_and_click(save):
                            pyautogui.press('enter')
                            pyautogui.hotkey('alt', 'y')
                            if locate_and_click(logout):
                                server = smtplib.SMTP('smtp.gmail.com', 587)
                                server.starttls()
                                server.login('senders email', '16 character key')
                                server.sendmail('senders email', 'receivers email', 'g - drive link')
                                print('Mail sent')

r.close()
