import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

# 定义1-高斯函数
def subtracted_gaussian_function(x, A, T,a,B):
    return A * np.exp(-(x/T) ** a) + B

filepath = "./1.csv"

x = np.loadtxt(filepath,dtype=np.float32,delimiter=",",usecols=(0),encoding='utf-8')
y = np.loadtxt(filepath,dtype=np.float32,delimiter=",",usecols=(1),encoding='utf-8')

# 执行拟合
initial_guess = [np.mean(y), x.mean(), 1,y.min()]  # 初始猜测值 [A, x0, sigma]
parameters, _ = curve_fit(subtracted_gaussian_function, x, y, p0=initial_guess)

# 生成拟合曲线的x和y值
fit_x = np.linspace(x.min(), x.max(), 100)
fit_y = subtracted_gaussian_function(fit_x, *parameters)

# 绘制原始数据和拟合曲线
plt.scatter(x, y, label='Data')  # 绘制散点图
plt.plot(fit_x, fit_y, color='r', label='Fit')  # 绘制拟合曲线
plt.xlabel('$t \ (ns)$')
plt.legend()
plt.show()

print("A: ",parameters[0])
print("T: ",parameters[1])
print("a: ",parameters[2])
print("B: ",parameters[3])