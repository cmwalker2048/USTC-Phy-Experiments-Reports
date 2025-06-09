from cProfile import label
import numpy as np
import matplotlib.pyplot as plt

plt.rcParams['font.sans-serif']=['SimHei']
plt.rcParams['axes.unicode_minus']= False

n = np.array([0,1,2,3,4,5,6])

u1 = np.array([0.011,0.183,0.217,0.288,0.358,0.343,0.277])
u2 = np.array([-0.015,-0.037,-0.059,-0.084,-0.099,-0.161,-0.231])
u3 = np.array([-0.002,-0.013,-0.068,-0.222,-0.276,-0.372,-0.463])

plt.plot(n,u1,'-o',label='第一组$U_g$')
plt.plot(n,u2,'-o',label='第二组$U_g$')
plt.plot(n,u3,'-o',label='第三组$U_g$')
plt.xlabel("放置砝码个数$n$")
plt.ylabel("电压表示数$U_g / mm$")
plt.title("实验原始数据")
plt.legend(loc=3)
plt.show()