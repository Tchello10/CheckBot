import time
import pyautogui
import keyboard

totalSalas = 26

pyautogui.keyDown('win')
pyautogui.press('1')
pyautogui.keyUp('win')

#Prepara as abas para conferencia
for o in range(totalSalas + 1):

    pyautogui.press('pgup')
    pyautogui.press('pgup')
    pyautogui.press('pgup')

    pyautogui.keyDown('ctrl')
    pyautogui.press('pgdn')
    pyautogui.keyUp('ctrl')


