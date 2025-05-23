from serial import Serial
import threading
import time

def receive()->None:
    # master = mavutil.mavlink_connection("/dev/ttyUSB0",baud=57600)
    ser = Serial(port="/dev/ttyUSB0", baudrate=115200)
    while True:
        print("Trying to recieve ...")
        #data = ser.read_until(b'\n')
        data = ser.read_all()
        #message = data.decode()
        print('Receiving Data:' + str(data))
        print("*******************\n\n")
        time.sleep(5)


def main()->None:
   print("Starting the daemon threads ...")
   threading.Thread(target=receive, daemon=False).start()


if __name__ == '__main__':
    #data = '12.5|13.55\n'.encode()
    #print('Sending Data:' + data.decode())
    main()



