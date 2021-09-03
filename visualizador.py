import matplotlib.pyplot as plt
temperaturas=[]
tiempos=[]
import datetime

with open('datos.txt','r') as file:
    lines=file.readlines()

for line in lines: 
    line=line.split('$')
    temperatura = line[3]
    temperatura = temperatura.replace('temperature=','')
    temperatura = temperatura.replace(' *C','')
    temperatura = float(temperatura)
    temperaturas.append(temperatura)
    time = line[1]
    time= time.replace('t=','')
    time= time[:-1]
    print(time)
    time=datetime.datetime.strptime(time,"%Y-%m-%d %H:%M:%S.%f")
    tiempos.append(time)

print(temperaturas)
print(tiempos)
fig, ax =plt.subplots()
ax.plot(tiempos,temperaturas)
plt.show()
