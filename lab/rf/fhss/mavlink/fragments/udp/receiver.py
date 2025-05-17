import time
from pymavlink import mavutil

class Receiver():

    def __init__(self):
        pass

    # Function to receive and reassemble fragmented data
    def receive_and_reassemble_data(self,expected_data_length:int):
        mavlink_connection = mavutil.mavlink_connection('udpin:0.0.0.0:14550')
        received_bytes = b''
        received_text = ''
        while True:
            msg = mavlink_connection.recv_match(blocking=True)
            if msg:
                received_text += msg.text
                #received_bytes += msg.get_msgbuf()
                #print(msg.text)
                #print(type(msg))
                #print(f"Received chunk: {msg.text}")
                # Check if all chunks are received (this is a simple example, you may need a more robust method)
                print(len(received_text))
                #if len(received_text) >= expected_data_length:
                #    break

        val:str = received_text
        received_text= ''
        return val
    


if __name__ == '__main__':
   # Set the expected data length for reassembly
   # Alan it is 990 bytes
   #expected_data_length = len(data)
   expected_data_length:int = 99

   # Start receiving and reassembling data
   receiver:Receiver = Receiver()
   reassembled_data = receiver.receive_and_reassemble_data(expected_data_length)
   #print(f"Reassembled data: {reassembled_data}")
   print(len(reassembled_data))