
'''
$ export PYTHONPATH=/home/alan/workspace-python/RTL-SDR/rf-surveillance/src
$ pwd 
 /home/alan/workspace-python/RTL-SDR/rf-surveillance/src
$ python rfcentral
$ python rfnode
$ python rfsink 
'''
from rf_receiver.css.receiver import Receiver

def main()-> None:
    receiver = Receiver('COM4')
    receiver.start()
   

# this is important so that it does not run from pytest 
if __name__ == "__main__": 
    main()

