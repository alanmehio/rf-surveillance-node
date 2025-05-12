
'''
$ export PYTHONPATH=/home/alan/workspace-python/RTL-SDR/rf-surveillance/src
$ pwd 
 /home/alan/workspace-python/RTL-SDR/rf-surveillance/src
$ python rfcentral
$ python rfnode
$ python rfsink 
'''
from rfcentral.rf_receiver import Receiver

def main()-> None:
    receiver = Receiver()
    receiver.start()
   

# this is important so that it does not run from pytest 
if __name__ == "__main__": 
    main()

