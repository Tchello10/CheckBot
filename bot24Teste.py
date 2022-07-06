import time
import pyautogui
import keyboard

totalSalas = 14
salas24 = 14
salas26 = 23
salas27 = 4
huddle24 = '24HR'
huddle26 = '26HR'
huddle27 = '27HR'
numeroSala = 1

#Zona de Testes
    #paraBot = 0
    #print(pyautogui.position())

#Abre o OperaGX
pyautogui.keyDown('win')
pyautogui.press('1')
pyautogui.keyUp('win')

time.sleep(5)

#Abre todas as guias do checklist
for j in range(totalSalas):
    pyautogui.middleClick(x=339, y=82)
    time.sleep(0.20)
pyautogui.click(x=339, y=82)

time.sleep(5)

#Preenche o 24º andar
for o in range(salas24):
       
    pyautogui.press('tab')
    pyautogui.press('tab')
    
    for l in range(4):
        pyautogui.press('down')
    
    pyautogui.press('tab')
    
    for m in range(4):
        pyautogui.press('down')

    pyautogui.press('tab')

    #Estrutura de completamento do número da sala

    if numeroSala == 8:
        numeroSala = numeroSala + 1

    elif numeroSala == 12:
        numeroSala = numeroSala + 4

    if numeroSala<10:
        pyautogui.write(str(huddle26)+"0"+str(numeroSala))
    
    elif numeroSala>=10:
        pyautogui.write(str(huddle26)+str(numeroSala))
    
    for k in range(11):
        pyautogui.press('tab')
        pyautogui.press('space')
        time.sleep(0.15)
    
    pyautogui.press('tab')

    time.sleep(0.15)

    pyautogui.write('Ok')

    time.sleep(0.15)

    pyautogui.press('tab')
    pyautogui.press('space')

    time.sleep(0.15)

    pyautogui.press('tab')

    #Demarcação de casos especiais de preenchimento
    
    time.sleep(0.15)

    pyautogui.press('tab')

    #muda de aba
    pyautogui.keyDown('ctrl')
    pyautogui.press('pgdn')
    pyautogui.keyUp('ctrl')

    #incrementa o numero da sala
    numeroSala = numeroSala + 1