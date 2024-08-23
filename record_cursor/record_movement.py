import mouse
import time
import json

mouse_events = []

mouse.hook(mouse_events.append)
time.sleep(10)
mouse.unhook(mouse_events.append)

with open('movement.json', 'w') as file:
    json.dump(mouse_events, file)