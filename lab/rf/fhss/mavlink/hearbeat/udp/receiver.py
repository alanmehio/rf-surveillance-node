from pymavlink import mavutil
import time

class Receiver():

    def __init__(self):
        pass

    def receive_heartbeat(self):
     
      # Create the connection
        master = mavutil.mavlink_connection('udpin:0.0.0.0:14550')

        while True:
            msg = master.recv_match()
            if not msg:
                continue
            if msg.get_type() == 'HEARTBEAT':
                print("\n\n*****Got message: %s*****" % msg.get_type())
                print("Message: %s" % msg)
                print("\nAs dictionary: %s" % msg.to_dict())
                # Armed = MAV_STATE_STANDBY (4), Disarmed = MAV_STATE_ACTIVE (3)
                print("\nSystem status: %s" % msg.system_status)

            time.sleep(0.2)
         

if __name__ == '__main__':
    receiver = Receiver()
    receiver.receive_heartbeat()

    
