import asyncio, json

class GomokuServer(asyncio.Protocol):

    def connection_made(self, transport):
        self.transport = transport
        self.address = transport.get_extra_info('peername')
        print('Accepted connection from {}'.format(self.address))

    def data_received(self, data):
        data = data.decode("utf-8")
        print(data)
        self.transport.write("Fuck".encode())
        self.transport.close()
        # self.data = json.loads(data)

    def connection_lost(self, exc):
        if exc:
            print('Client {} error: {}'.format(self.address, exc))
        else:
            print('Client {} closed socket'.format(self.address))


def RunServer():
    address = ("127.0.0.1", 4000)
    loop = asyncio.get_event_loop()
    coro = loop.create_server(GomokuServer, *address)
    server = loop.run_until_complete(coro)
    print('Listening at {}'.format(address))
    try:
        loop.run_forever()
    finally:
        server.close()
        loop.close()
