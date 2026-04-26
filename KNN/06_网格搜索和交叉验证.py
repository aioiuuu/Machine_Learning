# 超参数：需要用户手动输入数据，不同的超参组合，可能会影响模型的预测结果
# 大白话解释：
# 网格搜索 + 交叉验证 ， 本质上指的是 GridSearchCV 这个API,它会帮我们寻找最优超参

# 导入工具包
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split,GridSearchCV
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score

# 1.加载鸢尾花数据集
iris_data = load_iris()

# 2.数据预处理，切分训练集和测试集
x_train, x_test, y_train, y_test = train_test_split(iris_data.data, iris_data.target,test_size=0.2,random_state=7)

# 3.特征工程 ==> 特征预处理 ==> 标准化
# 3.1创建标准化对象
transfer = StandardScaler()
x_train = transfer.fit_transform(x_train)
x_test = transfer.transform(x_test)

# 4.模型训练
estimator = KNeighborsClassifier()
# 4.2定义字典，记录可能出现的情况
param_dict = {'n_neighbors':[i for i in range(1,11)]}
# 4.3创建GriSearchCV对象 ==> 寻找最优超参
estimator = GridSearchCV(estimator, param_dict, cv=4)
# 4.4具体的模型训练动作
estimator.fit(x_train, y_train)
# 4.5打印最优的超参组合
print(f'最优评分：{estimator.best_score_}')
print(f'最优的超参组合：{estimator.best_params_}')
print(f'最优的估计器对象：{estimator.best_estimator_}')
print(f'具体的交叉验证结果：{estimator.cv_results_}')

# 5.模型评估
# 5.1获取最优超参的模型对象。
estimator = KNeighborsClassifier(n_neighbors=8)
# 5.2模型训练
estimator.fit(x_train, y_train)
# 5.3模型预测
y_pre = estimator.predict(x_test)
# 5.4模型评估
print(f'准确率：{accuracy_score(y_test, y_pre)}')