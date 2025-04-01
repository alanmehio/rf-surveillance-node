import time 
from pymavlink import mavutil

class Sender():
  
  def __init__(self):
    pass
  
  # Function to send fragmented data
  # Mavlink v1 max 250 bytes while mavlink v2 is 280 bytes
  def send_fragmented_data(self,data, chunk_size=250):
    # Create a MAVLink connection
    mavlink_connection = mavutil.mavlink_connection('udpout:0.0.0.0:14550')
    num_chunks = (len(data) + chunk_size - 1) // chunk_size
    for i in range(num_chunks):
        chunk = data[i * chunk_size:(i + 1) * chunk_size]
        print(len(chunk))
        custom_message = mavlink_connection.mav.statustext_encode(
            severity=6,  # Severity level (6 is info)
            text=chunk
        )
        mavlink_connection.mav.send(custom_message)

if __name__ == '__main__':
    # Example data to send (more than 280 bytes)
    data = b'This is a large data stream that needs to be fragmented into smaller chunks and sent over MAVLink. ' * 10
    print(len(data))
    print(str(data))
    #Send the fragmented data
    sender:Sender = Sender()
    sender.send_fragmented_data(data)
    print("Fragmented data sent.")

