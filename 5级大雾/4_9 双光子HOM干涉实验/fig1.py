import numpy as np
import matplotlib.pyplot as plt

# 原始数据
x = np.array([0.03,0.1,0.2,0.4])
y1 = np.array([19000,37000,66000,128000])
y2 = np.array([15000,35000,66000,123000])
y3 = np.array([878,2777,10521,22290])

# 执行线性拟合
coefficients = np.polyfit(x, y3, 1)  # 1表示线性拟合，2表示二次拟合，以此类推
slope = coefficients[0]  # 斜率
intercept = coefficients[1]  # 截距

# 生成拟合直线的x和y值
fit_x = np.linspace(x.min(), x.max(), 100)
fit_y = slope * fit_x + intercept

# 绘制原始数据和拟合直线
plt.scatter(x, y3, label='Data')  # 绘制散点图
plt.plot(fit_x, fit_y, color='r', label='Linear Fit')  # 绘制拟合直线
plt.xlabel('Pump Power (mW)')
plt.ylabel('Coincidences Count(s)')
plt.legend()
plt.show()

x = np.array([0.03,0.1,0.2,0.4,0.6,1,1.5,2,2.5,3.06,4.02])
y = np.array([220.5,397.71429,585.5,446.8,367.90816,259.15714,165.59615,15.01923,131.835,100.33667,87.667])

x = np.array([16,16.1,16.2,16.3,16.4,16.5,16.6,16.7,16.75,16.76,16.77,16.78,16.79,16.8,16.81,16.82,16.83,16.84,16.85,16.86,16.87,16.88,16.89,16.9,16.95,17,17.1,17.2,17.3,17.4,17.5])
y = np.array([84224,85275,84477,84635,84073,82151,79213,52606,45010,44086,42755,43079,42574,40937,41096,41343,40319,41520,39465,41783,38952,41577,42050,42020,51766,70114,72595,72407,74381,70928,67575])