import torch
import torch.nn as nn
#todo;计算inputs与target之差的绝对值
def test():
    #todo:设置真实值和预测值
    y_pred = torch.tensor([0,3])
    y_true = torch.tensor([0.6,0.4],dtype=torch.float,requires_grad=True)
    #todo:实例Sm00th损失对象
    loss = nn.SmoothL1Loss()
    #todo:计算损失
    l = loss(y_pred,y_true).detach().numpy()
    print(f'loss:{ l}')

if __name__ == '__main__':
    test()