import keyboard

def wPressed():
    
    print("The user presed the 'x' keykey!")

keyboard.add_hotkey('x', wPressed, args=()) # MUST BE DEFINED AFTER THE FUNCTION, wPressed, IS DEFINED

def keyPressed(key=None):
    
    print("The user pressed the", key, "key!")

done = False
def exitLoop():
    
    done = True

keyboard.add_hotkey('w', keyPressed, args=('w'))#keyboard.read_event().name))
keyboard.add_hotkey('a', keyPressed, args=('a'))#keyboard.read_event().name))
keyboard.add_hotkey('s', keyPressed, args=('s'))#keyboard.read_event().name))
keyboard.add_hotkey('d', keyPressed, args=('d'))#keyboard.read_event().name))

keyboard.add_hotkey('c', exitLoop, args=())
while not done:
    pass

print("left the loop")
