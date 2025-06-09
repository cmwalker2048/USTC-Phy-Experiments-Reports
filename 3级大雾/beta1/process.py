import numpy as np

def func1():
    x = np.loadtxt("./data2.dat",dtype=np.float64,delimiter=" ",usecols=(0),encoding='utf-8')
    y = np.loadtxt("./data2.dat",dtype=np.float64,delimiter=" ",usecols=(1),encoding='utf-8')

    with open("./d2.dat","w") as file:
        for i in range(len(x)):
            file.write("%d %f\n"%(x[i],y[i]-0.177))

#func1()

def func2():
    x = np.loadtxt("./d2.dat",dtype=np.float64,delimiter=" ",usecols=(0),encoding='utf-8')
    y = np.loadtxt("./d2.dat",dtype=np.float64,delimiter=" ",usecols=(1),encoding='utf-8')
    
    '''
    with open("./d3.dat","w") as file:
        for i in range(len(x)):
            file.write("%d %f\n"%(x[i],y[i]/y[0]))
    
    with open("./d4.dat","w") as file:
        for i in range(len(x)):
            file.write("%d %f\n"%(x[i],np.log(y[i]/y[0])))
    '''
    
    with open("./x1.dat","w") as file:
        for i in range(len(x)):
            file.write("%f %f\n"%(x[i]*0.04956,y[i]/y[0]))
            
func2()