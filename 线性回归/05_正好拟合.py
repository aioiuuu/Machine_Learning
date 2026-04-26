import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error

# 1.准备数据x,y(增加上噪声)
np.random.seed(666)
x = np.random.uniform(-3, 3.0, size=100)
y = (0.5 * x ** 2) + (x +2) + np.random.normal(0, 1, size=100)

# 2.实例化线性回归模型
estimator = LinearRegression()

# 3.训练模型
X=x.reshape(-1,1)
X2 = np.hstack([X,X**2])
estimator.fit(X2,y)

# 4.模型预测
y_predict = estimator.predict(X2)

# 5.计算均方误差
mse = mean_squared_error(y,y_predict)
print(f'均方误差为：{mse}')

# 6.画图
plt.scatter(x,y)
plt.plot(np.sort(x),y_predict[np.argsort(x)],color='r')
plt.show()