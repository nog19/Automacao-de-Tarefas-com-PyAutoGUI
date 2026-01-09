import pyautogui
import time

pyautogui.PAUSE = 0.8
pyautogui.press ('win')
pyautogui.write('chrome')
pyautogui.press('enter')
time.sleep(0.8) 
pyautogui.click(x=800, y=499)
pyautogui.press('enter')
pyautogui.write('https://www.youtube.com')
pyautogui.press('enter')

