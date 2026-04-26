# 特征工程的目的：
# 处理数据，用于提升模型的性能
# 归一化目的：
# 防止因为量纲问题，导致特征列的方差值较大，影响模型的效果
# 弊端：容易受到最小值和最大值的影响
# 1.导包
from sklearn.preprocessing import MinMaxScaler

# 2.准备数据集（归一化之前的原数据集）
x_train = [[90,2,10,40],[60,4,15,45],[75,3,13,46]]

# 3.创建归一化对象
transfer = MinMaxScaler(feature_range=(0,1))

# 4.对原数据集进行归一化操作。
x_train_new = transfer.fit_transform(x_train)

# 5.打印归一化后的数据
print(f'归一化后的数据是：\n{x_train_new}')