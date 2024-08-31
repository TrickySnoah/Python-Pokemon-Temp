from threading import Thread
from time import sleep as s

# create the sub class
class Dialogue(Thread):
    
    # initialization
    def __init__(self, event, message, speed=[.03,.3], character=None, *args, **kwargs):
        super().__init__(*args, **kwargs) # what arguments should this be taking?
        self.event = event
        self.message = message
        self.speed = speed # speed is a list, containing .3 and .7. The .7 is the speed for ellipses. This will be detected later on.
        self.character = character
        #self.threadOneRunning = False # is this needed?
    
    def __textOutput(self):
        # split the words in the message
        words = self.message.split()
        
        # loop for every word in the words list
        for word in words:
            
            # loop for every letter in each word
            for letter in word:
                
                # print the letter and wait a little
                print(letter, end="")
                s(self.speed[0])
                    
            # at the end of each word, add a space
            print(" ", end="")
            
        # output a newline
        print()
    
    def run(self) -> None: # Thread.start() starts this
        
        # output the text
        self.__textOutput()
        
        #print("Thread ending.") # this tells the user that the thread is dead