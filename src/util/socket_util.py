import socket

from config.classes import SocketType

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
    def __init__(self, ip: str, port: int):
        self.ip = ip
        self.velodyne =
        self.port = port
    
    def __repr__(self):
        pass

    def set_buffer(self,buf_size):
        pass

    def open_server(self):
        pass

    def open_client(self):
        pass