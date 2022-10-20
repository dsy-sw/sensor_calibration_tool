from config.classes import SensorType
from src.util.socket_util import open_socket

class NovatelDriver(SensorType):
    def __init__(self, sock):
        self.sock = sock
    
    def __repr__(self):
        pass
    
    def raw_parser(self):
        pass

    def run(self):
        pass
        