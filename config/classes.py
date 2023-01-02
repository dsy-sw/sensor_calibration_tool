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
class Base:
    name: str
    start_time: time


@dataclass
class SensorType(Base):
    dev_type: str
    manufacturer: str
    status: int = STAT.DISCONNECTED
    last_update: float = 0  # unit: sec
    update_rate: float = 0    # hz
    translation:tuple = (0, 0, 0)  # unit: meter
    rotation:tuple = (0, 0, 0)  # unit: meter
    

@dataclass
class SocketType():
    ip: str
    port:int
    protocol:str
    client_bind: tuple = (ip,port)
    
    
@dataclass
class Velodyne(SensorType):
    raw_data: bytes = 0
    velo: bool = 1
    client_bind: tuple = (ip,port)
    
    
@dataclass
class LidarType(SensorType, SocketType):
    model_name: str
    frame_id: int
    horizeontal_range: tuple(int,int)
    vertical_channel: tuple(int,int)
    frame_rate: int
    rpm: int
    
'''
frame_id: "velodyne32"
scan_channel: "/apollo/sensor/velodyne32/VelodyneScan"
rpm: 600.0
model: HDL32E
mode: STRONGEST
firing_data_port: 8308
use_sensor_sync: false
max_range: 130.0
min_range: 0.4
use_gps_time: true
calibration_online: false
calibration_file: "/apollo/modules/drivers/lidar/velodyne/params/HDL32E_calibration_example.yaml"
organized: false
convert_channel_name: "/apollo/sensor/velodyne32/PointCloud2"
use_poll_sync: true
is_main_frame: true
'''


    
'''
• Channels: 32
• Measurement Range: 200 m
• Range Accuracy: Up to ±3 cm (Typical)2
• Horizontal Field of View: 360°
• Vertical Field of View: 40° (-25° to +15°)
• Minimum Angular Resolution (Vertical): 0.33° (non-linear distribution)
• Angular Resolution (Horizontal/Azimuth): 0.1° to 0.4°
• Frame Rate: 5 Hz to 20 Hz
• Integrated Web Server for Easy Monitoring and Configuration
'''
