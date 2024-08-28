from time import sleep as s

def functionThree(stopThread):
    
    while not stopThread():
        print("Hello ")
        s(1)
        
def functionFour(message, stopThread):
    
    while not stopThread():
        print(message)
        s(1)