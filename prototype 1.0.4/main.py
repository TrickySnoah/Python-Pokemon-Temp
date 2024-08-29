from time import sleep as s
from threading import Thread as t

import pygame
import pyautogui
import os
import dialogue

# set the window to a certain spot on the screen
x_specspot = 0 #Variable used for a specific spot
y_specspot = 30 #Varialbe used for a specific spot

os.environ['SDL_VIDEO_WINDOW_POS'] = '%d,%d' % (x_specspot,y_specspot) #Used so that environment variables can be set in python

# get the resolution of the user's screen
resolution = pyautogui.size()
reso_width = resolution[0]; reso_height = resolution[1]

# set up pygame
pygame.init()
screen = pygame.display.set_mode((reso_width,reso_height))
clock = pygame.time.Clock()
FPS = 120
quitGame = False

# set up keyboard action boolean variables
spacePressed = False

# initialize the boolean variables for the threads
threadOneRunning = False

while not quitGame:
    
    # check to see whether the user pressed the X to close the window or not
    for event in pygame.event.get():
        if event.type == pygame.QUIT or pygame.key.get_pressed()[pygame.K_ESCAPE]:
            quitGame = True
    
    # initialize variables. Where these variables are initialized will be somewhere else later on. They
    # are only here for now.
    message = "This is a message" # msg that will be outputted
    dialogueType = "character" # the type of message that should be outputted
    voiceType = "regular" # the type of speaking from the characters

    # the there is a dialogue type is to organize the type of text that will outputted, such as
    # character dialogue (regular, shouting, whispering), pokemon atacks, system messages, etc.

    # initialize the threads
    threadOne = t(target=dialogue.mainDialogue, args=(lambda : threadOneRunning, message, dialogueType, voiceType,))
    
    # start the thread if the user presses the spacebar
    if pygame.key.get_pressed()[pygame.K_SPACE]:
        if not spacePressed and not threadOneRunning:
            threadOneRunning = True
            threadOne.start()
            threadOneRunning = threadOne.join()
        spacePressed = True
    else:
        spacePressed = False
    print(f"running: {threadOneRunning} pressed: {spacePressed}")
    # update the screen and clock
    pygame.display.flip()
    clock.tick(FPS)
    
pygame.quit()