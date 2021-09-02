import serial
import time
import csv
import threading
arduino = serial.Serial("/dev/ttyACM3",9600)

def store_data(time,temperature,pressure,humidity):
    append = [time,temperature,pressure,humidity]
    with open('datos.txt', 'w') as csvFile:
        csvFile.write(time)
    csvFile.close()


while True:
    try:
        raw = arduino.readline()
        t_string = raw.decode()
        temp = t_string.split("##")
        #print(t_string)
        #print(temp)
        temperatura=temp[6]
        temperatura=temperatura.split()
        temperatura=temperatura[0]
        print(temperatura)
        store_data()
        
    except:
        pass
