import torch
import torch.nn as nn
def dm01():
    #todo:设置真实值
    y_true = torch.tensor([0,1,0],dtype=torch.float)

    #todo:设置预测值
    y_pred = torch.tensor([0.1,0.8,0.05],dtype=torch.float)

    #todo:创建一个二分类交叉熵损失函数
    criterion = nn.BCELoss()
    loss = criterion(y_pred,y_true)
    print(f'loss={loss}')

if __name__ == '__main__':
    dm01()