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
        
    def __pokemonList(self): # the name of this may change later on
        print("pL")
        pass
    
    def __pokedex(self): # the name of this may change later on
        print("pd")
        pass
    
    def __bag(self):
        print("b")
        pass
    
    def __success(self):
        print("su")
        pass
    
    def __save(self):
        print("sa")
        pass
    
    def __options(self):
        print("o")
        pass
    
    def run(self) -> None: # Thread.start() starts this
        # this is going to be the main thread
        
        while not self.quit:
            
            # check to see if the user presses W, A, S, or D, and change the value of __selection accordingly
            if pygame.key.get_pressed()[pygame.K_w]:
                # decrease the value of __selection by 2, 1, or 0
                if (self.__selection - 2) >= 1: self.__selection -= 2
                elif (self.__selection - 1) >= 1: self.__selection -= 1
                
                while pygame.key.get_pressed()[pygame.K_w]: pass
                
            elif pygame.key.get_pressed()[pygame.K_a]:
                # decrease the value of __selection by 1 or 0
                if (self.__selection - 1) >= 1: self.__selection -= 1
                
                while pygame.key.get_pressed()[pygame.K_a]: pass
                
            elif pygame.key.get_pressed()[pygame.K_s]:
                # increase the value of __selection by 2, 1, or 0
                if (self.__selection + 2) <= 6: self.__selection += 2
                elif (self.__selection + 1) <= 6: self.__selection += 1
                
                while pygame.key.get_pressed()[pygame.K_s]: pass
                
            elif pygame.key.get_pressed()[pygame.K_d]:
                # increase the value of __selection by 1 or 0
                if (self.__selection + 1) <= 6: self.__selection += 1
                
                while pygame.key.get_pressed()[pygame.K_d]: pass
            
            # check for when the user presses 'e'
            if pygame.key.get_pressed()[pygame.K_e]:
                # call a function based on the selection
                if self.__selection == 1:
                    self.__pokemonList()
                    
                elif self.__selection == 2:
                    self.__pokedex()
                    
                elif self.__selection == 3:
                    self.__bag()
                    
                elif self.__selection == 4:
                    self.__success()
                    
                elif self.__selection == 5:
                    self.__save()
                    
                elif self.__selection == 6:
                    self.__options()
            
            print(self.__selection)
            s(.085)