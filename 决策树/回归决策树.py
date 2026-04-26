# 导包
import pandas as pd
import numpy as np
from sklearn.tree import DecisionTreeRegressor
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt

# 1.准备数据集
x=np.array(list(range(1,11))).reshape(-1,1)
y=np.array([5.56,5.70,5.91,6.40,6.80,7.05,8.90,8.70,9.00,9.05])

# 2.创建模型
model1=DecisionTreeRegressor(max_depth=1)
model2=DecisionTreeRegressor(max_depth=3)
model3=LinearRegression()
model1.fit(x,y)
model2.fit(x,y)
model3.fit(x,y)

# 3.模型预测
x_test = np.arange(0.0,10.0,0.01).reshape(-1,1)
y_pre1=model1.predict(x_test)
y_pre2=model2.predict(x_test)
y_pre3=model3.predict(x_test)

# 4. 绘制图像
plt.figure(figsize=(10,6),dpi=100)
plt.plot(x_test,y_pre1,label='max_depth=1')
plt.plot(x_test,y_pre2,label='max_depth=3')
plt.plot(x_test,y_pre3,label='LinearRegression')
plt.scatter(x,y)
plt.xlabel('data')
plt.ylabel('target')
plt.title('DecisionTreeRegressor')
plt.legend()
plt.show()

