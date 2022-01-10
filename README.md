# gpsRead
Python library to interface GPS module 

# GPS Usage
Run below code to get GPS related data
Note: Use port as 'COM1', 'COM2' etc in case of windows machine. Use port as '/dev/ttyUSB0' in case of linux based devices::
```
from gps import gpsRead
if __name__ == '__main__':
    x = gpsRead("COM5",9600)
    while True:
        p = x.get_position()
        print(p)
```
