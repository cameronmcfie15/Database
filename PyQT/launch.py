import math
import time
import matplotlib.pyplot as plt

def graph(multiply, divide):
    x=[]
    y=[]
    for i in range(1, 70000, 100):
        angle = multiply * (1 - max(0, (math.log(i / 1000))) / divide)
        #angle = 100 * (1 - max(0, (math.log(i / 1000))) / 4.6)
        print(i, angle)
        x.append(i)
        y.append(angle)
        #time.sleep(1)
        #print(max(0, (math.log(i / 1000)))/4.6)

    del x[0:10]
    del y[0:10]
    plt.plot(x, y)
    plt.show()
    time.sleep(2)
    plt.close()


graph(90, 4.6)

