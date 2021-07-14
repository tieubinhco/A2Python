import serial
import time
arduino = serial.Serial('COM4', 115200, timeout=0.1)
# while True:
# # the last bit gets rid of the new-line chars
# data = arduino.readline()[:-2]
# if data:
#     print(data)
while 1:
    data = arduino.readline()
    print(data)
    f = open('myfile.txt', 'a')
    data = str(data)
    f.write(data)
    f.close()
    time.sleep(1)
