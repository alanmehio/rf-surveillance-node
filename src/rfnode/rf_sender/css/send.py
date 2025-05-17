from serial import Serial
import threading
import time


def send()->None:
    ser = Serial(port="COM4", baudrate=115200)
    while True:
        #data = '12.5|35.55\n'.encode()#
        data = '12.55|35.55'.encode()
        print('Sending Data:' + data.decode())
        ser.write(data)
        print('Data has been sent now')
        print("*********************\n\n")
        time.sleep(0.2) # 200 ms

def main()->None:
   print("Starting the daemon threads ...")
   threading.Thread(target= send, daemon=False).start()


if __name__ == '__main__':
    main()



