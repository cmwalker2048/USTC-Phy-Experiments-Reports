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
t = np.array([-90,-84,-78,-72,-66,-60,-54,-48,-42,-36,-30,-24,-18,-12,-6,0])
v = np.array([0,13,44,91,154,226,308,395,483,568,648,718,775,818,844,853])

t1 = np.array([0,6,12,18,24,30,36,42,48,54,60,66,72,78,84,90])
v1 = np.array([853,844,817,772,713,642,561,475,385,297,216,146,85,39,10,0])

t_2 = np.cos(t*np.pi/180)**2
v_2 = v/853

t1_2 = np.cos(t1*np.pi/180)**2
v1_2 = v1/853

# 利用scipy中的linalg进行最小二乘法
A = np.vstack([t1_2**0,t1_2**1])
sol,r,rank,s= lstsq(A.T,v1_2)

# 标注点
#plt.plot(0.1127,1.775,'x',color='r')

# 获得拟合数据
m = 100
x = np.linspace(0,1,m)
y = sol[0] + sol[1] * x

print("g:")
print(sol[1]*2)
print(sol[0])

plt.scatter(t1_2,v1_2,marker="x",color='r',label='原始数据')
plt.plot(x,y,label='拟合曲线')
plt.xlabel('$\cos^2{\\theta}$')
plt.ylabel('$I/I_0$')
#显示图例
plt.legend(loc=4)
#标题
plt.title('$I/I_0$-$\cos^2{\\theta}$关系图$\\theta \in \left[0^\circ,90^\circ\\right]$')
# 说明
string1 = '$(I/I_0)=%0.3f+%0.3f\cos^2{\\theta}$' % (sol[0],sol[1])
string2 = '$g=%0.3f m/s$' % (sol[1]*2)
plt.text(0.1,1,string1,fontsize=15,verticalalignment="top",horizontalalignment="left")
plt.text(0.1,2.6,string2,fontsize=15,verticalalignment="top",horizontalalignment="left")
#plt.savefig(r'D:\\Documents\\USTC\\Freshman\\second\\大雾基础实验A\\exp\\重力加速度的测量\\pic.png')
plt.show()
'''
fig,ax = plt.subplots(figsize=(12,8))
ax.plot(x,y,'b',lw=2,label='Least square fit')
ax.set_xlabel("t(ms)",fontsize=18)
ax.set_ylabel("v(m/s)",fontsize=18)
plt.show()
'''