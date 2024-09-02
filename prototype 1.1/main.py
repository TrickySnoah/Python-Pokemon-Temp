from threading import Thread, Event

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

# initialize the boolean variables for the threads
dialogueThreadRunning = False
 
while not quitGame:
    
    # check to see whether the user pressed the X to close the window or not
    for event in pygame.event.get():
        if event.type == pygame.QUIT or pygame.key.get_pressed()[pygame.K_ESCAPE]:
            quitGame = True
    
    # initialize variables. Where these variables are initialized will be somewhere else later on. They
    # are only here for now.
    message = "In this world, there are plenty of things that can affect the way we live, including our diet, attitude, and actions.&We are also affected by ... a lot of uncontrollable things ... but, there will always be ways to change our outcomes." # msg that will be outputted
    character = "Noah" # this is the name of the character that is speaking

    # the there is a dialogue type is to organize the type of text that will outputted, such as
    # character dialogue (regular, shouting, whispering), pokemon atacks, system messages, etc.

    # update the boolean variables for the threads
    try: dialogueThreadRunning = dialogueThread.is_alive()
    except: pass

    # initialize the thread IF it's not running
    if not dialogueThreadRunning:
        event = Event()
        dialogueThread = dialogue.Dialogue(event, message, character=character)

    # start the thread if the user presses the spacebar
    if pygame.key.get_pressed()[pygame.K_SPACE]:
        if not dialogueThreadRunning: # make sure to not execute multiple times if the thread is running already
            dialogueThread.start()

    # update the screen and clock
    pygame.display.flip()
    clock.tick(FPS)


# kill the threads if necessary
if dialogueThreadRunning: dialogueThread.event.set() # sets the event boolean variable to True

# end pygame
pygame.quit()