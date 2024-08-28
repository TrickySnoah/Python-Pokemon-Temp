import threading
from time import sleep as s

from classes import Main as m
from classes import Dialogue as d
        
#threadOne = threading.Thread(target=d.EF1, args=())
#threadTwo = threading.Thread(target=d.EF2, args=())

#threadOne.start()
#s(.1)
#threadTwo.start()

main = m()
main.startThread(d, "EF1")
s(.5)
main.startThread(d, "EF2")