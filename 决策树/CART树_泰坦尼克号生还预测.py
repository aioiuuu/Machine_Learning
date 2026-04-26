import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import classification_report
import matplotlib.pyplot as plt
from sklearn.tree import plot_tree

# 1.加载数据
data = pd.read_csv("../data/titanic_train.csv")
data.info()

# 2.数据的预处理
x = data[["Pclass", "Age", "Sex"]]
y=data["Survived"]

x = x.copy()
x['Age'] = x['Age'].fillna(x['Age'].mean())
# 通过浅拷贝来处理数据，将Age列的缺失值填充为该列的均值
x.info()

x = pd.get_dummies(x,columns=["Sex"])
# 划分训练集和测试集
x_train,x_test,y_train,y_test = train_test_split(x,y,test_size=0.2,random_state=23)

# 3.创建模型对象
estimator = DecisionTreeClassifier(max_depth=10)
estimator.fit(x_train,y_train)

# 4.模型预测
y_predict = estimator.predict(x_test)

# 5.模型评估
print(classification_report(y_test,y_predict))

# 6.模型可视化
plt.figure(figsize=(30,20))
plot_tree(estimator,filled=True,max_depth=5)
plt.show()