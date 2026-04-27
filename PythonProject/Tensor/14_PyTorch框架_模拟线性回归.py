import torch
from torch.utils.data import TensorDataset, DataLoader
from torch import nn, optim
from sklearn.datasets import make_regression
import matplotlib.pyplot as plt

plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False


def create_dataset():
    x, y, coef = make_regression(
        n_samples=100,
        n_features=1,
        bias=14.5,
        noise=10,
        random_state=3,
        coef=True,
    )
    x = torch.tensor(x, dtype=torch.float32)
    y = torch.tensor(y, dtype=torch.float32).reshape(-1, 1)  # 修复：y变成 [n,1]
    return x, y, coef


def train(x, y, true_coef):
    dataset = TensorDataset(x, y)
    dataloader = DataLoader(dataset, batch_size=10, shuffle=True)

    model = nn.Linear(in_features=1, out_features=1)

    print(f'初始权重: {model.weight.item():.4f}, 初始偏置: {model.bias.item():.4f}')

    criterion = nn.MSELoss()
    optimizer = optim.SGD(model.parameters(), lr=0.05)  # 降低学习率

    epochs = 300
    loss_list = []

    for epoch in range(epochs):
        epoch_loss = 0.0
        num_batches = 0

        for train_x, train_y in dataloader:
            y_pred = model(train_x)
            loss = criterion(y_pred, train_y)

            optimizer.zero_grad()
            loss.backward()
            optimizer.step()

            epoch_loss += loss.item()
            num_batches += 1

        avg_loss = epoch_loss / num_batches
        loss_list.append(avg_loss)

        if (epoch + 1) % 50 == 0:
            print(f'轮数：{epoch + 1:4d}, 平均损失：{avg_loss:.4f}')

    learned_weight = model.weight.item()
    learned_bias = model.bias.item()
    print(f'\n========== 训练结果 ==========')
    print(f'真实系数: {true_coef:.4f}, 学习到的权重: {learned_weight:.4f}, 误差: {abs(true_coef - learned_weight):.4f}')
    print(f'真实偏置: 14.5000, 学习到的偏置: {learned_bias:.4f}, 误差: {abs(14.5 - learned_bias):.4f}')
    print(f'最终损失: {loss_list[-1]:.4f}')

    plot_results(x, y, model, loss_list, true_coef)


def plot_results(x, y, model, loss_list, true_coef):
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 5))

    ax1.scatter(x.numpy(), y.numpy(), label='数据点', alpha=0.6, edgecolors='k', s=50)

    x_range = torch.linspace(x.min(), x.max(), 100).reshape(-1, 1)
    with torch.no_grad():
        y_pred = model(x_range)

    ax1.plot(x_range.numpy(), y_pred.numpy(), 'r-', linewidth=2.5,
             label=f'拟合直线 (w={model.weight.item():.2f}, b={model.bias.item():.2f})')

    true_y = true_coef * x_range.numpy().flatten() + 14.5
    ax1.plot(x_range.numpy(), true_y, 'g--', linewidth=2, label=f'真实直线 (w={true_coef:.2f}, b=14.5)')

    ax1.set_xlabel('X', fontsize=12)
    ax1.set_ylabel('Y', fontsize=12)
    ax1.set_title('线性回归拟合结果对比', fontsize=14, fontweight='bold')
    ax1.legend(loc='best', fontsize=10)
    ax1.grid(True, alpha=0.3)

    ax2.plot(loss_list, 'b-', linewidth=2)
    ax2.set_xlabel('Epoch', fontsize=12)
    ax2.set_ylabel('Loss', fontsize=12)
    ax2.set_title('训练损失曲线', fontsize=14, fontweight='bold')
    ax2.grid(True, alpha=0.3)
    ax2.set_xlim(0, len(loss_list))

    plt.tight_layout()
    plt.savefig('linear_regression_result.png', dpi=150, bbox_inches='tight')
    plt.show()
    print('\n结果图已保存为 linear_regression_result.png')


if __name__ == '__main__':
    x, y, coef = create_dataset()
    print(f'数据集信息:')
    print(f'  - 样本数量: {len(x)}')
    print(f'  - X形状: {x.shape}')
    print(f'  - Y形状: {y.shape}')
    print(f'  - 真实系数: {coef:.4f}\n')
    train(x, y, coef)
