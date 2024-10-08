from threading import Thread
from time import sleep as s
import pygame

from settings import *

# initialize pygame
pygame.init()

# constant variables

# create the sub class
class InGameMenu(Thread):
    
    # initialization
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs) # what arguments should this be taking?
        self.temp = 5
        
        self.quit = False
        
        self.__selection = 1
        # the list will look like this:
        # [ Pokemon , Pokedex,		[ 1 , 2,
        #   Bag , Success,			  3 , 4,
        #   Save , Options ]		  5 , 6 ]
  
    def run(self) -> None: # Thread.start() starts this
        # this is going to be the main thread
        
        while not self.quit:
            
            # check to see if the user presses W, A, S, or D, and change the value of __selection accordingly
            if pygame.key.get_pressed()[pygame.K_w]:
                print("w")
                
                while pygame.key.get_pressed()[pygame.K_w]: pass
                
            elif pygame.key.get_pressed()[pygame.K_a]:
                print("a")
                
                while pygame.key.get_pressed()[pygame.K_a]: pass
                
            elif pygame.key.get_pressed()[pygame.K_s]:
                print("s")
                
                while pygame.key.get_pressed()[pygame.K_s]: pass
                
            elif pygame.key.get_pressed()[pygame.K_d]:
                print("d")
                
                while pygame.key.get_pressed()[pygame.K_d]: pass