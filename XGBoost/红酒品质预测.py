import joblib
import numpy as np
import pandas as pd
from collections import Counter
import xgboost as xgb                                    #极限梯度提升树对象
from sklearn.model_selection import train_test_split, GridSearchCV  # 训练集和测试集的划分
from sklearn.metrics import classification_report        #模型分类评估报告
from sklearn.model_selection import StratifiedKFold      #类似于K折交叉验证
from sklearn.metrics import confusion_matrix, accuracy_score
from sklearn.utils import class_weight


def model1():
    df = pd.read_csv('../data/winequality-white.csv',sep=';')
    # df.info()
    x = df.iloc[:,:-1]
    y = df.iloc[:,-1]-3
    # print(x[:5])
    # print(y[:5])
    print(f'查看标签的分布情况：{Counter(y)}')
    x_train,x_test,y_train,y_test = train_test_split(x,y,test_size=0.3,random_state=23,stratify=y)
    pd.concat([x_train,y_train],axis=1).to_csv('../data/wine_train.csv',index=False)
    pd.concat([x_test,y_test],axis=1).to_csv('../data/wine_test.csv',index=False)

def model2():
    # 加载数据
    train = pd.read_csv('../data/wine_train.csv')
    test = pd.read_csv('../data/wine_test.csv')
    # 划分训练集和测试集
    x_test=test.iloc[:,:-1]
    y_test=test.iloc[:,-1]
    x_train=train.iloc[:,:-1]
    y_train=train.iloc[:,-1]

    estimator = xgb.XGBClassifier(n_estimators=100,
                                  learning_rate=0.1,
                                  max_depth=5,
                                  random_state=23,
                                  objective='multi:softmax',
                                  )

    class_weight.compute_sample_weight('balanced',y_train)

    estimator.fit(x_train,y_train)
    y_predict = estimator.predict(x_test)
    print('准确率：',accuracy_score(y_test,y_predict))
    joblib.dump(estimator,'../data/红酒品质分类.pkl')

def model3():
    # 加载数据
    train = pd.read_csv('../data/wine_train.csv')
    test = pd.read_csv('../data/wine_test.csv')
    # 划分训练集和测试集
    x_test = test.iloc[:, :-1]
    y_test = test.iloc[:, -1]
    x_train = train.iloc[:, :-1]
    y_train = train.iloc[:, -1]
    estimator = joblib.load('../data/红酒品质分类.pkl')

    #创建网格搜索对象+交叉验证（结合分层采样数据），找模型最优参数组合
    param_dict  = {'max_depth':[3,5,7,9],'n_estimators':[30,50,100,150],'learning_rate':[0.2,0.3,1,1.3]}
    skf = StratifiedKFold(n_splits=3,shuffle=True,random_state=23)
    gs_estimator = GridSearchCV(estimator,param_dict,cv=skf)
    # 模型训练
    gs_estimator.fit(x_train,y_train)
    # 模型预测
    y_pre = gs_estimator.predict(x_test)
    print(f'预测值为：{y_pre}')
    #打印模型评估结果

    # print(f'最优估计器：{gs_estimator.best_estimator_}')
    # print(f'最优评分：{gs_estimator.best_score_}')
    # 准确率：
    print(f'准确率：{accuracy_score(y_test,y_pre)}')
if __name__ == '__main__':
    # model1()
    # model2()
    model3()