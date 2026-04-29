import torch
from torch.utils.tensorboard import SummaryWriter
from tqdm import tqdm
import config
from RNN.src.model import InputMethodModel
from dataset import get_dataloader


def train_one_epoch(model, dataloader, loss_fn, optimizer, device):
    model.train()
    total_loss = 0
    for inputs, targets in tqdm(dataloader, desc='训练'):
        inputs = inputs.to(device)
        targets = targets.to(device)

        # todo:前向传播
        outputs = model(inputs)
        loss = loss_fn(outputs, targets)

        # todo:反向传播
        loss.backward()
        optimizer.step()
        optimizer.zero_grad()

        total_loss += loss.item()
    return total_loss / len(dataloader)


def train():
    # todo:确定设备
    device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')

    # todo:数据集 - 使用采样加速训练
    print(f"\n加载训练数据 (采样比例: {config.TRAIN_SAMPLE_RATIO:.1%})...")
    dataloader = get_dataloader(train=True)
    
    with open(config.MODELS_DIR / 'vocab.txt', 'r', encoding='utf-8') as f:
        vocab_list = [line.strip() for line in f.readlines()]
    
    vocab_size = len(vocab_list)
    print(f"词表大小: {vocab_size}")
    print(f"训练批次数量: {len(dataloader)}")

    # todo:调用模型
    model = InputMethodModel(vocab_size=vocab_size).to(device)

    # todo:损失函数
    loss_fn = torch.nn.CrossEntropyLoss()

    # todo:优化器
    optimizer = torch.optim.Adam(model.parameters(), lr=config.LEARNING_RATE)

    # todo:tensorboard writer
    writer = SummaryWriter(log_dir=config.LOGS_DIR)

    # todo:开始训练
    best_loss = float('inf')
    patience = 3  # 早停耐心值
    patience_counter = 0
    
    for epoch in range(1, 1 + config.EPOCHS):
        print("\n" + "=" * 10, f" Epoch:{epoch}/{config.EPOCHS} ", "=" * 10)
        loss = train_one_epoch(model, dataloader, loss_fn, optimizer, device)
        print(f'loss: {loss:.4f}')
        writer.add_scalar('loss', loss, epoch)

        # todo:保存模型
        if loss < best_loss:
            best_loss = loss
            torch.save(model.state_dict(), config.MODELS_DIR / 'best.pth')
            print(f'✓ 模型保存成功 (loss: {loss:.4f})')
            patience_counter = 0
        else:
            patience_counter += 1
            print(f'⚠ 未改善 (patience: {patience_counter}/{patience})')
        
        # 早停机制
        if patience_counter >= patience:
            print(f"\n早停触发！最佳loss: {best_loss:.4f}")
            break
    
    writer.close()
    print(f"\n训练完成！最佳loss: {best_loss:.4f}")


if __name__ == '__main__':
    train()