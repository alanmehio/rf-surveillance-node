from pymavlink import mavutil
# Import common module for MAVLink 2
from pymavlink.dialects.v20 import common as mavlink2
import time

class Receiver():

    def __init__(self):
        pass

    def receive_heartbeat(self):
        # Connect to the MAVLink device
         connection = mavutil.mavlink_connection("/dev/ttyUSB1")
         print("Heartbeat recieved from system(system %u component %u) %(connection.target_system, connection.target_component)")
         while True:
            # Receive a message 
            print("Trying to receive hearbeat...")
            message = connection.recv_match(blocking=True)
            if message is not None:
                print("Received not None message")
                print(message.to_dict())
                if message.get_type() == 'HEARTBEAT':
                    print("Heartbeat received from system %u component %u" % (message.system_id, message.component_id))

            time.sleep(1)
         

if __name__ == '__main__':
    receiver = Receiver()
    receiver.receive_heartbeat()

    
