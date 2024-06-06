import rpa as r
import pyautogui
import time
import smtplib

r.init()




r.url('https://netbanking.hdfcbank.com/netbanking/')
r.wait()

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




def locate_and_click(image_file, confidence=0.9, double_click=False, text_to_type=None):
    location = pyautogui.locateOnScreen(f'{imageLocation}\\{image_file}', confidence=confidence)
    if location:
        center = pyautogui.center(location)
        pyautogui.moveTo(center)
        if double_click:
            pyautogui.doubleClick()
        else:
            pyautogui.click()
        print(f'Clicked on the image file: {image_file}')

        time.sleep(2)

        if text_to_type:
            pyautogui.typewrite(text_to_type)
            print(f'Typed text: {text_to_type}')
        time.sleep(2)  
        return True
    else:
        print(f'Image file {image_file} not found on the screen.')
        return False

if locate_and_click(customerid, double_click= True, text_to_type='xxxxxxx'):
    time.sleep(5)
    pyautogui.press('enter')
    time.sleep(5)
    if locate_and_click(password, text_to_type='xxxxxx') or locate_and_click(password2, text_to_type='xxxxxxx'):
        time.sleep(5)
        if locate_and_click(login):
            time.sleep(5)
            if locate_and_click(savingsaccount):
                time.sleep(5)
                if locate_and_click(view):
                    time.sleep(5)
                    if locate_and_click(printt):
                        time.sleep(5)
                        if locate_and_click(save):
                            time.sleep(2)
                            pyautogui.press('enter')
                            pyautogui.hotkey('alt', 'y')
                            time.sleep(7)
                            if locate_and_click(logout):
                                time.sleep(5)
                                

                                
                                server = smtplib.SMTP('smtp.gmail.com', 587)
                                server.starttls()

                                server.login('senders email', '16 character key')

                                server.sendmail('senders email', 'recievers email', 'g - drive link')
                                print('Mail sent')



time.sleep(5)  


                                
                               


r.close()
