import os
import pyautogui
import time 
import threading

def execute_process():
    #Open the VM Network Editor Software 
    path = "C:\Program Files (x86)\VMware\VMware Workstation"
    os.chdir(path)
    os.system("vmnetcfg.exe")


def GUI_Navagation():
    #Move the cursor and change the subnet addres
    pyautogui.moveTo(759,362, duration=4)          
    pyautogui.click(759,362)
    pyautogui.moveTo(846,710, duration=3) 
    pyautogui.click(846,710)
    for i in  range(10):
      pyautogui.press("backspace")
    time.sleep(3)
    pyautogui.write("1921680")
    pyautogui.press("space")
    pyautogui.write("0")
    pyautogui.moveTo(981,762, duration=1) 
    pyautogui.click(981,762)
# Threads to executes tasks 1 & 2

thread_1 = threading.Thread(target=execute_process)
thread_2 = threading.Thread(target=GUI_Navagation)



#Threads - Start
thread_1.start()
thread_2.start()
#Threads - Join
thread_1.join()
thread_2.join()

exit()

