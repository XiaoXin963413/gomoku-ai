import asyncio, json

class GomokuServer(asyncio.Protocol):

    def connection_made(self, transport):
        self.__transport = transport
        self.__address = transport.get_extra_info('peername')
        print('Accepted connection from {}'.format(self.__address))

    def data_received(self, data):
        data = json.loads(data.decode("utf-8"))

        response = self.__parse(data)
        response = json.dumps(response)
        self.__transport.write(response.encode("utf-8"))
        # self.transport.close()

    def connection_lost(self, exc):
        if exc:
            print('client {} error: {}'.format(self.__address, exc))
        else:
            print('client {} closed socket'.format(self.__address))

    def __parse(self, require):
        if (require['chess_record']):
            self.__print_chessborad(require['chess_record'])
        return require

    def __print_chessborad(self, chseeborad):
        for i in chseeborad:
            for j in range(0, len(i)):
                if j == 0:
                    print("[ ", end="")
                print(i[j], end=" ")
                if j == 18:
                    print("]", end="")
            print()

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
