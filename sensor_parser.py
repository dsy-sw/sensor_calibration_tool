import socket
import logging.config
from threading import Thread
from time import sleep

import config.parameters as param
from config.config import *

logging.config.fileConfig('./config/logging.conf')
lidar_log = logging.getLogger('lidar')
gnss_log = logging.getLogger('gnss')
radar_log = logging.getLogger('radar')

class SensorParcer():
    def __init__(self, sensor_name,
                connect_type = Default.SENSER_CONNECT_DEFAULT,
                timeout = Default.SOCKET_TIMEOUT_DEAFULT):

        self.run_stat = True

        self.working_sensor = False
        self.raw_dara = ''
        self.data = ''
        self.sensor_name = sensor_name
        self.connect_type = connect_type
        self.timeout = timeout

        self._runParser = True
        target_sensor = {'lidar':self.lidar_run, 'radar':self.radar_run, 'gnss':self.gnss_run}
        self._sensorThread = Thread(target = target_sensor[sensor_name], name = self.sensor_name, daemon=True)

    def open_tcp_socket(self):
        def_fname = f'{self.sensor_name}: {self.open_tcp_socket.__name__}'
        connect_stat = False
        SNESOR_ADDR = param.sensor_addr[self.sensor_name]

        while not connect_stat:
            try:
                sensorServer =  socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                sensorServer.bind(SNESOR_ADDR)
                sensorServer.connect()
                sensorServer.settimeout(self.timeout)
                connect_stat = True

            except (ConnectionError, ConnectionAbortedError, ConnectionRefusedError) as err:
                connect_stat = False
                sensorServer.close()
                print(f'Raise Error... {def_fname}: {err}')
                sleep(3)

        return sensorServer
    
    def open_udp_socket(self) -> socket.socket:
        def_name = f'{self.sensor_name}--{self.open_udp_socket.__name__}'
        connect_stat = False
        SNESOR_ADDR = param.sensor_addr[self.sensor_name]

        while not connect_stat:
            try:
                sensorServer = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
                sensorServer.bind(SNESOR_ADDR)

                sensorServer.settimeout(self.timeout)
                connect_stat = True
                
            except (ConnectionError, ConnectionAbortedError, ConnectionRefusedError, Exception) as err:
                connect_stat = False
                sensorServer.close()
                sleep(3)
                print(f'Raise Error... {def_name} : {err}')

        return sensorServer

    def lidar_parser(self):
        def_name = f'{self.sensor_name}--{self.lidar_parser.__name__}'
        
        
    def parsing(self):
        def_name = f'{self.sensor_name}--{self.parsing.__name__}'

    def lidar_run(self):
        def_name = f'{self.sensor_name}--{self.lidar_run.__name__}'
        lidar_run = True
        while lidar_run:
            parser_run = True
            lidar_run = False
            if self.connect_type == 'tcp':
                lidar = self.open_tcp_socket()
            elif self.connect_type == 'udp':
                lidar = self.open_udp_socket()
            else: 
                print(f'{def_name}: Connect Type Error')
                parser_run = False
                lidar_run = True
            sleep(5)
            
        while parser_run:
            try:
                # print(f'{lidar = }')
                self.raw = lidar.recv(Velodnye.RECV_BUFFER)
                # self.lidar_parser()
                lidar_log.info(f'{param.sensor_addr[self.sensor_name]},{self.raw}')
                sleep(1/6)
            except Exception as err:
                print(f'{def_name}: {err} ')
                parser_run = False
                lidar.close()
                sleep(5)

        
    def gnss_run(self):
        def_name = f'{self.sensor_name}--{self.gnss_run.__name__}'

    def radar_run(self):
        def_name = f'{self.sensor_name}--{self.radar_run.__name__}'

    def get_data(self):
        def_name = f'{self.sensor_name}--{self.get_data.__name__}'
        if not self.data:
            return self.data
        else:
            print(f'{def_name}: Empty data!')
            return 0

    def run(self):
        def_name = f'{self.sensor_name}--{self.run.__name__}'

        while self.run_stat:
            if self._runParser and not self._sensorThread.is_alive():
                try:
                    self._sensorThread.start()
                except Exception as err:
                    print(f'Raise Error... {def_name} : {err}')
                    
            sleep(5)

if '__main__' == __name__:
    request_sensor = []
    sensor = SensorParcer('lidar', connect_type='udp')
    sensor.run()