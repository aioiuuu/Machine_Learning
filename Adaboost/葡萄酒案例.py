from sklearn.datasets import load_wine
import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import AdaBoostClassifier
# 集成学习：集成多个弱学习器的结果
from sklearn.metrics import accuracy_score


# 加载葡萄酒数据集
wine = load_wine()

# 转换成 DataFrame
df_wine = pd.DataFrame(wine.data, columns=wine.feature_names)

# ✅ 增加一列：葡萄酒类别（就是你图片里的 class label）
df_wine['class'] = wine.target

# 查看数据信息
# df_wine.info()

# 数据预处理
df_wine = df_wine[df_wine['class']!=1]
# 过滤掉类别为1的样本
# 留下类别为0和2的样本

x=df_wine[['alcohol','hue']]
y=df_wine['class']

le = LabelEncoder()
y = le.fit_transform(y)
print(y)

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.3, random_state=0, stratify=y)
estimator1 = DecisionTreeClassifier(max_depth=3)
estimator1.fit(x_train, y_train)
y_pre = estimator1.predict(x_test)
print(f'预测结果：{y_pre }')
print(f'准确率：{accuracy_score(y_test, y_pre)}')

estimator2 = AdaBoostClassifier(estimator=estimator1, n_estimators=500,learning_rate=0.1)
estimator2.fit(x_train, y_train)
y_pre = estimator2.predict(x_test)
print(f'预测结果：{y_pre }')
print(f'准确率：{accuracy_score(y_test, y_pre)}')