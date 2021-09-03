import matplotlib.pyplot as plt
temperaturas=[]
tiempos=[]
humidity_list=[]
list_heat=[]
dummy=[]
import datetime

def format_text(line,variable,unit,pos):
    try:
        name=variable
        variable=line[pos]
        string="{}=".format(name)
        variable = variable.replace(string,'')
        variable = variable.replace(" {}".format(unit),'')
        variable = float(variable)
        return variable
    except:
        pass
    

with open('datos.txt','r') as file:
    lines=file.readlines()
    

for line in lines:
    try:
        line=line.split('$')
        temperatura = format_text(line,"temperature","*C",3)
        temperaturas.append(temperatura)
        humidity=format_text(line,"humidity","%",2)
        heat_index=format_text(line,"heat_index","*C",4)
        time = line[1]
        time= time.replace('t=','')
        time= time[:-1]
        #print(humidity)
        time=datetime.datetime.strptime(time,"%Y-%m-%d %H:%M:%S.%f")
        tiempos.append(time)
        humidity_list.append(humidity)
        list_heat.append(heat_index)
        dummy.append(heat_index-temperatura)
    except:
        pass

#print(humidity_list)
#print(tiempos)
fig, ax =plt.subplots(2,2)
ax[0,0].plot(tiempos,temperaturas)
ax[0,0].set_title("Temperature")
ax[0,0].set(xlabel="datetime",ylabel="Celsius (*C)")
ax[1,0].plot(tiempos,humidity_list)
ax[1,0].set_title("Humidity")
ax[1,0].set(xlabel="datetime",ylabel="Humidity (%)")
ax[1,1].plot(tiempos,list_heat)
ax[1,1].set_title("Heat index")
ax[1,1].set(xlabel="datetime",ylabel="Heat Index (*C)")
ax[0,1].plot(tiempos,dummy)
ax[0,1].set_title("Diff")
ax[0,1].set(xlabel="datetime",ylabel="Celsius (*C)")
plt.show()
