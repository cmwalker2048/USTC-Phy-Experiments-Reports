import numpy as np

filepath = "./b_1.dat"
x = np.loadtxt(filepath,dtype=np.float64,delimiter=",",usecols=(3),encoding='utf-8')

def ave():
    sum = 0
    for i in range(len(x)):
        sum += x[i]
    ave = sum/(len(x))
    print(ave)
    