import asyncio
import numpy as np

class Server():
    frequencies:np.array
    
    async def handle_client(self,reader, writer):
        addr = writer.get_extra_info('peername')
        # see https://docs.python.org/3/library/asyncio-stream.html
        byte_object  = await reader.read(220000) # bytes type fix me we need a better way to read readuntil seems not working
        print(f'Received bytes size {len(byte_object)} from  {addr!r}')
        frequencies =np.frombuffer(byte_object,np.float64)
        print(f'received numpy array length {len(frequencies)}')
        print(type(frequencies))
        print(frequencies[0])

    async def start(self):
        server = await  asyncio.start_server(self.handle_client, '127.0.0.1',8888)
        addrs = ','.join(str(sock.getsockname()) for sock in server.sockets)
        print(f'Serving on {addrs}')

        async with server:
            await server.serve_forever()

server = Server()
asyncio.run(server.start())
    