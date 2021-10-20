import time
import math
import pyautogui as auto

r = 300
time.sleep(4)
t = 0

while r > 40:
    while t < 2 * math.pi:
        x = r * math.cos(t)
        y = r * math.sin(t)
        auto.click(x + 500, y + 600)
        t = t + 0.1
    t = 0
    r = r - 10
