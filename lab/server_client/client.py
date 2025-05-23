import asyncio
import numpy as np

class Client():

  async def send(self,arr:np.array):
    reader, writer = await asyncio.open_connection(
        '127.0.0.1',8888)
    
    bytes_message = arr.tobytes()
    print(f'bytes size is {len(bytes_message)}') # bytes size is 127600

    print(f'Send: np.array')
    writer.write(bytes_message)
    #writer.write(b'\n') # end of line indicator
    await writer.drain()

    #data = await reader.read(100)
    #print(f'Received:{data.decode()!r}')

    print('Close the connection')
    writer.close()
    await writer.wait_closed()

# frequencies = np.arange(105.5, 106.5,1,np.float64)
frequencies = np.arange(105.5e6, 106.5e6, 100, np.float64)
print(f' array length {len(frequencies)}')
print(frequencies[0])
client = Client()
asyncio.run(client.send(frequencies))



