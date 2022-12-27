import socket, json


class GomokuClient:
    def __init__(self):
        self.__address = "127.0.0.1"
        self.__port = 4000
        self.__response = ""

    def connect(self, cause_error=False):
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.connect((self.__address, self.__port,))
        if cause_error:
            return

        # recv = threading.Thread(target = self.recv_data, args = (sock,))
        # recv.start()

    def send_data(self, data):
        data = json.dumps(data)
        self.sock.sendall(data.encode('utf-8'))

    def recv_data(self):
        self.__response = self.sock.recv(4096)
        return (json.loads(self.__response)) 

        # self.recvdata = json.loads(self.recvdata)

    def recv_until(self, sock, suffix):
        message = sock.recv(4096)
        if not message:
            raise EOFError('socket closed')
        while not message.endswith(suffix):
            data = sock.recv(4096)
            if not data:
                raise IOError('received {!r} then socket closed'.format(message))
            message += data
        return message.decode("utf-8")