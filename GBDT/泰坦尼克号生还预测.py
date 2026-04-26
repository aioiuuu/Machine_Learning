import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import GradientBoostingClassifier
from sklearn.metrics import accuracy_score
from sklearn.model_selection import GridSearchCV



df = pd.read_csv('../data/titanic_train.csv')

# 数据的预处理
x = df[['Pclass','Age','Sex']]
y=df['Survived'].copy()

# 处理Age列的缺失值，用该列的均值填充
x['Age']=x['Age'].fillna(x['Age'].mean())

#热编码处理字符串类型
x = pd.get_dummies(x,columns=['Sex'])

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.3, random_state=23)

# 创建决策树模型
def model1():
    estimator = DecisionTreeClassifier()
    estimator.fit(x_train,y_train)
    y_predict = estimator.predict(x_test)
    print("预测结果为：",y_predict)
    print("精确度为：",accuracy_score(y_test,y_predict))

# 创建梯度提升模型
def model3():
    estimator3 = GradientBoostingClassifier()
    estimator3.fit(x_train,y_train)

    # 创建网格搜索对象
    param_grid = {
        'n_estimators':[50,60,70,80,90,100],
        'learning_rate':[0.1,0.2,0.3,0.4,0.5],
        'max_depth':[1,2,3,4,5]
    }
    estimator3 = GradientBoostingClassifier()
    estimator3 = GridSearchCV(estimator3,param_grid,cv=5)
    estimator3.fit(x_train,y_train)
    print("最佳参数：",estimator3.best_params_)
    print("最佳结果：",estimator3.best_score_)
    print('准确率',estimator3 .score(x_test,y_test))

if __name__ == '__main__':
    # model1()
    # model2()
    model3()