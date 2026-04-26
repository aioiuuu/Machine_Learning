# KNN算法介绍：
# 基于欧氏距离计算 测试集和每个训练集之间的距离，然后根据距离升序排列，
# 找到最近的k个样本，
# 基于k个样本投票，票数最多的就作为预测结果————分类问题
# 基于k个样本计算平均值，作为最终预测结果————回归问题

# 1.导包
from sklearn.neighbors import KNeighborsClassifier

# 2.准备数据集(测试集 和 训练集)
# train:训练集
# test:测试集
# neighbors:最近邻的邻居数
x_train = [[0],[1],[2],[3]]
y_train = [0,0,1,1]
x_test = [[5]]
# 二维数组

#3.创建（KNN分类模型）模型对象

estimator = KNeighborsClassifier(n_neighbors=3)

# 4.传入：训练集的特征数据，训练集的标签数据
estimator.fit(x_train,y_train)

# 5.模型预测
# 传入测试集的标签数据，获取到预测结果
y_pre = estimator.predict(x_test)

# 6.打印预测结果
print(f'预测结果为：{y_pre}')