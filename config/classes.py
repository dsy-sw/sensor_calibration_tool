import platform
if platform.system() == "Linux":
    #!/usr/bin/python3.10
    pass

from dataclasses import dataclass
from time import time
import sys
import os

sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
print(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))

from config.constants import *



@dataclass
class DataBase:
    name: str
    start_time: time()
    status: int = STATE.DISCONNECTED
    last_update: float = 0
    update_rate: float = 0    # hz

@dataclass
class Sensor:
    dev_type: str
    manufacturer: str
    ip: int
    port: int

class Lidar(DataBase, Sensor):
    def __init__(self):
        self.raw_data: bytes = None