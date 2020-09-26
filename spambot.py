import pyautogui, time

time.sleep(3)
f = open("spam", 'r')
for word in f:
    pyautogui.typewrite(word)
    pyautogui.press("enter")
