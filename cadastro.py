
import pyautogui
import pandas as pd
import time
from config import EMAIL, SENHA

def login():

    pyautogui.click(x=487, y=362)
    pyautogui.write(EMAIL)

    pyautogui.press("tab")
    pyautogui.write(SENHA)

    pyautogui.press("tab")
    pyautogui.press("enter")

    time.sleep(3)


def cadastrar_produtos():

    tabela = pd.read_csv("data/produtos.csv")

    for linha in tabela.index:

        pyautogui.click(x=474, y=263)

        dados = tabela.loc[linha]

        pyautogui.write(str(dados["codigo"]))
        pyautogui.press("tab")

        pyautogui.write(str(dados["marca"]))
        pyautogui.press("tab")

        pyautogui.write(str(dados["tipo"]))
        pyautogui.press("tab")

        pyautogui.write(str(dados["categoria"]))
        pyautogui.press("tab")

        pyautogui.write(str(dados["preco_unitario"]))
        pyautogui.press("tab")

        pyautogui.write(str(dados["custo"]))
        pyautogui.press("tab")

        obs = "" if pd.isna(dados["obs"]) else str(dados["obs"])
        pyautogui.write(obs)

        pyautogui.press("tab")
        pyautogui.press("enter")

        pyautogui.scroll(5000)
