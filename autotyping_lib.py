from pynput.keyboard import Key, Controller
import time
import random
import subprocess
import pygetwindow

keyboard = Controller()

class Globals:
    ProcessName = ""
    WindowTitle = ""

class Process:
    @staticmethod
    def IsValidWindow():
        win = pygetwindow.getActiveWindow()
        return win.title == Globals.WindowTitle
    
    @staticmethod
    def IsValidProcess(): # checks if process exists in taskmanager
        try:
            process_list = subprocess.Popen(['tasklist'], stdout=subprocess.PIPE, text=True)
            for process in process_list.stdout:
                if Globals.ProcessName in process:
                    return True
            return False 
        except Exception as e:
            print(f"Error checking processes: {e}")
            return False

class Functions:
    @staticmethod
    def Delay(Delta):
        time.sleep(Delta)

    @staticmethod
    def SplitMessage(Words):
        return [char for char in Words]
    
    @staticmethod
    def SendMessage(Message):
        keyboard.type(Message)
        keyboard.press(Key.enter)
        keyboard.release(Key.enter)
        Functions.Delay(random.uniform(0.08, 0.1))

    @staticmethod
    def SendRandomMessage(Message): 
        Functions.SendMessage(random.choice(Message))

    @staticmethod
    def SendMessageWithinRange(Lowest, Highest, Message):
        for _ in range(random.randint(Lowest, Highest)): 
            Functions.SendMessage(Message)

    @staticmethod
    def SendRandomMessageWithinRange(Lowest, Highest, Message):
        for _ in range(random.randint(Lowest, Highest)):
            Functions.SendRandomMessage(Message)
