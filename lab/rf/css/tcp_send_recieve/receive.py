from serial import Serial
import threading
import time
import array

def chksum(packet: bytes) -> int:
    if len(packet) % 2 != 0:
        packet += b'\0' # this is null character in c see

    res = sum(array.array("H", packet))
    res = (res >> 16) + (res & 0xffff)
    res += res >> 16

    return (~res) & 0xffff

def receive()->None:
    ser = Serial(port="COM4", baudrate=115200)
    ser.flush()
    while True:
        #print('ping')
        if ser.in_waiting >0:
            msg = ser.read_all()
            if msg :
                sum:int = chksum(msg)
                print(sum)

        time.sleep(0.01)


def main()->None:
    receive()


if __name__ == '__main__':
    main()



