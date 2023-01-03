import socket

from ...config.classes import SocketType

def open_socket(my_bind:tuple, protocol:str = 'udp', host_bind:tuple = ('',''), buf_size = 4096, timeout:int = 0, all_group:bool = False):
    my_port = my_bind[1]
    if protocol == 'udp':
        _socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, socket.IPPROTO_UDP)
        if all_group:
            _socket.bind("",my_port)
        else:
            _socket.bind(my_bind)
        _socket.settimeout(timeout)
    elif protocol == 'tcp':
        if host_bind == ('',''): return False
        _socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        _socket.setsockopt(socket.SOL_TCP,socket.TCP_NODELAY, 1)
        _socket.bind(my_bind)
        _socket.settimeout(timeout)
        _socket.connect(host_bind)
    _socket.setsockopt(socket.SOL_SOCKET,socket.SO_SNDBUF,buf_size)
    _socket.setsockopt(socket.SOL_SOCKET,socket.SO_RCVBUF,buf_size)
    return _socket

if __name__ == '__main__':
    a = open_socket(('localhost',5555))
    print(a.getsockopt(socket.SOL_SOCKET, socket.SO_RCVBUF))
    
class SocketUtil(SocketType):
    SOCKET_TIMEOUT = 5
    def __init__(self, parent: object=None, ip: str = None, port: int = None, protocol: str = None, socket_type = "server", buf_size = 2048):
        self.parent = parent
        self.ip = str(ip)
        self.port = port
        self.bind: tuple = (ip, port)
        self.raw_data = None
        self.socket_type = socket_type
        self.buf_size = buf_size

        if self.protocol == "tcp":
            self.comm = socket()
        else:
            self.comm = socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    def __repr__(self):
        pass

    def set_buffer(self,buf_size):
        pass

    def connect(self):
        pass
    
    def server_listen(self):
        if self.socket_type == "server":
            pass
        else:
            pass
        pass

    def open_server(self):
        pass

    def open_client(self):
        pass

    def execute(self):
        pass