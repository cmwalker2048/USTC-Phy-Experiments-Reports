# 2022/3/17
# 重力加速度的测量
# 光电门测重力加速度

import numpy as np
import matplotlib.pyplot as plt
from scipy.linalg import lstsq

#avoid font problem
plt.rcParams['font.sans-serif']=['SimHei']
plt.rcParams['axes.unicode_minus']= False

#原始实验数据
t = np.array([28.449,28.649,28.825,29.02,29.232])
v = np.array([-0.015,-0.037,-0.059,-0.084,-0.099])
# 利用scipy中的linalg进行最小二乘法
A = np.vstack([t**0,t**1])
sol,r,rank,s= lstsq(A.T,v)

# 标注点
#plt.plot(0.1127,1.775,'x',color='r')

# 获得拟合数据
m = 1000
x = np.linspace(28.449,29.232,m)
y = sol[0] + sol[1] * x

print("g:")
print(sol[1]*2)
print(sol[0])

plt.scatter(t,v,marker="x",color='r',label='原始数据')
plt.plot(x,y,label='拟合曲线')
plt.xlabel('焊点的相对位置$l / mm$')
plt.ylabel('电压表的示数$U_g / mv$')
#显示图例
plt.legend(loc=1)
#标题
plt.title('电压表的示数$U_g$与焊点的相对位置$l$关系图')
# 说明
string1 = '$l=%0.3f+%0.3fn$' % (sol[0],sol[1])
string2 = '$g=%0.3f m/s$' % (sol[1]*2)
plt.text(28.825,-0.025,string1,fontsize=15,verticalalignment="top",horizontalalignment="left")
plt.text(0.1,2.6,string2,fontsize=15,verticalalignment="top",horizontalalignment="left")
plt.show()
plt.savefig('fig2.png')
'''
fig,ax = plt.subplots(figsize=(12,8))
ax.plot(x,y,'b',lw=2,label='Least square fit')
ax.set_xlabel("t(ms)",fontsize=18)
ax.set_ylabel("v(m/s)",fontsize=18)
plt.show()
'''