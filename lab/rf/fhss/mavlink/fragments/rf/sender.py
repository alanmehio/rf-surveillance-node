import time 
from pymavlink import mavutil

class Sender():
  
  def __init__(self, serial_driver_path:str):
    self.serial_driver_path = serial_driver_path
  
  # Function to send fragmented data
  # Mavlink v1 max 250 bytes while mavlink v2 is 280 bytes
  def send_fragmented_data(self,data, chunk_size=250):
    # Create a MAVLink connection
    mavlink_connection = mavutil.mavlink_connection(self.serial_driver_path)
    num_chunks = (len(data) + chunk_size - 1) // chunk_size
    for i in range(num_chunks):
        chunk = data[i * chunk_size:(i + 1) * chunk_size]
        #print(len(chunk))
        custom_message = mavlink_connection.mav.statustext_encode(
            severity=6,  # Severity level (6 is info)
            text=chunk
        )
        print(chunk)
        mavlink_connection.mav.send(custom_message)

if __name__ == '__main__':
    # Example data to send (more than 280 bytes)
    data = 'This is a large data stream that needs to be fragmented into smaller chunks and sent over MAVLink. '.encode()
    print(f'bytes length {len(data)}')
    print(f'string length {len(data.decode())}')
    print(data.decode())
    #Send the fragmented data
    sender:Sender = Sender('/dev/ttyUSB1')
    sender.send_fragmented_data(data, 99)
    print("Fragmented data sent.")

