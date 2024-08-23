import time
import ctypes
while True: 
    time.sleep(5)
    ctypes.windll.user32.keybd_event(0x07, 0, 2, 0)