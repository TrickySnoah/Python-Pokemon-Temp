from threading import Thread
from time import sleep as s

# create the sub class
class Dialogue(Thread):
    
    # initialization
    def __init__(self, event, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.event = event
        self.threadOneRunning = False
        
    def run(self) -> None: # Thread.start() starts this?
        for i in range(50):
            print(i)
        
        self.event.set()
        
    
    
