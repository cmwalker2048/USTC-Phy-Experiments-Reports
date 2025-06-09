import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

def func_1(B,a,b,c):
    x0 = 384
    y0 = 0.091
    return np.piecewise(B,[B <= x0,B > x0],[lambda B: a*B**2+b*B+y0-a*x0**2-b*x0,lambda B: c*B+y0-x0*c])

def func_2(B,a,b,c):
    x0 = 768
    y0 = 0.363
    return np.piecewise(B,[B <= 768,B > 768],[lambda B: a*B**2+b*B+y0-a*x0**2-b*x0,lambda B: c*B+y0-x0*c])

def draw_1(filepath):
    x = np.loadtxt(filepath,dtype=np.float32,delimiter=",",usecols=(0),encoding='utf-8')
    y = np.loadtxt(filepath,dtype=np.float32,delimiter=",",usecols=(1),encoding='utf-8')
    
    B = 0.001*x * 2400
    R = (y-y[0])/y[0]
    
    #np.piecewise(B,[B <= B[4],B > B[4]],[lambda B: a*B**2+b,lambda B: B])
    p,e = curve_fit(func_1,B,R,bounds=(0,[2.,200.,1.]))
    
    xd = np.linspace(B[0],B[-1],1000)
    
    plt.plot(B,R,'o',label='Data')
    plt.plot(xd,func_1(xd,*p),label='Fitting Curve')
    plt.legend(loc=2,framealpha=1, shadow=True)
    plt.xlabel("$B/Gs$")
    plt.ylabel("$\Delta R / R(0)$")
    plt.title("$\Delta R / R(0)$-$B$ Figure when 1,3 is break")
    plt.show()
    pass

def draw_2(filepath):
    x = np.loadtxt(filepath,dtype=np.float32,delimiter=",",usecols=(0),encoding='utf-8')
    y = np.loadtxt(filepath,dtype=np.float32,delimiter=",",usecols=(1),encoding='utf-8')
    
    B = 0.001*x * 2400
    R = (y-y[0])/y[0]
    
    p,e = curve_fit(func_2,B,R,bounds=(0,[2.,200.,1.]))
    
    xd = np.linspace(B[0],B[-1],1000)
    
    plt.plot(B,R,'o',label='Data')
    plt.plot(xd,func_2(xd,*p),label='Fitting Curve')
    plt.legend(loc=2,framealpha=1, shadow=True)
    plt.xlabel("$B/Gs$")
    plt.ylabel("$\Delta R / R(0)$")
    plt.title("$\Delta R / R(0)$-$B$ Figure when 1,3 is short")
    plt.show()
    pass

#draw_1("./data_close.csv")
draw_2("./data_short.csv")
