import torch
import torch.nn as nn
def dm01():
    # 1.手动创建样本的真实值---》就是上述公式中的y
    y_true = torch.tensor([[0,1,0],[1,0,0]], dtype=torch.float)

    # 手动创建样本的预测值
    y_pred = torch.tensor([[0.1,0.9,0.2],[0.8,0.1,0.1]], requires_grad=True,dtype=torch.float)

    # 创建损失函数
    criterion = nn.CrossEntropyLoss()

    # 计算损失
    loss = criterion(y_pred, y_true)
    print(loss)

if __name__ == '__main__':
    dm01()