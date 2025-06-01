# from https://www.geeksforgeeks.org/struct-module-python/
# https://docs.python.org/3/library/stdtypes.html#bytearray
# https://docs.python.org/3/library/struct.html

import struct
import zlib

def checksum_calculator(data:bytes):
    checksum = zlib.crc32(data)
    return checksum

data = "Hello world"
packet = data.encode()
checksum_sent = checksum_calculator(packet)


source_port=1111
destination_port = 1112
data_length = len(packet)
upd_header_bytes_sent = struct.pack("!IIII", source_port,destination_port,data_length,checksum_sent)
print(len(upd_header_bytes_sent))
#   packet += b'\0' # this is null character in c see
terminating_char =  b'\0'
packet_with_header = upd_header_bytes_sent + packet

# receive now
upd_header_bytes_received = packet_with_header[:16]
data_received = packet_with_header[16:]
upd_header_received = struct.unpack("!IIII", upd_header_bytes_received)
check_sum_received = upd_header_received[3]
if checksum_sent == check_sum_received:
    print("CORRECT......YES")

