import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import interp1d

# 原始数据
x = np.array([0.03,0.1,0.2,0.4,0.6,1,1.5,2,2.5,3.06,4.02])
y = np.array([220.5,397.71429,585.5,446.8,367.90816,259.15714,165.59615,15.01923,131.835,100.33667,87.667])

x1 = np.array([0.03,0.1,0.2,0.4,0.6,1,1.5,2.5,3.06,4.02])
y1 = np.array([220.5,397.71429,585.5,446.8,367.90816,259.15714,165.59615,131.835,100.33667,87.667])

# 执行三次样条插值
f = interp1d(x1, y1, kind='cubic')  # cubic表示三次样条插值

# 生成插值曲线的x和y值
interp_x = np.linspace(x1.min(), x1.max(), 100)
interp_y = f(interp_x)

# 绘制原始数据和插值曲线
plt.scatter(x, y, label='Data')  # 绘制散点图
plt.plot(interp_x, interp_y, color='r', label='Cubic Spline')  # 绘制插值曲线
plt.xlabel('Pump Power (mW)')
plt.ylabel('CAR')
plt.legend()
plt.show()