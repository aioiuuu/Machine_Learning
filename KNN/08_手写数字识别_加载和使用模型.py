import matplotlib.pyplot as plt
import joblib

def test_model():
   # 1.加载图片
   x=plt.imread("../data/myplot.png")
   # 1.1绘制图片
   #plt.imshow(x,cmap='gray')
   #plt.show()

   # 2.加载模型
   # 把一张480*640*4的图片，拉直变成1行64000列的一维特征向量
   estimator=joblib.load('knn_手写数字识别model.pkl')

   # 3.模型预测
   print(x.reshape(1,-1).shape)

   # 4.训练模型应该用到归一化


if __name__ == '__main__':
    test_model()