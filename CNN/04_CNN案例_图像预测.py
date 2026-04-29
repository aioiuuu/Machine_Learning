import torch
import torch.nn as nn
from torchvision.datasets import CIFAR10
from torchvision.transforms import ToTensor
from torch.utils.data import DataLoader
import torch.optim as optim
import time
import matplotlib.pyplot as plt
from torchsummary import summary

BATCH_SIZE = 8

def create_dataset():
    train_dataset = CIFAR10(root='../data', train=True, transform=ToTensor(), download=True)
    test_dataset = CIFAR10(root='../data', train=False, transform=ToTensor(), download=True)
    return train_dataset, test_dataset

class ImageModel(nn.Module):
    def __init__(self):
        super().__init__()
        self.conv1 = nn.Conv2d(3, 6, 3, 1, 0)
        self.pool1 = nn.MaxPool2d(2, 2, 0)

        self.conv2 = nn.Conv2d(6, 16, 3, 1, 0)
        self.pool2 = nn.MaxPool2d(2, 2, 0)

        self.linear1 = nn.Linear(576, 120)
        self.linear2 = nn.Linear(120, 84)
        self.output = nn.Linear(84, 10)
    
    def forward(self, x):
        x = self.pool1(torch.relu(self.conv1(x)))
        x = self.pool2(torch.relu(self.conv2(x)))
        x = x.reshape(x.size(0), -1)
        x = torch.relu(self.linear1(x))
        x = torch.relu(self.linear2(x))
        return self.output(x)

def train_model(train_dataset):
    dataloader = DataLoader(train_dataset, batch_size=BATCH_SIZE, shuffle=True)
    model = ImageModel()
    loss_fn = nn.CrossEntropyLoss()
    optimizer = optim.Adam(model.parameters(), lr=0.001)
    
    for epoch in range(10):
        total_loss, total_samples, total_correct = 0.0, 0, 0
        start = time.time()
        
        for x, y in dataloader:
            model.train()
            pred_y = model(x)
            loss = loss_fn(pred_y, y)
            optimizer.zero_grad()
            loss.backward()
            optimizer.step()
            
            total_correct += (pred_y.argmax(dim=-1) == y).sum().item()
            total_loss += loss.item() * len(y)
            total_samples += len(y)
        
        avg_loss = total_loss / total_samples
        accuracy = total_correct / total_samples
        elapsed = time.time() - start
        print(f'第{epoch+1}轮，总损失：{avg_loss:.4f}, 准确率：{accuracy:.4f}, 耗时：{elapsed:.2f}秒')
    
    torch.save(model.state_dict(), '../data/img_model.pth')

def evaluate(test_data):
    dataloader = DataLoader(test_dataset,batch_size=BATCH_SIZE,shuffle=False)
    model = ImageModel()
    model.load_state_dict(torch.load('../data/img_model.pth'))
    total_correct,total_samples = 0,0
    for x,y in dataloader:
        model.eval()
        y_pred = model(x)
        y_pred = torch.argmax(y_pred,dim=-1)
        total_correct += (y_pred==y).sum()
        total_samples+=len(y)

    print(f'acc:{total_correct/total_samples:.2f}')
if __name__ == '__main__':
    train_dataset, test_dataset = create_dataset()
    # model = train_model(train_dataset)
    evaluate(test_dataset)

