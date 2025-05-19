import queue
import time
import numpy as np
from threading import Thread
import logging
from datetime import datetime
import json
from common.util import NumpyComplexEncoder
from model.rf_model import HighPowerSample, HighPowerFrequency
from device_manager import DeviceManager
from rf_sender.css.sender import Sender

class DataBroker():
    q = queue.Queue()

    def __init__(self,hold:float=0.2):
        self.logger = logging.getLogger("Broker")
        self.hold= hold

    def set_rf_sender(self,sender:Sender)->None:
        self.sender = sender

    def worker(self):
        while True:
            self.logger.info('inside the worker now ..')
            obj = DataBroker.q.get() # blocks until an element found in queue
        
            # check for the element type 
            if isinstance(obj,HighPowerSample):

                #obj_str = obj.to_json(NumpyComplexEncoder) Alan in V2
                payload:str = str(round(obj.get_frequency(),2)) + "|" + str(round(obj.get_power(),2))
                self.sender.send(payload)
                time.sleep(self.hold) # 200 ms is 0.2 
                #self.logger.info(f'Got the HighPowerSample {obj_str}')
            elif isinstance(obj,HighPowerFrequency):
                obj_str = obj.to_json()
                self.logger.info(f' Got the HighPowerFrequency  {obj_str}')

    def start(self):
        # Turn on the worker thread
        Thread(target=self.worker, daemon=True).start()



        

        