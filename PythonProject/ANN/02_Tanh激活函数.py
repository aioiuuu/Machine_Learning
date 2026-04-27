import torch
import matplotlib.pyplot as plt

# 解决中文显示问题
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False

# ---------------------- 1. 生成数据 ----------------------
# 在 -5 到 5 之间生成 1000 个点（足够平滑）
x = torch.linspace(-5, 5, 1000)

# 计算 Tanh 函数值
y_tanh = torch.tanh(x)

# Tanh 导数公式：1 - tanh(x)²
y_tanh_deriv = 1 - torch.tanh(x) ** 2

# ---------------------- 2. 绘图 ----------------------
plt.figure(figsize=(12, 5))

# 子图1：Tanh 函数图像
plt.subplot(1, 2, 1)
plt.plot(x.numpy(), y_tanh.numpy(), 'b-', linewidth=2, label='Tanh')
plt.grid(True, alpha=0.3)
plt.title('Tanh 激活函数', fontsize=14)
plt.xlabel('x')
plt.ylabel('tanh(x)')
plt.axhline(0, color='k', linestyle='--', alpha=0.5)  # 水平中线
plt.axvline(0, color='k', linestyle='--', alpha=0.5)  # 垂直中线
plt.legend()

# 子图2：Tanh 导数图像
plt.subplot(1, 2, 2)
plt.plot(x.numpy(), y_tanh_deriv.numpy(), 'r-', linewidth=2, label='Tanh 导数')
plt.grid(True, alpha=0.3)
plt.title('Tanh 函数导数', fontsize=14)
plt.xlabel('x')
plt.ylabel('tanh\'(x)')
plt.axhline(0, color='k', linestyle='--', alpha=0.5)
plt.legend()

plt.tight_layout()
plt.show()