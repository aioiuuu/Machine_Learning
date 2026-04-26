import numpy as np
import pandas as pd
from sklearn.linear_model import LogisticRegression
# 逻辑回归模型
from sklearn.preprocessing import StandardScaler
# 标准化处理
from sklearn.model_selection import train_test_split
# 划分数据集
from sklearn.metrics import accuracy_score
# 模型评估

# 1.加载数据集
data=pd.read_csv('breast-cancer-wisconsin-original.csv')
# data.info()

# 2.数据预处理
data.replace('?', np.nan, inplace=True)
data.dropna(inplace=True)
# data.info()

# 3.特征预处理
x = data.iloc[:, 1:-1]
# 683行，9列
y = data.iloc[:, -1]
# 683行，1列
# print(x.shape,y.shape)
x_train,x_test,y_train,y_test = train_test_split(x,y,test_size=0.2,random_state=23)
transfer = StandardScaler()
x_train = transfer.fit_transform(x_train)
x_test = transfer.transform(x_test)

# 4.模型训练
estimator = LogisticRegression()
estimator.fit(x_train,y_train)

# 5.模型预测
y_predict = estimator.predict(x_test)
print(f'预测值为：{y_predict}')

# 6.模型评估
print(f'准确率：{accuracy_score(y_test,y_predict)}')
print(f'准确率：{estimator.score(x_test,y_test)}')