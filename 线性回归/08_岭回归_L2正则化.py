import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import Ridge
from sklearn.metrics import mean_squared_error
from sklearn.preprocessing import StandardScaler  # 关键！

# 1. 准备数据
np.random.seed(666)
x = np.random.uniform(-3, 3.0, size=100)
y = (0.5 * x ** 2) + (x + 2) + np.random.normal(0, 1, size=100)

# 2. 构造高次特征 X ~ X^10
X = x.reshape(-1, 1)
X_poly = np.hstack([X**i for i in range(1, 11)])  # x~x10

# ==========================================
# 3. 【必须加】特征标准化（解决不收敛+效果差）
# ==========================================
scaler = StandardScaler()
X_poly_scaled = scaler.fit_transform(X_poly)

# 4. 岭回归（alpha 调大一点）
estimator = Ridge(alpha=1)  # 不要用 0.0005

# 5. 训练
estimator.fit(X_poly_scaled, y)
y_predict = estimator.predict(X_poly_scaled)

# 6. 评估
mse = mean_squared_error(y, y_predict)
print(f'均方误差为：{mse}')

# 7. 画图
plt.scatter(x, y)
plt.plot(np.sort(x), y_predict[np.argsort(x)], color='r', linewidth=2)
plt.title('Perfect Fit!')
plt.show()