import torch
import matplotlib.pyplot as plt
def test_StepLR():
    #todo:设置学习率初始化之为1
    LR = 0.1
    iteration = 10
    max_epoch = 200
    #todo:初始化参数
    y_true = torch.tensor([0])
    x = torch.tensor([1.0])
    w = torch.tensor([1.0],requires_grad=True)
    #todo:定义优化器
    optimizer = torch.optim.SGD([w],lr=LR,momentum=0.9)
    #todo:定义学习率衰减器
    milestones = [50,125,160]
    scheduler_lr = torch.optim.lr_scheduler.MultiStepLR(optimizer,milestones=milestones,gamma=0.5)
    #todo:获取学习率的值和当前的epoch：
    lr_list,epoch_list = [],[]
    for epoch in range(max_epoch):
        lr_list.append(scheduler_lr.get_last_lr())
        epoch_list.append(epoch)
        for i in range(iteration):
            loss = ((w*x-y_true)**2)/2.0
            optimizer.zero_grad()
            #todo:反向传播
            loss.backward()
            optimizer.step()
        scheduler_lr.step()
    print(lr_list)
    plt.plot(epoch_list,lr_list,label='StepLR Scheduler')
    plt.xlabel('epoch')
    plt.ylabel('learning rate')
    plt.legend()
    plt.show()

if __name__ == '__main__':
    test_StepLR()