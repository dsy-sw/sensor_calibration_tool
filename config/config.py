class SensorInfo:
    manufacturer_list = ['velodyne','septentrio','ouster','novatel','mike'] 

    sensor_dict = {'velodyne':'lidar', 'autoroad':'radar', 'novatel':'gnss'}
    # name_match = {['velodyne16', 'velodyne32', 'velodyne64', 'ouster16']:'lidar',
    #             ['novatel', 'septentrio']:'gnss',
    #             ['autoroad']:'radar'}

    position = {}

class Default:
    SENSER_CONNECT_DEFAULT = 'tcp'
    SOCKET_TIMEOUT_DEAFULT = 5

class Velodnye:
    RECV_BUFFER = 1248