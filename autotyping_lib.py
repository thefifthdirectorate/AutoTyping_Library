from pynput.keyboard import Key, Controller
import time

keyboard = Controller()

def Enter(): # Presses Enter
    keyboard.press(Key.enter)
    keyboard.release(Key.enter)

def SetDelay(Delay): # Sets delay for each message 
    time.sleep(Delay)

def GetHotkey(HotKey, Do): # Sets your Hotkey for each message
    with keyboard.pressed(HotKey):
        Do

def SendMessage(string, string1, string2, string3, string4, string5, string6): # Sends messages, you can add more parameters if needed
    keyboard.type(string)
    Enter()
    keyboard.type(string1)
    Enter()
    keyboard.type(string2)
    Enter()
    keyboard.type(string3)
    Enter()
    keyboard.type(string4)
    Enter()
    keyboard.type(string5)
    Enter()
    keyboard.type(string6)
    Enter()
