from threading import Thread, Event
import otherFileThreadingTest as file

event = Event()

dialogue = file.Dialogue(event)

dialogue.start()

for i in range(200):
    print(dialogue.is_alive())
    
print("Starting dialogue again")
dialogue = file.Dialogue(event)
dialogue.start()