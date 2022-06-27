import time
import pyautogui
import keyboard

totalSalas = 26
salas26 = 23
salas27 = 4
huddle26 = '26HR'
huddle27 = '27HR'
numeroSala = 1

#Testes ou coisas mal sucedidas:
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

#Preenche o 26º andar
for i in range(salas26):
    
    pyautogui.press('tab')
    pyautogui.press('tab')
    
    for l in range(3):
        pyautogui.press('down')
    
    pyautogui.press('tab')
    
    for m in range(4):
        pyautogui.press('down')

    pyautogui.press('tab')

    #Estrutura de completamento do número da sala

    if numeroSala == 8:
        numeroSala = numeroSala + 1
    
    if numeroSala == 21:
        numeroSala = numeroSala + 1

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
    if numeroSala == 3:
        pyautogui.write('Reservada para Elaine')
    elif numeroSala == 10:
        pyautogui.write('Sala bloqueada')
    elif numeroSala == 11:
        pyautogui.write('Sala bloqueada')
    
    time.sleep(0.15)

    pyautogui.press('tab')

    #muda de aba
    pyautogui.keyDown('ctrl')
    pyautogui.press('pgdn')
    pyautogui.keyUp('ctrl')

    #incrementa o numero da sala
    numeroSala = numeroSala + 1

#zerando as variáveis para garantir o funcionamento
numeroSala = 1
i = 0
j = 0
k = 0
l = 0
m = 0

#Preenche o check do 27º andar
for n in range(salas27):
    
    pyautogui.press('tab')
    pyautogui.press('tab')
    
    for l in range(3):
        pyautogui.press('down')
    
    pyautogui.press('tab')
    
    for m in range(4):
        pyautogui.press('down')

    pyautogui.press('tab')

    pyautogui.write(str(huddle27)+"0"+str(numeroSala))

    for k in range(11):
        pyautogui.press('tab')
        pyautogui.press('space')
    
    pyautogui.press('tab')

    time.sleep(0.15)

    pyautogui.write('Ok')

    time.sleep(0.15)

    pyautogui.press('tab')
    pyautogui.press('space')

    time.sleep(0.15)

    pyautogui.press('tab')

    pyautogui.write('Bloqueada para reforma')

    pyautogui.press('tab')

    #muda de aba
    pyautogui.keyDown('ctrl')
    pyautogui.press('pgdn')
    pyautogui.keyUp('ctrl')

    numeroSala = numeroSala + 1

#Prepara as abas para conferencia
for o in range(totalSalas + 1):

    pyautogui.press('pgup')
    pyautogui.press('pgup')
    pyautogui.press('pgup')

    pyautogui.keyDown('ctrl')
    pyautogui.press('pgdn')
    pyautogui.keyUp('ctrl')


