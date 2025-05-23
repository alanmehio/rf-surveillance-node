'''
from pymavlink import mavutil

# Create a connection to the MAVLink device
# Replace 'COM3' with your serial port and 57600 with your baud rate
master = mavutil.mavlink_connection('COM3', baud=57600)

# Wait for the heartbeat message to find the system ID
master.wait_heartbeat()

# Create a heartbeat message
heartbeat_msg = master.mav.heartbeat_encode(
    type=mavutil.mavlink.MAV_TYPE_QUADROTOR,
    autopilot=mavutil.mavlink.MAV_AUTOPILOT_ARDUPILOTMEGA,
    base_mode=0,
    custom_mode=0,
    system_status=mavutil.mavlink.MAV_STATE_ACTIVE
)

# Send the heartbeat message
master.mav.send(heartbeat_msg)

print("Heartbeat message sent!")
'''

import time
from pymavlink import mavutil
import pymavlink.dialects.v20.all as dialect
# Import common module for MAVLink 2
from pymavlink.dialects.v20 import common as mavlink2
class Sender():
    def __init__(self, serial_driver_path:str):
        self.serial_driver_path = serial_driver_path

    def send_heartbeat(self):
        master = mavutil.mavlink_connection(self.serial_driver_path)
       # master.wait_heartbeat() # it blocks the send waiting the receiver which is not the case 
        heartbeat_msg = master.mav.heartbeat_encode(
        type=mavutil.mavlink.MAV_TYPE_QUADROTOR,
        autopilot=mavutil.mavlink.MAV_AUTOPILOT_ARDUPILOTMEGA,
        base_mode=0,
        custom_mode=0,
        system_status=mavutil.mavlink.MAV_STATE_ACTIVE)
        
        while True:
            # send the heartbeat message
            print("Trying to send heartbest")
            master.mav.heartbeat_send(mavutil.mavlink.MAV_TYPE_GCS,
                                                mavutil.mavlink.MAV_AUTOPILOT_INVALID, 0, 0, 0)
            print("Heartbest sent")
            print("\n\n")
            time.sleep(1)
    
if(__name__) == '__main__':
    sender = Sender("/dev/ttyUSB0")
    sender.send_heartbeat()

    

