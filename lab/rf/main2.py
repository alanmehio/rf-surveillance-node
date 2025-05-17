"""
    If you have a companion computer on your vehicle, you can send a status text
    message from the companion computer to the GCS using the MAVLink protocol to
    inform the user of the status of the process running on the companion computer.

    This is useful for debugging and for creating and sending messages to the GCS
    that are not part of the standard MAVLink protocol. And also the companion
    computer uses the MAVLink protocol and underlying infrastructure.

    This example assumes that you have a companion computer on your vehicle and
    that you have a UDP connection between the companion computer and the GCS.

    Device string for UDP connection: "udpout:127.0.0.1:14560" means that the
    companion computer acts as a source component (like the autopilot on the
    MAVLink connection) and sends messages to the GCS on the local machine.

    At the ardu-sim.sh, replace the "--out 127.0.0.1:14560" with "--master 127.0.0.1:14560"

    https://mavlink.io/en/messages/common.html#STATUSTEXT
"""

import time
import os
import random
from threading import Thread
import pymavlink.mavutil as utility
import pymavlink.dialects.v10.all as dialect

class Sender2(Thread):
    def __init__(self):
        Thread.__init__(self)

    def send_text_message(self):
        # create serial connection
        connection = utility.mavlink_connection("/dev/ttyUSB0", baud=115200)
        # inform user about the protocol used
        print(os.environ['MAVLINK_DIALECT'])
        
        # create an infinite loop
        while True:

            # create the text
            #text = f"Roll a dice: {random.randint(1,6)} flip a coin: {random.randint(0,1)}"
            text = "Alan Mehio"
            # create STATUSTEXT message
            message = dialect.MAVLink_statustext_message(severity=dialect.MAV_SEVERITY_INFO,
                                                 text=text.encode())

            # send message to the GCS
            connection.mav.send(message)
            print("Message Sent")

            # sleep a bit
            time.sleep(0.5)


    def run(self):
        print(f'Thread running: {self.name}')
        self.send_text_message()


class Receiver2(Thread):

    def __init__(self):
         Thread.__init__(self)

    def receive_text_message(self):
        connection = utility.mavlink_connection("/dev/ttyUSB1", baud=115200)
        print(os.environ['MAVLINK_DIALECT'])
        # infinite loop
        while True:

            # try to receive a message
            try:

                # receive a message
                message = connection.recv_match(type=None,blocking=False)
                # convert received message to dictionary
                if(message is not None):
                    message = message.to_dict()
                    print(message['reason'])
                    # for each field name in field names of this message
                    for field_name in dialect.MAVLink_statustext_message.fieldnames:

                        # if the field is system boot time in milliseconds
                        if field_name == "text":
                            # print field name and contained field value
                            print(field_name, message[field_name])

            # exit on Ctrl+C
            except KeyboardInterrupt:
                print("User interrupt received, exiting.")
                exit(0)

            # bare except to catch all the exceptions
            except Exception as e:
                # print error message
                print(f"Error occurred: {e}")

            # tiny sleep to cool down the terminal
            time.sleep(0.010)

    def run(self):
        print(f'Thread running: {self.name}')
        self.receive_text_message()


if(__name__) == "__main__":
    # set_dialect(os.environ['MAVLINK_DIALECT'])
    #os.environ['MAVLINK_DIALECT'] = 'MAVLINK'
    sender = Sender2()
    sender.start()
   
    print(Thread.name)
    receiver = Receiver2()
    receiver.start()

    sender.join()
    receiver.join()

