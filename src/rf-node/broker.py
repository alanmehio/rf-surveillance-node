import queue
import numpy as np
from threading import Thread

class DataBroker():
    q = queue.Queue()

    def __init__(self):
        pass

    def worker(self):
        while True:
            print('inside the worker now ..')
            item = DataBroker.q.get()
            print(f'Working on {type(item)}')
            print(f' The type of the element is {type(item[0])}')
        
            # check for the element type 
            if isinstance(item[0],np.complex128):
                print(f'Got the samples of size {len(item)}')
            elif isinstance(item[0], np.float64):
                print(f' Got the frequencies array of size {len(item)}')

    def start(self):
        # Turn on the worker thread
        Thread(target=self.worker, daemon=True).start()