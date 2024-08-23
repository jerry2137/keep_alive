import threading
import time
import keyboard
import ctypes
import sys
import json


def move(mouse_events):
    last_time = None
    for event in mouse_events:
        if last_time is not None:
            time.sleep(abs(event[2] - last_time))
        last_time = event[2]
        ctypes.windll.user32.SetCursorPos(int(event[0]), int(event[1]))

def loop_moves():
    with open('movement.json', 'r') as file:
        mouse_events = json.load(file)
    while True:
        move(mouse_events)
        mouse_events.reverse()


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