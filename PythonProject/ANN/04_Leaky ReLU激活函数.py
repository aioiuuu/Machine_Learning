import torch
import matplotlib.pyplot as plt

# 解决中文显示与负号问题
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False

# ---------------------- 1. 生成数据 ----------------------
# 在 -5 到 5 之间生成 1000 个等间距点
x = torch.linspace(-5, 5, 1000)

# Leaky ReLU 超参数：负区间斜率，默认常用 0.01 / 0.1
negative_slope = 0.1

# 计算 Leaky ReLU 函数值（PyTorch内置函数）
y_leaky_relu = torch.nn.functional.leaky_relu(x, negative_slope=negative_slope)

# 手动计算 Leaky ReLU 导数
# x > 0 时导数为 1，x ≤ 0 时导数为 negative_slope
y_leaky_relu_deriv = torch.where(x > 0, torch.tensor(1.0), torch.tensor(negative_slope))

# ---------------------- 2. 绘图 ----------------------
plt.figure(figsize=(12, 5))

# 子图1：Leaky ReLU 函数图像
plt.subplot(1, 2, 1)
plt.plot(x.numpy(), y_leaky_relu.numpy(), 'c-', linewidth=2, label=f'Leaky ReLU (α={negative_slope})')
plt.grid(True, alpha=0.3)
plt.title('Leaky ReLU 激活函数', fontsize=14, fontweight='bold')
plt.xlabel('x', fontsize=12)
plt.ylabel('leaky_relu(x)', fontsize=12)
plt.axhline(0, color='k', linestyle='--', alpha=0.5)  # 水平中线
plt.axvline(0, color='k', linestyle='--', alpha=0.5)  # 垂直中线
plt.legend(fontsize=10)

# 子图2：Leaky ReLU 导数图像
plt.subplot(1, 2, 2)
plt.plot(x.numpy(), y_leaky_relu_deriv.numpy(), 'm-', linewidth=2, label='Leaky ReLU 导数')
plt.grid(True, alpha=0.3)
plt.title('Leaky ReLU 函数导数', fontsize=14, fontweight='bold')
plt.xlabel('x', fontsize=12)
plt.ylabel("leaky_relu'(x)", fontsize=12)
plt.axhline(0, color='k', linestyle='--', alpha=0.5)
plt.legend(fontsize=10)

plt.tight_layout()
plt.show()