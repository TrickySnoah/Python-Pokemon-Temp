import threading
from time import sleep as s

class Main:
    
    def __init__(self):
        pass
    
    def startThread(self, subClass, function):
        return subClass.startThread(self, function)

class Dialogue(Main):
    
    def __init__(self):
        heldTextLines = [] # this sets a list of text lines. This holds strings
    
    def startThread(self, function):
        # this will start a thread for any of the functions below
        if function == "EF1":
            threading.Thread(target=Dialogue.EF1, args=()).start()
            
        elif function == "EF2":
            threading.Thread(target=Dialogue.EF2, args=()).start()
        
    
    def EF1():
        # example function 1
        while True:
            print("a")
            s(1)
            print("b")
            s(1)
            print("c")
            s(1)
        
    def EF2():
        # example function 2
        while True:
            print("1")
            s(1)
            print("2")
            s(1)
            print("3")
            s(1)
        
