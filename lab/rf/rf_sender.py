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
from pymavlink import mavutil
# Import common module for MAVLink 2
from pymavlink.dialects.v20 import common as mavlink2
class Sender():
    def __init__(self):
        pass

    def send_heartbeat(self):
        master = mavutil.mavlink_connection("/dev/ttyUSB0",baud=57600)
       # master.wait_heartbeat() # it blocks the send waiting the receiver which is not the case 
        heartbeat_msg = master.mav.heartbeat_encode(
        type=mavutil.mavlink.MAV_TYPE_QUADROTOR,
        autopilot=mavutil.mavlink.MAV_AUTOPILOT_ARDUPILOTMEGA,
        base_mode=0,
        custom_mode=0,
        system_status=mavutil.mavlink.MAV_STATE_ACTIVE)
        
        # send the heartbeat message
        master.mav.heartbeat_send(mavutil.mavlink.MAV_TYPE_ONBOARD_CONTROLLER,
                                  mavutil.mavlink.MAV_AUTOPILOT_INVALID,0,0,0)

    def send_text_message(self, device:any):
        # create connection to mavlink device
        print(mavutil.mavlink10())
        #mavutil.set_dialect(pymavlink.dialects.v20.MAVLINK20)
        connection = mavutil.mavlink_connection(device, baud=115200)
        print('Sending text message')
        connection.mav.statustext_send(mavutil.mavlink.MAV_SEVERITY_NOTICE
                                       ,"QGC will readt this".encode())
        connection.close()

    

