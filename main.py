from threading import Thread as t
from time import sleep as s
import threadingTest as otherFile

stopThread = False

def functionOne(stopThread):
    
    while not stopThread():
        print("Preparing ")
        s(1)
        
def functionTwo(stopThread):
    
    while not stopThread():
        print("message.\n")
        s(1)

t1 = t(target=functionOne, args=(lambda : stopThread, ))
t2 = t(target=functionTwo, args=(lambda : stopThread, ))

t3 = t(target=otherFile.functionThree, args=(lambda : stopThread, ))
t4 = t(target=otherFile.functionFour, args=("world.\n", lambda : stopThread))

t1.start()
s(.1)
t2.start()
s(.3)

t3.start()
s(.1)
t4.start()
s(.3)

count = 0
while True:
    print("=== Interuption ===\n")
    s(1)
    
    count += 1
    
    if count == 5: break
    
stopThread = True

t1.join()
t2.join()
t3.join()
t4.join()