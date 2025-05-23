from serial import Serial
import threading
import time


def send()->None:
    ser = Serial(port="/dev/ttyUSB1", baudrate=115200)
    while True:
        data = '12.5|35.55\n'.encode()
        print('Sending Data:' + data.decode())
        ser.write(data)
        print('Data has been sent now')
        print("*********************\n\n")
        time.sleep(10)

def main()->None:
   print("Starting the daemon threads ...")
   threading.Thread(target= send, daemon=False).start()


if __name__ == '__main__':
    main()



