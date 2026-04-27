import numpy as np
import matplotlib.pyplot as plt

def softmax(x):
    exp_x = np.exp(x - np.max(x))
    return exp_x / np.sum(exp_x)

# 随便一组模拟的模型输出 logits
logits = np.array([2.0, 1.5, 0.5, -1.0, 3.0])
prob = softmax(logits)
labels = [f'Class {i+1}' for i in range(len(logits))]

plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False

# 画图
plt.figure(figsize=(10, 5))
x = np.arange(len(labels))

plt.bar(x - 0.2, logits, 0.4, label='原始 logits（得分）', color='#4477aa')
plt.bar(x + 0.2, prob,  0.4, label='Softmax 概率', color='#ee7755')

plt.xlabel('类别')
plt.ylabel('数值')
plt.title('Softmax 效果可视化：原始得分 → 概率分布')
plt.xticks(x, labels)
plt.legend()
plt.grid(alpha=0.3)
plt.tight_layout()
plt.show()