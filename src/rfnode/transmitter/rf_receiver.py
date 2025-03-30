from pymavlink import mavutil
# Import common module for MAVLink 2
from pymavlink.dialects.v20 import common as mavlink2
import time

class Receiver():

    def __init__(self):
        pass

    def receive_heartbeat(self):
        # Connect to the MAVLink device
         connection = mavutil.mavlink_connection("/dev/ttyUSB1", baud=57600)
         connection.wait_heartbeat()
         print("Heartbeat recieved from system(system %u component %u) %(connection.target_system, connection.target_component)")
         while True:
             # Receive a message 
             message = connection.recv_match(blocking=True)
             if message is not None:
                 print(message)

    def receive_text_message(self,device:any):
        # connection to the MAVLINK device
        print(mavutil.mavlink10())
        connection = mavutil.mavlink_connection(device,baud=115200)

        while False:
            # Receive a message 
            print('Trying to receive a message')
            message = connection.recv_match(blocking=False)
            if message is None:
                pass

            if message is not None:
                print(f'message recieved {type(message)}')
                break
            
            # Don't abuse the CPU by running the loop maximum speed
            time.sleep(0.001)

        print('Received message ...')
                 

''' 
# Wait for a heartbeat from the device
connection.wait_heartbeat()
print("Heartbeat received from system (system %u component %u)" % (connection.target_system, connection.target_component))


while True:
    # Receive a message
    message = connection.recv_match(blocking=True)
    if message is not None:
        print(message)
'''
