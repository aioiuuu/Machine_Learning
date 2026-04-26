# 导包
import pandas as pd
from sklearn.model_selection import train_test_split
# 决策树分类
from sklearn.tree import DecisionTreeClassifier
# 决策森林 分类
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import GridSearchCV

# 1.读取数据
df = pd.read_csv('../data/titanic_train.csv')

# 2.数据预处理
x = df[['Pclass', 'Age', 'Sex']].copy()
y = df['Survived']

# 2.2空值 处理
x['Age'] = x['Age'].fillna(x['Age'].mean())

# 2.3热编码处理
x = pd.get_dummies(x)

# 2.4 数据集划分
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=23)

def model1():
    # 3.决策树算法
    estimator1 = DecisionTreeClassifier()

    # 3.2模型训练
    estimator1.fit(x_train, y_train)

    # 4.模型预测
    y_predict = estimator1.predict(x_test)
    print('预测结果为：', y_predict)

    # 5.模型评估
    print('准确率：', estimator1.score(x_test, y_test))
    print('*'*50)

def model2():
    # 随机森林算法
    estimator2 = RandomForestClassifier()
    estimator2.fit(x_train, y_train)
    y_predict = estimator2.predict(x_test)
    print(f'预测值为{y_predict}')
    print(f'随机森林算法的准确率：{estimator2.score(x_test, y_test)}')

def model3():
    estimator3 = RandomForestClassifier()
    estimator3.fit(x_train, y_train)
    params = {'n_estimators': [30,50,60,70],'max_depth': [2,3,4,5,6,7,8,9,10]}
    gs_estimator = GridSearchCV(estimator3, param_grid=params, cv=3)
    gs_estimator.fit(x_train, y_train)
    y_pred3 = gs_estimator.predict(x_test)
    print(f'预测值为{y_pred3}')
    print(f'准确率：{gs_estimator.score(x_test, y_test)}')
    print(f'最佳参数：{gs_estimator.best_params_}')

if __name__ == '__main__':
    model1()
    # model2()
    # model3()