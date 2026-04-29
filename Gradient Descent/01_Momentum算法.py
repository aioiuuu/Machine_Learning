import torch
import torch.nn as nn
import torch.optim as optim

def dm01_momentum():
    # 初始化权重参数
    w = torch.tensor([1.0], requires_grad=True, dtype=torch.float)
    
    # 定义优化器(使用Momentum)
    optimizer = optim.SGD([w], lr=0.01, momentum=0.9)
    
    for i in range(2):
        # 梯度清零
        optimizer.zero_grad()
        
        # 定义损失函数 L = w^2 / 2
        criterion = (w**2) / 2.0
        
        # 反向传播
        criterion.backward()
        
        # 更新参数
        optimizer.step()
        
        print(f'Iteration {i+1}: w={w.item():.6f}, grad={w.grad.item():.6f}, loss={criterion.item():.6f}')


if __name__ == '__main__':
    dm01_momentum()