import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import interp1d


filepath = "./2.csv"

x = np.loadtxt(filepath,dtype=np.float32,delimiter=",",usecols=(0),encoding='utf-8')
y = np.loadtxt(filepath,dtype=np.float32,delimiter=",",usecols=(1),encoding='utf-8')
# 执行三次样条插值
f = interp1d(x, y, kind='cubic')  # cubic表示三次样条插值

# 生成插值曲线的x和y值
interp_x = np.linspace(x.min(), x.max(), 100)
interp_y = f(interp_x)

# 绘制原始数据和插值曲线
plt.scatter(x, y, label='Data')  # 绘制散点图
plt.plot(interp_x, interp_y, color='r', label='Cubic Spline')  # 绘制插值曲线
plt.xlabel('Input Laser Power (mW)')
plt.ylabel('SHG Power (mW)')
plt.legend()
plt.show()