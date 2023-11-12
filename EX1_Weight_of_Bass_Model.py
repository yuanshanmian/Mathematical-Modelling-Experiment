import numpy as np
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt

# 提供的数据
length = np.array([36.8, 31.8, 43.8, 36.8, 32.1, 45.1, 35.9, 32.1]).reshape(-1, 1)
girth = np.array([24.8, 21.3, 27.9, 24.8, 21.6, 31.8, 22.9, 21.6]).reshape(-1, 1)
weight = np.array([765, 482, 1162, 737, 482, 1389, 652, 454])

# 构建多元线性回归模型
model = LinearRegression()
model.fit(np.hstack((length, girth)), weight)

# 输出模型参数
print("截距（Intercept）: ", model.intercept_)
print("身长系数（Coefficient for length）: ", model.coef_[0])
print("胸围系数（Coefficient for girth）: ", model.coef_[1])

pre_weight = model.intercept_ + model.coef_[0] * length + girth * model.coef_[1]

# 计算平均相对误差
MRE = np.mean(np.abs(weight - pre_weight) / weight)

print("平均相对误差（MRE）: {:.2f}%".format(MRE))
print("真实值(true weight)：   ", ", ".join(str(int(x)) for x in weight))
print("预测值(Predict weight)：", ", ".join(str(int(x[0])) for x in pre_weight))

plt.scatter(np.arange(8), weight, color='b', label='true')
plt.scatter(np.arange(8), pre_weight, color='r', label='predict')
plt.legend()
plt.show()
