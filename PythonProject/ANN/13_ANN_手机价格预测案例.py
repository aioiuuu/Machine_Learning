import torch
from sklearn.preprocessing import StandardScaler
from torch.utils.data import TensorDataset
from torch.utils.data import DataLoader
import torch.nn as nn
import torch.optim as optim
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import time
from torchsummary import summary


def create_dataset():
    #todo:加载csv文件数据集
    data = pd.read_csv('../data/train.csv')
    #print(f'data: {data.shape}')  #(2000,21)
    #todo:获取x特征列和y标签列
    x,y=data.iloc[:,:-1],data.iloc[:,-1]
    # print(f'x: {x.shape}, y: {y.shape}')
    #todo:把特征列转成浮点型
    x = x.astype(np.float32)
    #todo:切分训练集和测试集
    x_train,x_test,y_train,y_test = train_test_split(x,y,test_size=0.2,random_state=3,stratify=y)
    #todo:数据标准化
    transfer = StandardScaler()
    x_train = transfer.fit_transform(x_train)
    x_test = transfer.transform(x_test)
    #todo:把数据集封装成张量数据集   数据-->张量Tensor--》数据集TensorDataset--》数据加载器DataLoader
    train_dataset = TensorDataset(torch.tensor(x_train), torch.tensor(y_train.values))
    test_dataset = TensorDataset(torch.tensor(x_test), torch.tensor(y_test.values))
    #todo:返回结果
    return train_dataset,test_dataset,x_train.shape[1],len(np.unique(y))

#todo:搭建神经网络
class PhonePriceModel(nn.Module):
    def __init__(self,input_dim,output_dim):
        #todo:初始化父类
        super().__init__()
        #todo:搭建神经网络
        #todo:输入层
        self.linear1 = nn.Linear(input_dim,128)
        self.linear2 = nn.Linear(128,256)
        self.linear3 = nn.Linear(256,512)
        self.linear4 = nn.Linear(512,128)
        self.output = nn.Linear(128,output_dim)
    def forward(self,x):
        #todo:隐藏层一：加权求和+激活函数（relu）
        x = torch.relu(self.linear1(x))
        #todo:隐藏层二：加权求和+激活函数（relu）
        x = torch.relu(self.linear2(x))
        #todo:隐藏层三：加权求和+激活函数（relu）
        x = torch.relu(self.linear3(x))
        #todo:隐藏层四：加权求和+激活函数（relu）
        x = torch.relu(self.linear4(x))
        #todo:输出层：加权求和
        x = self.output(x)
        return x

def train(train_dataset,input_dim,output_dim):
    #todo:创建数据加载器
    train_loader = DataLoader(train_dataset,batch_size=16,shuffle=True)
    #todo:创建神经网络模型
    model = PhonePriceModel(input_dim,output_dim)
    #todo:定义损失函数，使用交叉熵损失函数
    criterion = nn.CrossEntropyLoss()
    #todo:创建优化器对象
    optimizer = optim.Adam(model.parameters(),lr=0.0001)
    #todo:模型训练
    epochs = 100
    for epoch in range(epochs):
        #todo:定义变量，记录每次训练的损失值，训练批次数
        total_loss,batch_num = 0.0,0
        #todo:定义变量，表示训练开始的时间
        start = time.time()
        for x,y in train_loader:
            model.train()
            y_pred = model(x)
            loss = criterion(y_pred,y)
            #todo:梯度清0，反向传播，优化参数
            optimizer.zero_grad()
            loss.backward()
            optimizer.step()
            total_loss+=loss.item()
            batch_num+=1
            print(f'epoch{epoch+1},loss:{total_loss/batch_num:.4f},time:{time.time()-start:.2f}s')

    #todo:保存模型参数
    torch.save(model.state_dict(), '../data/phone.pth')


def evaluate(test_dataset,input_dim,output_dim):
    model = PhonePriceModel(input_dim,output_dim)
    model.load_state_dict(torch.load('../data/phone.pth'))
    #todo:创建测试集的数据集加载对象
    test_loader = DataLoader(test_dataset,batch_size=8,shuffle=False)
    correct = 0
    #todo:从数据加载器中，获得到每批次的数据
    for x,y in test_loader:
        model.eval()
        y_pred = model(x)
        y_pred = torch.argmax(y_pred,dim=1)
        # print(f'y_pred:{y_pred}')
        correct+=(y_pred==y).sum()
    #todo:计算准确率
    print(f'准确率：{correct/len(test_dataset):.4f}')

if __name__ == '__main__':
    #todo:创建数据集
    train_dataset,test_dataset,input_dim,output_dim = create_dataset()
    # model = PhonePriceModel(input_dim,output_dim)
    # summary(model,(16,input_dim))
    # train(train_dataset,input_dim,output_dim)
    evaluate(test_dataset,input_dim, output_dim)