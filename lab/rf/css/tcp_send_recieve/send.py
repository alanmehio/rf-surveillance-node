from serial import Serial
import threading
import time
import array
import struct
import zlib

MAX_PAYLOAD = 32  # max payload size this can change later OK Alan

NULL_CHAR =  b'\0'

def checksum_calculator(data:bytes)->int:
    checksum = zlib.crc32(data)
    return checksum

# 4bytes*2 = 8 bytes
def generate_header(data:bytes)->bytes:
    data_length:int = len(data)
    checksum:int = checksum_calculator(data)
    print(f'Checksum before sending {checksum}')
    print(f'data length before sending {data_length}')
    return struct.pack("!II",data_length,checksum)


def build_packet(payload:str)->list[bytes]:
     data:bytes = payload.encode() + NULL_CHAR
     header:bytes = generate_header(data)
     data = header + data
     # Split data into chunks
     chunks = [data[i:i+MAX_PAYLOAD-2] for i in range(0, len(data), MAX_PAYLOAD-2)]
     indexed_chunks:list[bytes] = []
     for i, chunk in enumerate(chunks):
        packet = bytes([i]) + chunk  # Add packet index
        indexed_chunks.append(packet)
        index:int = packet[0]
        if(index == 0):
            print("HEADER ...")
            header = packet[1:9]
            val = struct.unpack("!II", header)
            print(f"data length is {val[0]}")
            print(f"checksum is {val[1]}")

     print(len(indexed_chunks))
     return indexed_chunks


def send()->None:
    ser = Serial(port="COM3", baudrate=115200)
    while True:
        data = 'Alan Mehio is going to sleep|Alan Mehio is going to sleep Alan Mehio is going to sleep|Alan Mehio is going to sleepAlan Mehio is going to sleep|Alan Mehio is going to sleepAlan Mehio is going to sleep|Alan Mehio is going to sleepAlan Mehio is going to sleep|Alan Mehio is going to sleepAlan Mehio is going to sleep|Alan Mehio is going to sleep'.encode()
        #sum:int = chksum(data)
        #print(str(sum))
        ser.write(data)
        time.sleep(1)



def main()->None:
     payload:str ="This is a large data payload that needs to be split into smaller packets for transmission over RF."
     val:list[bytes] =build_packet(payload)
     print(len(val))


if __name__ == '__main__':
    main()



