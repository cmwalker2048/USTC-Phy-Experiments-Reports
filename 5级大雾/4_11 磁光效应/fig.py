import numpy as np
import matplotlib.pyplot as plt

filepath = "./1.csv"

x = np.loadtxt(filepath,dtype=np.float32,delimiter=",",usecols=(0),encoding='utf-8')
y = np.loadtxt(filepath,dtype=np.float32,delimiter=",",usecols=(1),encoding='utf-8')
# 绘制散点图
plt.scatter(x, y, color='skyblue', marker='.')

# 设置图形标题和坐标轴标签
plt.title('Hysteresis Loop')
plt.xlabel('$I(A)$')
plt.ylabel('$U(V)$')

# 显示图形
plt.show()