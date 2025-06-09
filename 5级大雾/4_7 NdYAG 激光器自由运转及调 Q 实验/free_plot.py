import numpy as np
import matplotlib.pyplot as plt

# 创建示例数据
x = np.array([600.0,650.0,700.0,750.0,800.0,850.0])
y = np.array([14.8, 23.42, 33.56, 44.82, 55.52, 65.32])
errors = np.array([0.276, 0.412, 0.432, 0.673, 0.688,0.624])

x = 10**(-4) * x**2
y = y/0.08*10**(-3)
errors = errors/0.08*10**(-3)

# 绘制误差条图形
plt.errorbar(x, y,yerr=errors, fmt='-..',capsize=5)

# 添加标题和标签
plt.title("Efficiency curve of free oscillating laser")
plt.xlabel("$E_{pump} \ (J)$")
plt.ylabel("$E_{laser} \ (J)$")

# 显示图形
plt.show()

print(y)