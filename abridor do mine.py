import pyautogui
import time

crafting_slots = [
    (902, 335),  # slot 1
    (937, 336),  # slot 2
    (915, 369),  # slot 3
    (936, 365),  # slot 4
]

pyautogui.press('win')
time.sleep(0.7)
pyautogui.write('tlaucher')
pyautogui.press('enter')
time.sleep(28)
pyautogui.click(x=847, y=749) # iniciou o laucher
time.sleep(65)
pyautogui.click(x=726, y=414) # abriu o menu
time.sleep(2)
pyautogui.click(x=483, y=323)
time.sleep(2)
pyautogui.click(x=483, y=323) # clicou no triangulo de iniciar
time.sleep(15)
pyautogui.mouseDown(x=483, y=323)  # Pressiona o botão do mouse
time.sleep(5)                     
pyautogui.mouseUp(x=483, y=323)    # Solta o botão do mouse
pyautogui.press('e')
# Espera o inventário abrir
time.sleep(1)

# Arraste o bloco de madeira bruta para a área de crafting 
pyautogui.moveTo(x=737, y=581)  # posição do bloco de madeira no inventário
pyautogui.mouseDown()
time.sleep(0.2)
pyautogui.moveTo(x=902, y=335)  # posição da área de crafting
pyautogui.mouseUp()
time.sleep(0.5)

# Clique para pegar as tábuas de madeira (resultado do crafting)
pyautogui.moveTo(x=1020, y=353)  # posição do resultado do crafting
pyautogui.click()
time.sleep(0.2)

# Coloque as tábuas de volta no inventário
pyautogui.moveTo(x=737, y=581)  # posição livre no inventário
pyautogui.click()
time.sleep(0.2)

# Fecha o inventário
# pyautogui.press('e')

# Supondo que as tábuas estão agora em (650, 650) no inventário
# Arraste uma tábua para cada slot do crafting 2x2 

for slot in crafting_slots:
    pyautogui.moveTo(x=737, y=581)  # posição das tábuas no inventário
    pyautogui.mouseDown()
    time.sleep(0.1)
    pyautogui.moveTo(slot[0], slot[1])
    pyautogui.mouseUp()
    time.sleep(0.1)

# Clique para pegar a crafting table
pyautogui.moveTo(x=1020, y=353)  # posição do resultado do crafting
pyautogui.click()
time.sleep(0.2)

# Coloque a crafting table em um slot livre do inventário
pyautogui.moveTo(x=737, y=581)  # posição livre no inventário
pyautogui.click()
time.sleep(0.2)

# Fecha o inventário
pyautogui.press('e')