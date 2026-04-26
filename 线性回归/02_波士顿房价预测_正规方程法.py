from sklearn.preprocessing import StandardScaler
# 标准化
from sklearn.model_selection import train_test_split
# 划分数据集
from sklearn.linear_model import LinearRegression
# 线性回归
from sklearn.linear_model import SGDRegressor
# 随机梯度下降
from sklearn.metrics import mean_squared_error, root_mean_squared_error, mean_absolute_error
# 均方误差

import pandas as pd
import numpy as np

# 1.加载 波士顿的房价数据
data_url = "http://lib.stat.cmu.edu/datasets/boston"
raw_df = pd.read_csv(data_url, sep="\\s+", skiprows=22, header=None)
data = np.hstack([raw_df.values[::2, :], raw_df.values[1::2, :2]])
target = raw_df.values[1::2, 2]

# print(f'特征：{data.shape}')
# # 506行13列
# print(f'标签：{target.shape}')
# # 506行
# print(f'特征数据：{data[:5]}')
# print(f'标签数据：{target[:5]}')
# 线性回归：用线性公式来描述 特征 和 标签之间关系的

# 2.数据的预处理，切分训练集和测试集
x_train,x_test,y_train,y_test = train_test_split(data,target,test_size=0.2,random_state=23)

# 3.特征工程
# 3.1创建标准化对象
transfer = StandardScaler()
# 3.2对训练集进行标准化
x_train = transfer.fit_transform(x_train)
x_test = transfer.transform(x_test)

# 4.模型训练
# 4.1 创建线性回归 正规方程模型对象
estimator = LinearRegression(fit_intercept=True)
# 4.2模型训练
estimator.fit(x_train,y_train)
# 4.3打印模型计算出来的w(权重)和b(偏置)
print(f'权重：{estimator.coef_}')
print(f'偏置：{estimator.intercept_}')

# 5.模型预测
y_pre = estimator.predict(x_test)
print(f'预测结果为：{y_pre}')

# 6.模型评估
print(f'均方误差为：{mean_squared_error(y_test,y_pre)}')
print(f'均方根误差为：{root_mean_squared_error(y_test,y_pre)}')
print(f'平均绝对误差为：{mean_absolute_error(y_test,y_pre)}')