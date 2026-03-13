
import pyautogui
from navegador import abrir_site
from cadastro import login, cadastrar_produtos

pyautogui.PAUSE = 1

print("Iniciando automação em 3 segundos...")
import time
time.sleep(3)

abrir_site()
login()
cadastrar_produtos()

print("Automação finalizada.")
