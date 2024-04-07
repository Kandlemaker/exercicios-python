import pyautogui

pyautogui.PAUSE = 1
#abrir a lixeira
pyautogui.press("win")
pyautogui.write("lixeira")
pyautogui.press("backspace")
pyautogui.press("enter")
#selecionar e deletar
pyautogui.hotkey('ctrl', 'a')
pyautogui.press("delete")
pyautogui.press("enter")