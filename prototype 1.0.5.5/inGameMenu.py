from threading import Thread
import pygame

from settings import *

# constant variables

# create the sub class
class InGameMenu(Thread):
    
    # initialization
    def __init__(self, message, speed=defaultSpeed, character=None, *args, **kwargs):
        super().__init__(*args, **kwargs) # what arguments should this be taking?
        self.temp = 5
        
        self.quit = False
        
        self.__temp = 5
  
    def run(self) -> None: # Thread.start() starts this
        
        pass