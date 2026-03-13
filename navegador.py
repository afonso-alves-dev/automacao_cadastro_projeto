
import pyautogui
import time
from config import URL

def abrir_site():
    pyautogui.press("win")
    pyautogui.write("chrome")
    pyautogui.press("enter")

    time.sleep(2)

    pyautogui.write(URL)
    pyautogui.press("enter")

    time.sleep(3)
