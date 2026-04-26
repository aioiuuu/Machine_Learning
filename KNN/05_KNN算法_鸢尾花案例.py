# 通过KNN算法实现鸢尾花的分类操作

# 导包
from sklearn.datasets import load_iris
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score

# 1.定义函数,加载鸢尾花数据集，并查看数据集
def dm01_load_iris():
    iris_data = load_iris()
    # print(f'数据集：\n{iris_data}')
    # print(f'数据集的类型：\n{type(iris_data)}')
    print(f'数据集所有的键：{iris_data.keys()}')

# 2.定义函数，加载鸢尾花数据集，并查看数据集
def dm02_show_iris():
    # 1.加载数据集
    iris_data = load_iris()
    # 2.把鸢尾花数据集封装成DataFrame
    iris_df = pd.DataFrame(data=iris_data.data, columns=iris_data.feature_names)
    # 3.给df对象新增1列==>标签列
    iris_df['label'] = iris_data.target
    # 4.通过Season绘制散点图
    # 参1：数据集 参2：x轴 参3：y轴 参4：分组字段 参5：是否显示拟合曲线
    sns.lmplot(data=iris_df, x='sepal length (cm)', y='sepal width (cm)', hue='label', fit_reg=True)
    # 5.设置标题，显示
    plt.show()

# 3.定义函数，切分训练集和测试集
def dm03_split_train_test():
    # 1.加载数据集
    iris_data = load_iris()
    # 2.数据的预处理：从150个特征和标签中，按照8：2的比例，切分训练集和测试集
    # 参1：特征数据  参2：标签数据  参3：测试集的比例  参4：随机种子
    x_train, x_test, y_train, y_test = train_test_split(iris_data.data,iris_data.target,test_size=0.2,random_state=123)
    # 3.打印切割后的结果
    print(f'训练集的特征：{x_train},个数：{len(x_train)}')

# 4.定义函数，实现鸢尾花完整案例 ==> 加载数据，数据预处理，特征工程，模型训练，模型评估，模型预测
def dm04_iris_evaluate_test():
    # 1.加载数据集
    iris_data = load_iris()
    # 2.数据的预处理，这里是把150条拆分成训练集和测试集
    x_train, x_test, y_train,y_test = train_test_split(iris_data.data,iris_data.target,test_size=0.2,random_state=123)
    # 3.特征工程
    transfer = StandardScaler()
    x_train = transfer.fit_transform(x_train)
    x_test = transfer.transform(x_test)
    # 4.模型训练
    estimator = KNeighborsClassifier(n_neighbors=3)
    estimator.fit(x_train, y_train)
    # 5.模型预测
    # 场景1：对刚才切分的30条测试数据进行测试
    y_pre = estimator.predict(x_test)
    print(f'预测结果：{y_pre}')
    # 场景2：对新数据（150条之外的数据）进行测试
    my_data = [[7.8 , 2.1 , 3.9 , 1.6]]
    my_data = transfer.transform(my_data)
    y_pre_new = estimator.predict(my_data)
    print(f'预测结果为：{y_pre_new}')
    # 查看上述数据集，每种分类的预测概率
    y_pre_proba = estimator.predict_proba(my_data)
    print(f'各分类预测概率为：{y_pre_proba}')

    # 6.模型评估
    # 方式1：直接评分，基于：训练集的特征 和 训练集的标签
    print(f'正确率：{estimator.score(x_train, y_train)}')
    # 方式2：基于测试集标签 和 预测结果 进行评分
    print(f'正确率：{accuracy_score(y_test, y_pre)}')
    # 测试

if __name__ == '__main__':
    dm04_iris_evaluate_test()