MAX_PAYLOAD = 32  # nRF24L01+ max payload size

def send()->None:
    data = b"This is a large data payload that needs to be split into smaller packets for transmission over RF."
    # Split data into chunks
    chunks = [data[i:i+MAX_PAYLOAD-2] for i in range(0, len(data), MAX_PAYLOAD-2)]

    for i, chunk in enumerate(chunks):
        packet = bytes([i]) + chunk  # Add packet number
        success = True  #radio.write(packet)
        if not success:
            print(f"Failed to send packet {i}")
        else:
            print(f"Sent packet {i}")


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
Add a header with total packet count or a terminator byte.
Use CRC32 or hashes to verify integrity.
Implement ACK/NAK for each packet.
Consider timeouts and retries.

'''