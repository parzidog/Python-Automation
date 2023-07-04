import pyautogui as pag
import pyperclip as clip
import time as t

position = pag.position()
press = pag.press

press("down")
press(3 * "enter")

pag.write("Python is good!\n")

pag.hotkey("command", "a")

# Store clipboard text

text = clip.paste()
