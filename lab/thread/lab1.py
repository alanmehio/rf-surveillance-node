# example of extenidn the thread 
from time import sleep
from threading import Thread

# custom thred class
class CustomThread(Thread):

   
    
    # override the run function
    def run(self):
        # block for a moment
        sleep(4)
        # display message
        print('This is  comming from another thread-->' + self.name)
    

# create the thread
thread = CustomThread()
# set the name of the thread
thread.name = 'Alan Mehio'
# start the thread
thread.start()

# wait for the thread to finish 
print("Waiting for the thread to finish")
thread.join()

 