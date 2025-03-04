import queue
import numpy as np
from threading import Thread
import logging

class DataBroker():
    q = queue.Queue()

    def __init__(self):
        self.logger = logging.getLogger("Broker")

    def worker(self):
        while True:
            self.logger.info('inside the worker now ..')
            items = DataBroker.q.get()
            self.logger.info(f'Working items type {type(items)}')
            self.logger.info(f' The type of the element is {type(items[0])}')
        
            # check for the element type 
            if isinstance(items[0],np.complex128):
                self.logger.info(f'Got the samples of size {len(items)}')
            elif isinstance(items[0], np.float64):
                self.logger.info(f' Got the frequencies array of size {len(items)}')

    def start(self):
        # Turn on the worker thread
        Thread(target=self.worker, daemon=True).start()