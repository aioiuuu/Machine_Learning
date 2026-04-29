import torch
import torch.nn as nn
def dm01():
    #todo:创建最大池化层
    inputs = torch.tensor([
        [
            [0,1,2],
            [3,4,5],
            [6,7,8]
        ]
    ])
    pool1 = nn.MaxPool2d(2,1,0)
    output = pool1(inputs)
    print(f'output:{output},shape:{output.shape}')

    #todo:创建平均池化层
    pool2 = nn.AvgPool2d(2,1,0)
    output = pool2(inputs)
    print(f'output:{output},shape:{output.shape}')

def dm02():
    #todo:创建最大池化层
    inputs = torch.tensor([
        [
            [0,1,2],
            [3,4,5],
            [6,7,8]
        ]
        ,
        [
            [0,1,2],
            [3,4,5],
            [6,7,8]
        ]
        ,
        [
            [0,1,2],
            [3,4,5],
            [6,7,8]
        ]
    ])
    pool1 = nn.MaxPool2d(2,1,0)
    output = pool1(inputs)
    print(f'output:{output},shape:{output.shape}')

    #todo:创建平均池化层
    pool2 = nn.AvgPool2d(2,1,0)
    output = pool2(inputs)
    print(f'output:{output},shape:{output.shape}')

if __name__ == '__main__':
    # dm01()
    dm02()