# 1.计算测试集和每个训练的样本之间的距离
# 2.基于距离进行升序排列
# 3.找到最近的k个样本
# 4.基于k个样本的标签值，计算平均值
# 5.将上述计算出来的平均值，作为最终的预测结果

# 1.导包
from sklearn.neighbors import KNeighborsRegressor

# 2.准备数据集（测试集 和 训练集）
x_train = [[0,0,1],[1,1,0],[3,10,10],[4,11,12]]
y_train = [0.1,0.2,0.3,0.4]
x_test = [[3,11,10]]

# 3.创建（KNN回归模型）模型对象
estimator = KNeighborsRegressor(n_neighbors=2)

# 4.模型训练
estimator.fit(x_train,y_train)

# 5.模型预测
y_pre = estimator.predict(x_test)

#6.打印预测结果
print(f'预测结果为：{y_pre}')
# 总结：
#     K值过小，容易受到异常值的影响，且会导致模型学到大量的藏的特征，导致出现：过拟合
#     K值过大，导致模型变得简单，容易发生：欠拟合