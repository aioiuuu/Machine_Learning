import torch

#定义x，表示：特征（输入数据），假设：2行5列，全1矩阵
x = torch.ones(2,5)
print(f'x:{x}')

#定义y,表示：标签（真实值），假设：2行3列，全0矩阵
y = torch.zeros(2,3)
print(f'y:{y}')

#初始化（可自动微分的）权重 和 偏执
w = torch.randn(5,3,requires_grad=True)
print(f'w:{w}')

b = torch.randn(3,requires_grad=True)
print(f'b:{b}')

#前向传播（正向传播），计算出 预测值（z）
z = x @ w + b
print(f'z:{z}')

#定义损失函数
criterion = torch.nn.MSELoss()
loss = criterion(z,y)
print(f'loss:{loss}')

#进行自动微分，结合反向传播，更新权重和偏执
loss.backward()

#打印w，b用来更新的梯度
print(f'w.grad:{w.grad}')
print(f'b.grad:{b.grad}')