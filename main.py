from gps import gpsRead
if __name__ == '__main__':
    x = gpsRead("COM5",9600)
    while True:
        p = x.get_position()
        print(p)