from pynput.keyboard import Key, Listener, KeyCode

import pygame



# the function that will be called by main.py
def titleScreenMain(key):
    
    pygame.init()
    
    quitGame = False
    
    print("entered title screen.")
    while not quitGame:
        
        # check to see whether the user pressed the X to close the window or not
        for event in pygame.event.get():
            if event.type == pygame.QUIT or pygame.key.get_pressed()[pygame.K_ESCAPE]:
                quitGame = True
        
        # check to see if the user chose to quit the game
        if key == Key.esc:
            quitGame = True
            break
        
        # the user will first be presented with the main screen, which will contain
        # three options: Continue, New Save, and Options.
        
        pygame.display.flip()
        clock.tick(FPS)
        
