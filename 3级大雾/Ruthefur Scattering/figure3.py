import numpy as np
import matplotlib.pyplot as plt
from scipy.linalg import lstsq

#avoid font problem
#plt.rcParams['font.sans-serif']=['SimHei']
#plt.rcParams['axes.unicode_minus']= False

#原始实验数据
t = np.array([10,13,16,19,22])
v = np.array([2.201,2.882,2.909,2.579,2.080])
nt = np.array([5.77E-5,1.642E-4,3.752E-4,7.421E-4,1.326E-3])
# 利用scipy中的linalg进行最小二乘法
A = np.vstack([t**0,t**1])
sol,r,rank,s= lstsq(A.T,v)

# 标注点
#plt.plot(0.1127,1.775,'x',color='r')

# 获得拟合数据
m = 1000
x = np.linspace(10,22,m)
y = sol[0] + sol[1] * x

print("g:")
print(sol[1])
print(sol[0])

plt.scatter(t,v,marker="x",color='r',label='Original Data')
plt.plot(t,v,color='skyblue')
plt.plot(x,y,label='Least Squares Fit')
plt.xlabel('$\\theta (^\circ)$')
plt.ylabel('K')
#显示图例
plt.legend(loc=1)
#标题
plt.title('$K \sim \\theta$ relationship')
# 说明
string1 = '$v=%0.3f+%0.3ft$' % (sol[0],sol[1])
string2 = '$g=%0.3f m/s$' % (sol[1]*2)
#plt.text(0.1,2.7,string1,fontsize=15,verticalalignment="top",horizontalalignment="left")
#plt.text(0.1,2.6,string2,fontsize=15,verticalalignment="top",horizontalalignment="left")
plt.savefig("./k.png")
plt.show()
'''
fig,ax = plt.subplots(figsize=(12,8))
ax.plot(x,y,'b',lw=2,label='Least square fit')
ax.set_xlabel("t(ms)",fontsize=18)
ax.set_ylabel("v(m/s)",fontsize=18)
plt.show()
'''