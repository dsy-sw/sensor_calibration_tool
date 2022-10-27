class LiDAR:
    manufacturer = {}
    address = {}
    total_info = {}
sensor_addr = {'velodyne_fc':('192.168.30.30',2368),
                'lidar':('192.168.30.1',2368),
                'velodyne_fl':('192.168.30.40',2368),
                'velodyne_fr':('192.168.30.50',2368),
                'velodyne_rr':('192.168.30.60',2368),
                'velodyne_rl':('192.168.30.70',2368),
                'novatel':('192.168.1.11',3007),
                }

sensor_working = {}