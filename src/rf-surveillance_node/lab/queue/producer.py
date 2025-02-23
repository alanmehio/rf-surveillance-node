import asyncio

class Producer():

    def __init__(self):
        pass

    async def create_queue(self):
        self.queue = asyncio.Queue


    async def get_queue(self):
        return self.queue
    
    async def add_task(self,w)