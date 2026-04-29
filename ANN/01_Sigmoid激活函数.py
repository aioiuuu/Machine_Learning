import torch
import matplotlib.pyplot as plt

# 解决中文乱码问题（必须添加，否则标题会显示方块）
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False

# 创建画布和坐标轴（1行2列，这里只用到第1个）
_, axes = plt.subplots(1, 2, figsize=(12, 5))  # 补充figsize优化显示

# 生成输入x：在[-20, 20]区间取1000个等间距点
x = torch.linspace(-20, 20, 1000)

# 输入值x通过sigmoid函数转换成激活值y
y = torch.sigmoid(x)

# 绘制Sigmoid函数图像
axes[0].plot(x.numpy(), y.numpy())  # 补充.numpy()，Matplotlib不直接支持Tensor
axes[0].grid(True)  # 显式指定True，增强可读性
axes[0].set_title('Sigmoid 函数图像', fontsize=14, fontweight='bold')
axes[0].set_xlabel('x', fontsize=12)
axes[0].set_ylabel('sigmoid(x)', fontsize=12)
axes[0].set_xlim(-20, 20)
axes[0].set_ylim(-0.1, 1.1)

# （可选）在第2个坐标轴补充Sigmoid的导数图像，方便理解
y_deriv = y * (1 - y)
axes[1].plot(x.numpy(), y_deriv.numpy(), 'r-')
axes[1].grid(True)
axes[1].set_title('Sigmoid 函数的导数图像', fontsize=14, fontweight='bold')
axes[1].set_xlabel('x', fontsize=12)
axes[1].set_ylabel("sigmoid'(x)", fontsize=12)
axes[1].set_xlim(-20, 20)
axes[1].set_ylim(-0.1, 0.3)

plt.tight_layout()
plt.show()

