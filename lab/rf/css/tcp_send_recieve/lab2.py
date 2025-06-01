import struct
import zlib

MAX_PAYLOAD = 32  # max payload size this can change later OK Alan

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

def send()->None:
     null_char =  b'\0'
     data = b"This is a large data payload that needs to be split into smaller packets for transmission over RF." + null_char
     #print(len(data))
     header:bytes = generate_header(data)
     #print(len(header))
     payload = header + data
     #print(len(payload))

    # Split data into chunks
     chunks = [payload[i:i+MAX_PAYLOAD-2] for i in range(0, len(payload), MAX_PAYLOAD-2)]

     for i, chunk in enumerate(chunks):
        packet = bytes([i]) + chunk  # Add packet number
        index:int = packet[0]
        #print(packet[0]) #
        if(index == 0):
            print("HEADER ...")
            header = packet[1:9]
            # upd_header_received = struct.unpack("!IIII", upd_header_bytes_received)
            val = struct.unpack("!II", header)
            print(f"data length is {val[0]}")
            print(f"checksum is {val[1]}")

         #radio.write(packet) Alan package is sent
        success = True
        #if not success:
         #   print(f"Failed to send packet {i}")
        #else:
        #    print(f"Sent packet {i}")


def receive()->None:
    received_chunks = {}
    expected_packets = None
    while True:
        if radio.available():
            buffer = []
            radio.read(buffer, radio.getDynamicPayloadSize())
            packet = bytes(buffer)
            packet_num = packet[0]
            chunk = packet[1:]
            received_chunks[packet_num] = chunk
            print(f"Received packet {packet_num}")

        # Optional: break when all expected packets are received
        if expected_packets and len(received_chunks) == expected_packets:
            break

    # Reassemble data
    data = b''.join(received_chunks[i] for i in sorted(received_chunks))
    print("Reassembled data:", data.decode())


#if __name__ == '__main__':
if __name__ == '__main__':
   send()


'''
b'\x00'
  b'\x01'
   b'\x02
Add a header with total packet count or a terminator byte.
Use CRC32 or hashes to verify integrity.
Implement ACK/NAK for each packet.
Consider timeouts and retries.

'''