import keyboard
import time
			#we have to use scan codes for all the f13 to f24 because the module does not support it eg: 183 = f13
keyboard.add_hotkey((183), print, args=('triggered', 'hotkey')) #f13
keyboard.add_hotkey((184), print, args=('triggered', 'hotkey')) #f14
keyboard.add_hotkey((185), print, args=('triggered', 'hotkey')) #f15
keyboard.add_hotkey((186), print, args=('triggered', 'hotkey')) #f16
keyboard.add_hotkey((187), print, args=('triggered', 'hotkey')) #f17
keyboard.add_hotkey((188), print, args=('triggered', 'hotkey')) #f18
keyboard.add_hotkey((189), print, args=('triggered', 'hotkey')) #f19
keyboard.add_hotkey((190), print, args=('triggered', 'hotkey')) #f20
keyboard.add_hotkey((191), print, args=('triggered', 'hotkey')) #f21
keyboard.add_hotkey((192), print, args=('triggered', 'hotkey')) #f22
keyboard.add_hotkey((193), print, args=('triggered', 'hotkey')) #f23
keyboard.add_hotkey((194), print, args=('triggered', 'hotkey')) #f24
while True:
    time.sleep(1)
