import torch
import torch.nn as nn

#1.定义函数，处理 二维数据
def dm01():
    #todo:创建图像样本数据集
    input_2d = torch.randn(size=(1,2,3,4))
    print(f'input_2d:{input_2d}')

    #todo:2.创建批量归一化层
    bn2d = nn.BatchNorm2d(num_features=2, eps=1e-05, momentum=0.1, affine=True, track_running_stats=True)

    #todo:对数据做批量归一化处理
    output_2d = bn2d(input_2d)
    print(f'output_2d:{output_2d}')
def dm02():
    #2行2列
    input_1d = torch.randn(size=(2,2))
    print(f'input_1d:{input_1d}')

    #创建线性层
    linear1 = nn.Linear(2,4)

    #对数据进行线性变换
    l1 = linear1(input_1d)
    print(f'l1:{l1}')

    #创建批量归一化层
    bn1d = nn.BatchNorm1d(num_features =4)
    output_1d = bn1d(l1)
    print(f'output_1d:{output_1d}')



if __name__ == '__main__':
    # dm01()
    dm02()