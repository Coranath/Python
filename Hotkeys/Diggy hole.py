import pyautogui

for i in range(10):
    pyautogui.moveTo(100,100, duration=1)
    pyautogui.moveTo(200,100, duration=1)
    pyautogui.moveTo(200,200, duration=1)
    pyautogui.moveTo(100,200, duration=1)