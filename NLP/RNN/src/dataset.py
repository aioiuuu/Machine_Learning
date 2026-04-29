import pandas as pd
import torch
from torch.utils.data import Dataset,DataLoader
import config

class InputMethodDataset(Dataset):
    def __init__(self, path, sample_ratio=1.0):
        self.data = pd.read_json(path, lines=True, orient="records").to_dict(orient="records")
        
        # 数据采样：只使用部分数据加速训练
        if sample_ratio < 1.0:
            sample_size = int(len(self.data) * sample_ratio)
            self.data = self.data[:sample_size]
            print(f"数据采样: 使用 {sample_size}/{len(self.data)} 条数据 (比例: {sample_ratio:.1%})")

    def __len__(self):
        return len(self.data)

    def __getitem__(self, index):
        input_tensor = torch.tensor(self.data[index]['input'], dtype=torch.long)
        target_tensor = torch.tensor(self.data[index]['target'], dtype=torch.long)
        return input_tensor, target_tensor

def get_dataloader(train=True, sample_ratio=None):
    path = config.PROCESSED_DATA_DIR/('train_dataset.jsonl' if train else 'test_dataset.jsonl')
    
    # 如果没有指定采样比例，根据训练/测试使用不同策略
    if sample_ratio is None:
        sample_ratio = config.TRAIN_SAMPLE_RATIO if train else 1.0
    
    dataset = InputMethodDataset(path, sample_ratio=sample_ratio)
    
    return DataLoader(
        dataset,
        batch_size=config.BATCH_SIZE,
        shuffle=True if train else False,
        num_workers=config.NUM_WORKERS,
        pin_memory=True if torch.cuda.is_available() else False
    )

if __name__ == '__main__':
    train_dataloader = get_dataloader(train=True)
    test_dataloader = get_dataloader(train=False)

    for input_tensor,target_tensor in train_dataloader:
        print(input_tensor.shape)
        print(target_tensor.shape)
        break