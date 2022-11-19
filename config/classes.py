import platform

if platform.system() == "Linux":
    #!/usr/bin/python3.10
    print("Version Linux")

from dataclasses import dataclass
from time import time
import sys
import os

sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
print(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))

from config.constants import *



@dataclass
class Base():
    name: str
    start_time: time


@dataclass
class SensorType(Base):
    dev_type: str
    manufacturer: str
    status: int = STAT.DISCONNECTED
    last_update: float = 0
    update_rate: float = 0    # hz

@dataclass
class ScoketType(Base):
    ip: str
    port:int
    protocol:str
    client_bind: tuple = (ip,port)
    
@dataclass
class Velodyne(SensorType):
    raw_data:bytes = 0
    velo:bool = 1