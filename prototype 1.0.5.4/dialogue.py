from threading import Thread
from time import sleep as s
import pygame

from settings import *

# constant variables
LETTER_OUTPUT_LIMIT = 40
MAX_LINE_OUTPUT = 2

# create the sub class
class Dialogue(Thread):
    
    # initialization
    def __init__(self, event, message, speed=defaultSpeed, character=None, *args, **kwargs):
        super().__init__(*args, **kwargs) # what arguments should this be taking?
        self.event = event
        self.message = message
        self.speed = speed # speed is a list, containing .03 and .07 by default. The .7 is the speed for ellipses. This will be detected later on.
        self.character = character
        
        self.__letterCount = 0
        self.__lineCount = 0
        self.__nameOutputted = False
        self.__messages = None
    
    def __textSpeedUp(self):
        
        # check for the spacebar being pressed
        if pygame.key.get_pressed()[pygame.K_SPACE]:
            # change the speed of the text
            self.speed = [.01,.01]
            
        else:
            # change back to the default speed
            self.speed = defaultSpeed
            
    def __nameOutput(self):
        for letter in self.character:
                    
            # check for termination
            if self.event.is_set(): break
            
            # check for speed up
            self.__textSpeedUp()
            
            # print the letter, wait a little, and increase the letter count
            print(letter, end="")
            s(self.speed[0])
            self.__letterCount += 1
        
        # output a colon and a space after the name
        print(":", end="")
        s(self.speed[0])
        print(" ", end="")
        s(self.speed[0])
        self.__letterCount += 2
        
        # change the name output boolean to true
        self.__nameOutputted = True
    
    def __textOutput(self):
        
        # split the words in the message
        words = self.message.split()
        
        # loop for every word in the words list
        for word in words:
            
            # check to see if the current letter count plus the length of the next word is greater than the limit
            if LETTER_OUTPUT_LIMIT < (self.__letterCount + len(word)):
                print()
                self.__letterCount = 0
                self.__lineCount += 1
               
            # check to see if two lines have been outputted already. If so, wait for the user to press spacebar again
            if self.__lineCount == MAX_LINE_OUTPUT:
                
                # ensure that the spacebar isn't being held
                while pygame.key.get_pressed()[pygame.K_SPACE]:
                    
                    # check for termination
                    if self.event.is_set(): break
                    
                # wait for the next spacebar press
                while True:
                    
                    # check for termination
                    if self.event.is_set(): break
                    
                    if pygame.key.get_pressed()[pygame.K_SPACE]:
                        self.__lineCount = 1
                        break
            
            # check to see if there's a name. If so, then output the name
            if (self.character != None) and (not self.__nameOutputted):
                self.__nameOutput()
                    
            # loop for every letter in each word
            for letter in word:
                
                # check for termination
                if self.event.is_set(): break
                
                # check for speed up
                self.__textSpeedUp()
                
                # print the letter, wait a little, and increase the letter count. Wait longer if ellipses are detected
                print(letter, end="")
                if word == "...": s(self.speed[1])
                else: s(self.speed[0])
                self.__letterCount += 1
            
            # check for termination
            if self.event.is_set(): break
            
            # at the end of each word, add a space and increase the letter count
            print(" ", end="")
            self.__letterCount += 1
            
        # output a newline
        print()
        
    def run(self) -> None: # Thread.start() starts this
        
        print("-") # this is just here to organize the output visually
        
        # check to see if there is an '&' in the message. If so, there are going to be breaks in the output
        if "&" in self.message:
            self.__messages = self.message.split("&")
            
            for message in self.__messages:
                self.message = message
                self.__textOutput()
                
                # check for termination
                if self.event.is_set(): break
                
                # if the user is holding down on the spacebar, wait for them to release it before going on
                while pygame.key.get_pressed()[pygame.K_SPACE]:
                    # check for termination
                    if self.event.is_set(): break
                    
                while True:
                    # check for termination
                    if self.event.is_set(): break
                    
                    if pygame.key.get_pressed()[pygame.K_SPACE]:
                        break
                    
                # reset the letter count and line count
                self.__letterCount = 0
                self.__lineCount = 0
                
                print() # this is just here to organize the output visually
        
        else:
            # output the text
            self.__textOutput()
