# 1.导包
from sklearn.preprocessing import StandardScaler
# 标准化对象
# 2.准备数据集（标准化之前的原数据集）
x_train = [[90,2,10,40],[60,4,15,45],[75,3,13,46]]

# 3.创建标准化对象
transfer = StandardScaler()

# 4.对原数据集进行标准化操作。
x_train_new = transfer.fit_transform(x_train)

# 5.打印标准化后的数据
print(f'归一化后的数据是：\n{x_train_new}')

# 6.打印数据集的均值和方差
print(f'数据集的均值为：{transfer.mean_}')
print(f'数据集的方差为：{transfer.var_}')
print(f'数据集的标准差为：{transfer.scale_}')