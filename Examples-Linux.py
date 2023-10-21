import keyboard
import os
import time
def task(): os.popen('su -c xfce4-taskmanager name') #Open task #put the name of the acc into where name is.

def mic(): os.popen('amixer -c1 set Capture toggle') 

			#we have to use scan codes for all the f14 to f24 because the module does not support it 184 = f14
			#Also don't use f13 because thats the mute button.
keyboard.add_hotkey((184), task) #f14
keyboard.add_hotkey((185), mic) #f15
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