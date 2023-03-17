
import pyautogui
import time
print(pyautogui.size())
pyautogui.moveTo(100, 100, duration = 5)
pyautogui.click(100,100)
time.sleep(3)


pyautogui.dragRel(0, 100, duration = 1)
pyautogui.typewrite("hello Geeks !")


