from threading import Thread
from time import sleep as s

# create the sub class
class Dialogue(Thread):
    
    # initialization
    def __init__(self, event, message, dialogueType, voiceType, *args, **kwargs):
        super().__init__(*args, **kwargs) # what arguments should this be taking?
        self.event = event
        self.message = message
        self.dialogueType = dialogueType
        self.voiceType = voiceType
        #self.threadOneRunning = False # is this needed?
    
    def __systemDialogue(self):
        pass
    
    def __characterDialogue(self):
        # split the words in the message
        words = self.message.split()
        
        # loop for every word in the words list
        for word in words:
            
            # loop for every letter in each word
            for letter in word:
                
                # print the letter and wait a little
                print(letter, end="")
                s(.03)
                    
            # at the end of each word, add a space
            print(" ", end="")
            
        # output a newline
        print()
    
    def run(self) -> None: # Thread.start() starts this
        
        # check to see which function is needed
        if self.dialogueType == "system":
            self.__systemDialogue()
        
        elif self.dialogueType == "character":
            self.__characterDialogue()
        
        #self.event.set() # what does this do?
        
        #print("Thread ending.") # this tells the user that the thread is dead