import serial
import time
import csv
import threading
from datetime import datetime
arduino = serial.Serial("/dev/ttyACM1",9600)

def store_data(humedad,temperature,indice_calor):
    time = datetime.now()
    with open('datos.txt', 'a') as csvFile:
        csvFile.write(" $t={} $humidity={} $temperature={}  $heat_index={}\n".format(time,humedad,temperature,indice_calor))
    csvFile.close()


while True:
    try:
        raw = arduino.readline()
        t_string = raw.decode()
        temp = t_string.split("##")
        #print(t_string)
        print(temp)
        humedad=temp[0]
        temperature=temp[1]
        indice_calor=temp[2]
        print(indice_calor)
        store_data(humedad,temperature,indice_calor)
    except:
        pass
        
