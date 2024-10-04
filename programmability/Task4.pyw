import pyautogui
import time 
import threading

#Netowrk Bridge Configuration

def execute_process():
    pass

def GUI_Navagation():
    pyautogui.moveTo(464,310, duration=1)
    pyautogui.doubleClick(464,310)
    #Move the cursor
    time.sleep(2)
    pyautogui.moveTo(722,211, duration=1)
    pyautogui.doubleClick(722,211)

    pyautogui.moveTo(424,82)
    time.sleep(0.5)
    pyautogui.doubleClick(424,82)

    pyautogui.moveTo(109,117,duration=1)
    pyautogui.doubleClick(109,117)
    
    # Currently in the Network Connections page
    pyautogui.moveTo(500,334,duration=1)
    pyautogui.doubleClick(500,334)


    pyautogui.moveTo(650,135,duration=1)
    pyautogui.doubleClick(650,135)

    pyautogui.moveTo(848,699,duration=1)
    pyautogui.doubleClick(848,699)

    pyautogui.moveTo(1119,505,duration=1)
    for i in range (15):
        pyautogui.doubleClick(1119,505)

    pyautogui.moveTo(847,484,duration=1)
    pyautogui.doubleClick(847,484)

    pyautogui.moveTo(1032,795,duration=1)
    pyautogui.doubleClick(1032,795)

    pyautogui.moveTo(1091, 745,duration=1)
    pyautogui.doubleClick(1091, 745)
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

