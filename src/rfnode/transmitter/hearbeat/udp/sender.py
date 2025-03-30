import time
from pymavlink import mavutil
from pymavlink.dialects.v10.ardupilotmega import MAVLINK_MSG_ID_UNKNOWN

class Sender():
    def __init__(self):
        pass

    def send_heartbeat(self):
        master = mavutil.mavlink_connection('udpout:0.0.0.0:14550')
        while True:
            # send the heartbeat message
            print("Trying to send heartbest")
            master.mav.heartbeat_send(mavutil.mavlink.MAV_TYPE_GCS,
                                                mavutil.mavlink.MAVLINK_MSG_ID_UNKNOWN, 0, 0, 0)
            print("Heartbest sent")
            print("\n\n")
            time.sleep(1)
    
if(__name__) == '__main__':
    sender = Sender()
    sender.send_heartbeat()

    

