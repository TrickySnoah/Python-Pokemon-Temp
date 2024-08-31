from threading import Thread
from time import sleep as s
import pygame

# constant variables
LETTER_OUTPUT_LIMIT = 40
MAX_LINE_OUTPUT = 2

# create the sub class
class Dialogue(Thread):
    
    # initialization
    def __init__(self, event, message, speed=[.03,.3], character=None, *args, **kwargs):
        super().__init__(*args, **kwargs) # what arguments should this be taking?
        self.event = event
        self.message = message
        self.speed = speed # speed is a list, containing .3 and .7. The .7 is the speed for ellipses. This will be detected later on.
        self.character = character
        
        self.__letterCount = 0
        self.__lineOutput = 0
    
    def __textOutput(self):
        # split the words in the message
        words = self.message.split()
        print("-") # this is just here to organize the output visually
        
        # loop for every word in the words list
        for word in words:
            
            # check to see if the current letter count plus the length of the next word is greater than the limit
            if LETTER_OUTPUT_LIMIT < (self.__letterCount + len(word)):
                print()
                self.__letterCount = 0
                self.__lineOutput += 1
                
            # check to see if two lines have been outputted already. If so, wait for the user to press spacebar again
            if self.__lineOutput == MAX_LINE_OUTPUT:
                while True:
                    
                    # check for termination
                    if self.event.is_set(): break
                    
                    if pygame.key.get_pressed()[pygame.K_SPACE]:
                        self.__lineOutput = 1
                        break
            
            # loop for every letter in each word
            for letter in word:
                
                # check for termination
                if self.event.is_set(): break
                
                # print the letter, wait a little, and increase the letter count
                print(letter, end="")
                s(self.speed[0])
                self.__letterCount += 1
            
            # check for termination
            if self.event.is_set(): break
            
            # at the end of each word, add a space and increase the letter count
            print(" ", end="")
            self.__letterCount += 1
            
        # output a newline
        print()
        
    def run(self) -> None: # Thread.start() starts this
        
        # output the text
        self.__textOutput()

