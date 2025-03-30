from pymavlink import mavutil
import time
import os 
from rf_sender import Sender
from rf_receiver import Receiver


def main()->None:
    sender = Sender()
    sender.send_text_message("/dev/ttyUSB0")
    receiver = Receiver()
    receiver.receive_text_message("/dev/ttyUSB1")

if __name__ == '__main__':
     main()