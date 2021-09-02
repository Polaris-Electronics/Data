import datetime as dt
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import random
import serial
import time
arduino = serial.Serial("/dev/ttyACM4",9600)


# Create figure for plotting
fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)
xs = []
ys = []


def animate(i, xs, ys):
    try:
        raw = arduino.readline()
        t_string = raw.decode()
        temp = t_string.split("##")
        #print(t_string)
        print(temp)
        temperatura=temp[6]
        temperatura=temperatura.split()
        temperatura=temperatura[0]
        print(temperatura)
        #arduino.flushInput()
    except:
        temperatura=0

    # Read temperature (Celsius) from TMP102
    temp_c = float(temperatura)

    # Add x and y to lists
    xs.append(dt.datetime.now().strftime('%H:%M:%S.%f'))
    ys.append(temp_c)

    # Limit x and y lists to 20 items
    xs = xs[-20:]
    ys = ys[-20:]

    # Draw x and y lists
    ax.clear()
    ax.plot(xs, ys)

    # Format plot
    plt.xticks(rotation=45, ha='right')
    plt.subplots_adjust(bottom=0.30)
    plt.title('Temperature over Time')
    plt.ylabel('Temperature (deg C)')

# Set up plot to call animate() function periodically
ani = animation.FuncAnimation(fig, animate, fargs=(xs, ys), interval=1)
plt.show()
