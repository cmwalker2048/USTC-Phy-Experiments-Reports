import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

# 定义1-高斯函数
def subtracted_gaussian_function(x, A, x0, sigma,B):
    return B - B*A * np.exp(-(x - x0) ** 2 / (2 * sigma ** 2))

# 原始数据
x = np.array([16,16.1,16.2,16.3,16.4,16.5,16.6,16.7,16.75,16.76,16.77,16.78,16.79,16.8,16.81,16.82,16.83,16.84,16.85,16.86,16.87,16.88,16.89,16.9,16.95,17,17.1,17.2,17.3,17.4,17.5])
y = np.array([84224,85275,84477,84635,84073,82151,79213,52606,45010,44086,42755,43079,42574,40937,41096,41343,40319,41520,39465,41783,38952,41577,42050,42020,51766,70114,72595,72407,74381,70928,67575])

x = x * 10/3
x = x - x.mean()

# 执行拟合
initial_guess = [0.5, np.mean(x), 1,np.mean(y)]  # 初始猜测值 [A, x0, sigma]
parameters, _ = curve_fit(subtracted_gaussian_function, x, y, p0=initial_guess)

# 生成拟合曲线的x和y值
fit_x = np.linspace(x.min(), x.max(), 100)
fit_y = subtracted_gaussian_function(fit_x, *parameters)

# 绘制原始数据和拟合曲线
plt.scatter(x, y, label='Data')  # 绘制散点图
plt.plot(fit_x, fit_y, color='r', label='Fit')  # 绘制拟合曲线
plt.xlabel('$\Delta T(ps)$')
plt.ylabel('Coincidences Count(s)')
plt.legend()
plt.show()