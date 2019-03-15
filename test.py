import pyautogui
import time

# import win32api

# pyautogui.click(100, 100)

# pyautogui.moveRel(0, 10)  # move mouse 10 pixels down
# pyautogui.dragTo(100, 150)
# pyautogui.dragRel(0, 10)  # drag mouse 10 pixels down
x = 200
y = 200
i = 200

from ctypes import Structure, windll, c_uint, sizeof, byref


class LASTINPUTINFO(Structure):
    _fields_ = [
        ('cbSize', c_uint),
        ('dwTime', c_uint),
    ]


def get_idle_duration():
    lastInputInfo = LASTINPUTINFO()
    lastInputInfo.cbSize = sizeof(lastInputInfo)
    windll.user32.GetLastInputInfo(byref(lastInputInfo))
    millis = windll.kernel32.GetTickCount() - lastInputInfo.dwTime
    return millis / 1000.0


temp = 0

while i < 1000:
    if get_idle_duration() > 1:
        print(i)
        pyautogui.moveTo(i + 1, i)
        pyautogui.moveTo(i, i)
        # time.sleep(0.001)
        # i += 10
