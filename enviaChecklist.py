import time
import pyautogui
import keyboard

totalSalas = 40

pyautogui.keyDown('win')
pyautogui.press('1')
pyautogui.keyUp('win')

for o in range(totalSalas + 1):

    pyautogui.press('enter')

    pyautogui.keyDown('ctrl')
    pyautogui.press('pgdn')
    pyautogui.keyUp('ctrl')

for i in range(totalSalas + 1):

    pyautogui.keyDown('ctrl')
    pyautogui.press('w')
    pyautogui.keyUp('ctrl')