import torch
import torch.nn as nn
from torchsummary import summary
class ModelDemo(nn.Module):
    #todo:1,在init魔法方法中，完成初始化：父类成员，以及神经网络搭建
    def __init__(self):
        #初始化父类成员。
        super().__init__()
        #1.2搭建神经网络--》隐藏层加输出层
        #隐藏层1：输入特征数：3   输出特征数：3
        self.linear1 = nn.Linear(3,3)
        #隐藏层2：输入特征数：2，  输出特征数：2
        self.linear2 = nn.Linear(3,2)
        #输出层：输入特征数：2，  输出特征数：2
        self.output = nn.Linear(2,2)

        #1.3对隐藏层进行参数初始化
        nn.init.xavier_normal_(self.linear1.weight)
        nn.init.zeros_(self.linear1.bias)
        nn.init.kaiming_normal_(self.linear2.weight)
        nn.init.zeros_(self.linear2.bias)
    #todo: 1.2前向传播：输出层--》隐藏层--》输出层
    def forward(self,x):
        # x = self.linear1(x)
        # x = torch.sigmoid(x)
        x = torch.sigmoid(self.linear1(x))
        x = torch.relu(self.linear2(x))
        #1.3第3层，输出层计算：加权求和+激活函数（softmax）
        x = torch.softmax(self.output(x),dim=-1)
        return x

def train():
    # todo:创建模型对象
    my_model = ModelDemo()
    # print(f'my_model: {my_model}')
    #2。todo:创建数据样本，随机生成‘
    data = torch.randn(size=(5,3))
    print(f'data: {data}')
    print(f'data.shape:{data.shape}')                   # torch.Size([5, 3])
    print(f'data.requires_grad:{data.requires_grad}')   # False
    #3.todo调用神经网络模型--》进行模型训练
    output = my_model(data)
    print(f'output: {output}')
    print(f'output.shape:{output.shape}')
    print(f'output.requires_grad:{output.requires_grad}')
    #4.todo:计算 和 查看模型参数。
    print('*************计算模型参数************')
    #参1：模型参数
    summary(my_model, input_size=(5, 3))

    print('*************查看模型参数************')
    for name,param in my_model.named_parameters():
        print(f'参数名称：{name},参数形状：{param.shape}')
        print(f'参数值：{param}\n')


#todo:3.测试：
if __name__ == '__main__':
    train()

