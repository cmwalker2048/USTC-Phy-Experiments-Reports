import numpy as np
import matplotlib.pyplot as plt
from scipy.linalg import lstsq

#avoid font problem
#plt.rcParams['font.sans-serif']=['SimHei']
#plt.rcParams['axes.unicode_minus']= False

#原始实验数据
t = np.array([1/9,1/16,1/25,1/36])
v = np.array([1/(657.14E-9),1/(486.35E-9),1/(433.73E-9),1/(409.77E-9)])
# 利用scipy中的linalg进行最小二乘法
A = np.vstack([t**0,t**1])
sol,r,rank,s= lstsq(A.T,v)

# 标注点
#plt.plot(0.1127,1.775,'x',color='r')

# 获得拟合数据
m = 1000
x = np.linspace(0,1/9,m)
y = sol[0] + sol[1] * x

print("g:")
print(sol[1])
print(sol[0])

plt.scatter(t,v,marker="x",color='r',label='Original Data')
plt.plot(x,y,label='Least Squares Fit')
plt.xlabel('$\lambda_{measure}$')
plt.ylabel('$\lambda_0$')
#显示图例
plt.legend(loc=1)
#标题
plt.title('$\lambda_{measure}$~$\lambda_0$ Least Squares Fitting')
# 说明
string1 = '$v=%0.3f+%0.3ft$' % (sol[0],sol[1])
string2 = '$g=%0.3f m/s$' % (sol[1]*2)
#plt.text(0.1,2.7,string1,fontsize=15,verticalalignment="top",horizontalalignment="left")
#plt.text(0.1,2.6,string2,fontsize=15,verticalalignment="top",horizontalalignment="left")
#plt.savefig("./temp.png")
plt.show()
'''
fig,ax = plt.subplots(figsize=(12,8))
ax.plot(x,y,'b',lw=2,label='Least square fit')
ax.set_xlabel("t(ms)",fontsize=18)
ax.set_ylabel("v(m/s)",fontsize=18)
plt.show()
'''