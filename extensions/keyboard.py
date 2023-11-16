import pyautogui

def mouseKey(key:int):
    if(key == 0):
        pyautogui.click()
    elif(key == 1):
        pyautogui.rightClick()
    else:
        pyautogui.middleClick()

    

def tab():
    pyautogui.keyDown('tab')
    pyautogui.keyUp('tab')

def enter():
    pyautogui.keyDown('enter')
    pyautogui.keyUp('enter')


def down():
    pyautogui.keyDown('down')
    pyautogui.keyUp('down')

def new_tab():
    pyautogui.keyDown('ctrl')
    pyautogui.keyDown('n')
    pyautogui.keyUp('ctrl')
    pyautogui.keyUp('n')

def select_all():
    pyautogui.keyDown('ctrl')
    pyautogui.keyDown('a')
    pyautogui.keyUp('ctrl')
    pyautogui.keyUp('a')

def copy():
    pyautogui.keyDown('ctrl')
    pyautogui.keyDown('c')
    pyautogui.keyUp('ctrl')
    pyautogui.keyUp('c')

def paste():
    pyautogui.keyDown('ctrl')
    pyautogui.keyDown('v')
    pyautogui.keyUp('ctrl')
    pyautogui.keyUp('v')

def close_tab():
    pyautogui.keyDown('ctrl')
    pyautogui.keyDown('w')
    pyautogui.keyUp('ctrl')
    pyautogui.keyUp('w')

def search():
    pyautogui.keyDown('ctrl')
    pyautogui.keyDown('alt')
    pyautogui.keyDown('n')
    pyautogui.keyUp('ctrl')
    pyautogui.keyUp('alt')
    pyautogui.keyUp('n')
def write(msg:str, speed=0.20):
    pyautogui.write(msg, interval=speed)
