import torch
import torch.nn as nn
def dm01():
    #todo:创建隐藏层输出结果
    t1 = torch.randint(0,10,size=(1,4)).float()
    print(f't1:{t1}')

    #todo:进行 线性变换 和 激活函数计算
    linear1 = nn.Linear(4,5)

    #todo:进行 线性变换
    l1 = linear1(t1)

    #todo:进行 激活函数计算
    output = torch.relu(l1)
    print(f'output:{output}')

    #todo；对激活值进行随机失活处理---》随机失活概率为0.5
    dropout = nn.Dropout(p=0.5)
    output = dropout(output)
    print(f'output:{output}')

if __name__ == '__main__':
    dm01()