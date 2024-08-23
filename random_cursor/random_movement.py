import threading
import time
import keyboard
import ctypes
import sys
import random

import win32gui


def loop_moves():
    while True:
        cursor = ctypes.wintypes.POINT()
        ctypes.windll.user32.GetCursorPos(ctypes.byref(cursor))
        x = cursor.x + random.choice([-1, 0, 1])
        y = cursor.y + random.choice([-1, 0, 1])
        ctypes.windll.user32.SetCursorPos(x, y)
        time.sleep(0.2)
        if win32gui.GetCursorInfo()[1] != 65567:
            ctypes.windll.user32.mouse_event(0x0006, ctypes.c_long(x), ctypes.c_long(x), 0, 0)


def main():
    
    if sys.platform == "win32":
        thread = threading.Thread(target=loop_moves)
        thread.daemon = True
        thread.start()

        while True:
            if keyboard.read_key():
                break
    else:
        print('OS not supported.')

if __name__ == '__main__':
    main()