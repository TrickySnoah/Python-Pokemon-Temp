from time import sleep as s

def systemDialogue(message):
    pass

def characterDialogue(message, voiceType):
    
    # split the words in the message
    words = message.split()
    
    # loop for every word in the words list
    for word in words:
        
        # loop for every letter in each word
        for letter in word:
            
            # print the letter and wait a little
            print(letter, end="")
            s(.03)
                
        # at the end of each word, add a space
        print(" ", end="")
        
    # return a boolean value to stop the thread
    return True
    
def mainDialogue(message, dialogueType, voiceType=None):
    
    print("Starting Thread One\n")
    s(.1)
    
    stopThread = False
    
    while not stopThread:
        
        if dialogueType == "system":
            systemDialgoue(message)
            
        elif dialogueType == "character":
            stopThread = characterDialogue(message, voiceType)
            