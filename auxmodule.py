import pyautogui
from datetime import datetime, timedelta
from constants import *
import keyboard


# Ищет кнопку на экране и кликает
def findNClick(path, confidence=CONFIDENCE, timer=TIMER):
    status = DEFAULT
    start = datetime.now()
    end = start + timedelta(seconds=timer)
    while start < end:
        button = pyautogui.locateOnScreen(path, confidence)
        if button:
            pyautogui.click(button)
            status = COMPLETED
            return status
        start = datetime.now()
        pyautogui.sleep(SLEEP)
    return status


# Наводит на ссылку и нажимает на появившуюся ссылку на твиттер
def moveToNClick(link_path, button_path, confidence=CONFIDENCE, timer=TIMER):
    status = DEFAULT

    start = datetime.now()
    end = start + timedelta(seconds=timer)
    while start < end:
        link = pyautogui.locateOnScreen(link_path, confidence)
        if link:
            pyautogui.moveTo(link)
            status = findNClick(button_path, confidence, TIMER_FAST)
            return status
        start = datetime.now()
        pyautogui.sleep(SLEEP)

    return FLAG


# page down
def pageDown(path, count=1):
    status = DEFAULT

    start_time = datetime.now()
    stop_time = start_time + timedelta(seconds=TIMER)
    while start_time < stop_time:
        page = pyautogui.locateOnScreen(path, confidence=CONFIDENCE)
        if page:
            option = pyautogui.locateOnScreen(OPTIONS, confidence=CONFIDENCE)
            if option:
                pyautogui.moveTo(option)
                pyautogui.sleep(1)
                while count > 0:
                    keyboard.send("pagedown")
                    count -= 1
                status = COMPLETED
            break
        start_time = datetime.now()
        pyautogui.sleep(SLEEP)

    return FLAG


# Закрывает вкладку
def closeTab():
    with pyautogui.hold('ctrl'):
        pyautogui.press('w')
        

def check(path, timer=TIMER_LONG):
    flag = 0
    start = datetime.now()
    end = start + timedelta(seconds=timer)
    while start < end:
        text = pyautogui.locateOnScreen(path, confidence=CONFIDENCE)
        if text:
            flag = 1
            break
        start = datetime.now()
        pyautogui.sleep(0.2)
    return flag

    
