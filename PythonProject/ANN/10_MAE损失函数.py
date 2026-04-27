import torch
import torch.nn as nn
#todo;计算inputs与target之差的绝对值
def test():
    #todo:设置真实值和预测值
    y_pred = torch.tensor([1,1,1.9],requires_grad=True,dtype=torch.float)
    y_true = torch.tensor([2,2,2],dtype=torch.float,requires_grad=True)
    #todo:实例MAE损失对象
    loss = nn.L1Loss()
    #todo:计算损失
    l = loss(y_pred,y_true).detach().numpy()
    print(f'loss:{ l}')

if __name__ == '__main__':
    test()
