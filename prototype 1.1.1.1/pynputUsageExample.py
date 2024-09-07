from pynput.keyboard import Key, Listener, KeyCode
from threading import Thread

import pygame
import pyautogui
import os

# use a global variable
at = "main"

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






# function for managing keyboard actions
def keyboard(key):
    global at
    
    # MAIN
    if at == "main":
        
        if key == KeyCode.from_char("e"):
            # start thread one
            print("entering thread one.")
            at = "threadOne"
            threadOneThread = Thread(target=threadOne)
            threadOneThread.start()
            
        elif key == Key.esc:
            print("ending main.")
            return False
        
    elif at == "threadOne":
        
        if key == KeyCode.from_char("e"):
            # start thread two
            print("entering thread two.")
            at = "threadTwo"
            threadTwoThread = Thread(target=threadTwo)
            threadTwoThread.start()
            
        elif key == Key.backspace:
            # go back to the main thread
            print("returning to main.")
            at = "main"
            
    elif at == "threadTwo":
        
        if key == KeyCode.from_char("e"):
            # can't go further
            print("can't go further.")
            
        elif key == Key.backspace:
            # go back to the main thread
            print("returning to thread one.")
            at = "threadOne"
            threadOneThread = Thread(target=threadOne)
            threadOneThread.start()
            




# thread functions
def threadOne():
    global at
    
    while True:
        
        if (at == "main") or (at == "threadTwo"): break
        
    print("threadOne ended.")
    
def threadTwo():
    global at
    
    while True:
        
        if at == "threadOne": break
        
    print("threadTwo ended.")
    
    
    
    
    

# create the keyboard listener and start it
listener = Listener(on_press=keyboard)
listener.start()

print("starting the main loop.")
while not quitGame:
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT or not listener.is_alive():
            quitGame = True
    
    # update the screen and clock
    pygame.display.flip()
    clock.tick(FPS)
    
print("program ended.")
pygame.quit()