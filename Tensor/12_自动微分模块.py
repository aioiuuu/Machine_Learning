import torch
#定义变量，记录初始的权重
w = torch.tensor(10,requires_grad=True,dtype=torch.float)

#定义loss变量，表示损失函数
loss = 2 *  w**2

#计算梯度
loss.backward()

#带入权重更新公式
w.data = w.data - 0.01 * w.grad

#打印最终结果
print(f'w:{w}')