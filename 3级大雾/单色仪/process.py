import numpy as np

def process(dst,filename):
    x = np.loadtxt(dst,dtype=np.float32,delimiter=" ",usecols=(0),encoding='utf-8')
    y = np.loadtxt(dst,dtype=np.float32,delimiter=" ",usecols=(1),encoding='utf-8')
    
    nx = []
    
    for i in range(len(x)):
        nx.append(x[i]+(i%8)*0.0125)
    
    with open(filename,"w") as out:
        for j in range(len(nx)):
            out.write("%f %f\n"%(nx[j],y[j]))

def div(in1,in2,out):
    x1 = np.loadtxt(in1,dtype=np.float32,delimiter=" ",usecols=(0),encoding='utf-8')
    x2 = np.loadtxt(in2,dtype=np.float32,delimiter=" ",usecols=(0),encoding='utf-8')
    y1 = np.loadtxt(in1,dtype=np.float32,delimiter=" ",usecols=(1),encoding='utf-8')
    y2 = np.loadtxt(in2,dtype=np.float32,delimiter=" ",usecols=(1),encoding='utf-8')

    ny = []
    for i in range(len(x1)):
        ny.append(y1[i]/y2[i])
    
    with open(out,"w") as out:
        for j in range(len(ny)):
            out.write("%f %f\n"%(x1[j],ny[j]))

def normalize(dst,out):
    x = np.loadtxt(dst,dtype=np.float32,delimiter=" ",usecols=(0),encoding='utf-8')
    y = np.loadtxt(dst,dtype=np.float32,delimiter=" ",usecols=(1),encoding='utf-8')
    
    ny = []
    sum = 0
    nny = []
    summ = 0
    
    for i in range(len(x)):
        if(i != 0):
            sum += y[i]*(x[i]-x[i-1])
    #for i in range(len(x)):
    #    ny.append(1-y[i]/sum)
    #'''
    for i in range(len(x)):
        ny.append(y[i]/sum)
    #'''
    #for i in range(len(x)):
    #    if(i != 0):
    #        summ += ny[i]*(x[i]-x[i-1])
    #for i in range(len(x)):
    #    nny.append(ny[i]/summ)
    
    with open(out,"w") as out:
        for j in range(len(ny)):
            out.write("%f %f\n"%(x[j],ny[j]))

#process("./data/r_3_2.txt","./data/neo/r_3_2.txt")
#div("./data/r_2_2.txt","./data/r_3_2.txt","./data/neo/ddiv1.txt")
normalize("./data/neo/ddiv1.txt","./data/neo/nn_1.txt")