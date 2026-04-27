import torch
import matplotlib.pyplot as plt

# 解决中文显示
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False

# 生成 x 数据
x = torch.linspace(-5, 5, 1000)

# ReLU 函数
y_relu = torch.relu(x)

# ReLU 导数
y_relu_deriv = torch.where(x > 0, torch.tensor(1.0), torch.tensor(0.0))

# 绘图
plt.figure(figsize=(12, 5))

# 左图：ReLU
plt.subplot(1, 2, 1)
plt.plot(x.numpy(), y_relu.numpy(), 'r-', linewidth=2, label='ReLU')
plt.grid(alpha=0.3)
plt.title('ReLU 激活函数', fontsize=14)
plt.xlabel('x')
plt.ylabel('relu(x)')
plt.axhline(0, color='k', linestyle='--', alpha=0.5)
plt.axvline(0, color='k', linestyle='--', alpha=0.5)
plt.legend()

# 右图：ReLU 导数
plt.subplot(1, 2, 2)
plt.plot(x.numpy(), y_relu_deriv.numpy(), 'g-', linewidth=2, label='ReLU 导数')
plt.grid(alpha=0.3)
plt.title('ReLU 导数', fontsize=14)
plt.xlabel('x')
plt.ylabel('relu\'(x)')
plt.legend()

plt.tight_layout()
plt.show()