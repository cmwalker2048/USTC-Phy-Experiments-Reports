import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

def func(x,a,b):
    return a*np.sqrt(x)+b

def one_x(filepath):
    x = np.loadtxt(filepath,dtype=np.float32,delimiter=",",usecols=(0),encoding='utf-8')
    y = np.loadtxt(filepath,dtype=np.float32,delimiter=",",usecols=(1),encoding='utf-8') 

    plot_x = 15.500 + x*0.05
    plot_y = y
    
    plt.plot(plot_x,plot_y,'o',c='red',label="data")
    plt.plot(plot_x,plot_y,'-',c='blue',label="curve")
    plt.legend(loc=1,framealpha=1, shadow=True)
    plt.title("Transmission Sensor $P$-$X$ figure")
    plt.xlabel("$X/mm$")
    plt.ylabel("$P/\mu W$")
    plt.show()

def one_y(filepath):
    x = np.loadtxt(filepath,dtype=np.float32,delimiter=",",usecols=(0),encoding='utf-8')
    y = np.loadtxt(filepath,dtype=np.float32,delimiter=",",usecols=(1),encoding='utf-8')

    x_1 = x[16:24:1]
    x_2 = x[25:31:1]
    x_3 = x[0:6:1]
    x_4 = x[7:15:1]
    
    y_1 = y[16:24:1]*0.001
    y_2 = y[25:31:1]
    y_3 = y[0:6:1]
    y_4 = y[7:15:1]*0.001
    
    x_0_1 = np.append(x_1,x_2)
    x_0_2 = np.append(x_3,x_4)
    y_0_1 = np.append(y_1,y_2)
    y_0_2 = np.append(y_3,y_4)
    
    plot_x_1 = np.append(x_0_1,x_0_2)
    plot_y = np.append(y_0_1,y_0_2)
    
    plot_x = plot_x_1*0.01 + 12.250
    
    plt.plot(plot_x,plot_y,'o',c='red',label='data')
    plt.plot(plot_x,plot_y,'-',c='blue',label='curve')
    plt.legend(loc=1,framealpha=1, shadow=True)
    plt.title("Transmission Sensor $P$-$Y$ figure")
    plt.xlabel("$Y/mm$")
    plt.ylabel("$P/\mu W$")
    plt.show()

def two(filepath):
    x = np.loadtxt(filepath,dtype=np.float32,delimiter=",",usecols=(0),encoding='utf-8')
    y = np.loadtxt(filepath,dtype=np.float32,delimiter=",",usecols=(1),encoding='utf-8')

    plot_x = 3.05 + x*0.05
    plot_y = y
    
    plt.plot(plot_x,plot_y,'o',c='red',label='data')
    plt.plot(plot_x,plot_y,'-',c='blue',label='curve')
    plt.legend(loc=1,framealpha=1, shadow=True)
    plt.title("Reflection Sensor $P$-$X$ Figure")
    plt.xlabel("$X/mm$")
    plt.ylabel("$P/\mu W$")
    plt.show()

def three(filepath):
    x = np.loadtxt(filepath,dtype=np.float32,delimiter=",",usecols=(0),encoding='utf-8')
    y = np.loadtxt(filepath,dtype=np.float32,delimiter=",",usecols=(1),encoding='utf-8')

    plot_x = 18.5 + x*0.05
    plot_y = y
    
    
    popt, pcov = curve_fit(func, plot_x, plot_y,bounds=(0, [1., 1.]))
    
    y_fit = [func(i,*popt) for i in plot_x]
    y_back = [func(i,*popt) for i in plot_y]
    
    plt.plot(plot_x,plot_y,'o',c='red',label='data')
    plt.plot(plot_x,plot_y,'-',c='blue',label='curve')
    plt.legend(loc=1,framealpha=1, shadow=True)
    plt.title("Bend Sensor $P$-$X$ Figure")
    plt.xlabel("$X/mm$")
    plt.ylabel("$P/\mu W$")
    plt.show()

#one_x("./1_x.csv")
#one_y("./1_y.csv")
#two("./2.csv")
three("./3.csv")