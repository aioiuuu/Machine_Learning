# 演示线性回归API的使用
from sklearn.linear_model import LinearRegression


# 1.准备数据集
x_train = [[160],[166],[172],[174],[180]]
y_train = [56.3,60.6,65.1,68.5,75]
x_test = [[176]]

# 2.数据的预处理，这里不需要
# 3.特征工程（特征提取，特征预处理），这里不需要

# 4.模型训练
estimator = LinearRegression()
estimator.fit(x_train,y_train)

# 4.1查看斜率和截距
print("斜率：",estimator.coef_)
print("截距：",estimator.intercept_)

# 预测值
y_pre = estimator.predict(x_test)
print("预测结果：",y_pre)