import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

# 定义1-高斯函数
def f(x,a,b,c,N):
    return N*x*a/(a*x**2+b*x+c)+1

# 原始数据
x = np.array([0.03,0.1,0.2,0.4,0.6,1,1.5,2,2.5,3.06,4.02])
y = np.array([220.5,397.71429,585.5,446.8,367.90816,259.15714,165.59615,15.01923,131.835,100.33667,87.667])

# 执行拟合
initial_guess = [1, 10, 1,y.mean()]  # 初始猜测值 [A, x0, sigma]
parameters, _ = curve_fit(f, x, y, p0=initial_guess)

# 生成拟合曲线的x和y值
fit_x = np.linspace(x.min(), x.max(), 100)
fit_y = f(fit_x, *parameters)

# 绘制原始数据和拟合曲线
plt.scatter(x, y, label='Data')  # 绘制散点图
plt.plot(fit_x, fit_y, color='r', label='Fit')  # 绘制拟合曲线
plt.xlabel('Pump Power (mW)')
plt.ylabel('CAR')
plt.legend()
plt.show()