with open("settings", "r") as file:
    
    # default speed
    defaultSpeed = file.readline()[-8:].rstrip('\n').split(",")
    defaultSpeed[0] = float(defaultSpeed[0])
    defaultSpeed[1] = float(defaultSpeed[1])
    
    # extra
    defaultExtra = bool(file.readline()[-4:])