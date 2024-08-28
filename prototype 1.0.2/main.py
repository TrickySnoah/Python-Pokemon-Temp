from time import sleep as s
from threading import Thread as t
import dialogue

# output a starting message
print("Starting game.\n")
s(1)

# initialize variables
#stopThread = False # boolean to stop the thread
message = "This is a message" # msg that will be outputted
dialogueType = "character" # the type of message that should be outputted
voiceType = "regular" # the type of speaking from the characters

# the there is a dialogue type is to organize the type of text that will outputted, such as
# character dialogue (regular, shouting, whispering), pokemon atacks, system messages, etc.

# create the thread for the dialogue
threadOne = t(target=dialogue.mainDialogue, args=(message, dialogueType, voiceType))

# start the thread
threadOne.start()