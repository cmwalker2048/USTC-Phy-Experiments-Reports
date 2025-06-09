import numpy as np
import matplotlib.pyplot as plt

filepath = "./3.csv"

x = np.loadtxt(filepath,dtype=np.float32,delimiter=",",usecols=(0),encoding='utf-8')
y = np.loadtxt(filepath,dtype=np.float32,delimiter=",",usecols=(1),encoding='utf-8')

plt.plot(x,y,"-X")
plt.xlabel("$U_{working}/V$")
plt.ylabel("$Counting$")
plt.show()