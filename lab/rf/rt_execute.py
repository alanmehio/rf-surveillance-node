'''
alan@lenovo:~$ ls -l /dev/serial/by-id
total 0
lrwxrwxrwx 1 root root 13 Mar 19 20:25 usb-FTDI_FT231X_USB_UART_D30EZ3WR-if00-port0 -> ../../ttyUSB1
lrwxrwxrwx 1 root root 13 Mar 19 20:23 usb-FTDI_FT231X_USB_UART_D30EZ7O4-if00-port0 -> ../../ttyUSB0
alan@lenovo:~$ 

id1 = D30EZ3WR
id2 = D30EZ7O4

Alan: change mode 
sudo chmod a+rw /dev/ttyUSB0 and ttyUSB1



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




# recieve heartbeat message
from pymavlink import mavutil

# Connect to the MAVLink device
connection = mavutil.mavlink_connection('tcp:localhost:5760')

# Wait for a heartbeat from the device
connection.wait_heartbeat()
print("Heartbeat received from system (system %u component %u)" % (connection.target_system, connection.target_component))


while True:
    # Receive a message
    message = connection.recv_match(blocking=True)
    if message is not None:
        print(message)
Handle specific messages: You can also handle specific types of messages by checking the message type. For example, to handle heartbeat messages:

while True:
    message = connection.recv_match(blocking=True)
    if message is not None:
        if message.get_type() == 'HEARTBEAT':
            print("Heartbeat received from system %u component %u" % (message.system_id, message.component_id))


    '''

from pymavlink import mavutil

def send_heartbeat():
        master = mavutil.mavlink_connection("/dev/ttyUSB0",baud=57600)
       # master.wait_heartbeat()
        heartbeat_msg = master.mav.heartbeat_encode(
        type=mavutil.mavlink.MAV_TYPE_QUADROTOR,
        autopilot=mavutil.mavlink.MAV_AUTOPILOT_ARDUPILOTMEGA,
        base_mode=0,
        custom_mode=0,
        system_status=mavutil.mavlink.MAV_STATE_ACTIVE)
        
        # send the heartbeat message
        master.mav.heartbeat_send(mavutil.mavlink.MAV_TYPE_ONBOARD_CONTROLLER,
                                  mavutil.mavlink.MAV_AUTOPILOT_INVALID,0,0,0)
        
def receive_heartbeat():
        # Connect to the MAVLink device
         print("Receiver: Before connecting")
         connection = mavutil.mavlink_connection("/dev/ttyUSB1", baud=57600)
         print("Receiver:After connecting")
         connection.wait_heartbeat()
         print(f'Heartbeat recieved from system(system {connection.target_system} component {connection.target_component}')
         print(f'Heartbeat recieved system {connection.address}')
         while True:
             # Receive a message 
             print('receive1...')
             message = connection.recv_match(blocking=True)
             print('receive2..')
             if message is not None:
                 if message.get_type == 'HEARTBEAT':
                      print("Alan HeartBeat")
                 print(message)

def main():
  send_heartbeat()
  receive_heartbeat() 


if __name__ == "__main__":
   main()
