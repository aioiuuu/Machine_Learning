from sklearn.datasets import load_digits
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score
import joblib
import matplotlib.pyplot as plt

def train_model():
    # 1. 加载数据集
    df=load_digits()

    # 2.数据的预处理
    # 2.1拆分特征列
    x,y=df.data,df.target
    # 2.2打印特征和标签的维度
    print(x.shape)
    print(y.shape)
    # 2.3对特征列进行归一化
    # x=x/255.0
    # 2.4 拆分训练集和测试集
    x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.2,random_state=123,stratify=y)

    # 3.模型训练
    estimator=KNeighborsClassifier(n_neighbors=5)
    estimator.fit(x_train,y_train)

    # 4.模型评估
    print("模型的准确率为：",estimator.score(x_test,y_test))
    print("模型的准确率为：",accuracy_score(y_test,estimator.predict(x_test)))

    # 5.保存模型
    # joblib.dump(estimator,'knn_手写数字识别model.pkl')
    # print("模型保存成功！")

    # 6.显示一张图片
    # plt.imshow(x[0].reshape(8,8),cmap=plt.cm.gray)
    # plt.show()

    # 7.使用模型
def test_model():
    x=plt.imread("../data/sklearn.png")

    # 转换动作
    x=x.reshape(1,-1)
    estimator = joblib.load('knn_手写数字识别model.pkl')
    # 模型预测
    y_pre = estimator.predict(x)
    print("预测结果为：",y_pre)

if __name__ == '__main__':
    train_model()
    test_model()