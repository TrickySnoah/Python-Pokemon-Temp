from threading import Thread, Event
import otherFileThreadingTest as file

event = Event()

dialogue = file.Dialogue(event)

dialogue.start()