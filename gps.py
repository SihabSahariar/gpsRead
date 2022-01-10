#Developed By Sihab Sahariar

import serial
class gpsRead:
    def __init__(self, port, baudrate):
        self.gps_port = serial.Serial(port, baudrate)

    def get_position(self):
        try:
            s = (self.gps_port.read(500)).decode('utf-8')
            data = s.splitlines()
            for i in range(len(data)):
                d = data[i].split(',')
                if d[0] == "$GPGGA" and len(d) == 15:
                    if d[2] == '' or d[4] == '':
                        return ["None", "None"]
                    else:
                        lat = float(d[2]) / 100
                        long = float(d[4]) / 100
                        return [lat, long]
        except:
            return ['error','error']


    
