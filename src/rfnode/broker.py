import queue
import numpy as np
from threading import Thread
import logging
from datetime import datetime
import json
from common.util import NumpyComplexEncoder
from model.rf_model import HighPowerSample, HighPowerFrequency
from device_manager import DeviceManager
from transmitter.fragments.rf.sender import Sender

class DataBroker():
    q = queue.Queue()

    def __init__(self):
        self.logger = logging.getLogger("Broker")
        #FIXME Alan just persist to database now 

    def worker(self):
        while True:
            self.logger.info('inside the worker now ..')
            obj = DataBroker.q.get() # blocks until an element found in queue
            #self.logger.info(f'Working items type {type(obj)}')
        
            # check for the element type 
            if isinstance(obj,HighPowerSample):
                obj_str = obj.to_json(NumpyComplexEncoder)
                self.logger.info(f'Got the HighPowerSample {obj_str}')
            elif isinstance(obj,HighPowerFrequency):
                obj_str = obj.to_json()
                self.logger.info(f' Got the HighPowerFrequency  {obj_str}')

    def start(self):
        # Turn on the worker thread
        Thread(target=self.worker, daemon=True).start()



        

        