import torch
import numpy as np
def model1():
    t1 = torch.tensor([1,2,3,4,5])
    print(f't1:{t1},type:{type(t1)}')
    print('-'*30)
    # 不共享内存
    n1 = t1.numpy().copy()
    print(f'n1:{n1},type:{type(n1)}')

def model2():
    n1 = np.array([11,22,33])
    print(f'n1:{n1},type:{type(n1)}')
    t1 = torch.from_numpy(n1).type(torch.float32)
    print(f't1:{t1},type:{type(t1)}')

    t2 = torch.tensor(n1)
    print(f't2:{t2},type:{type(t2)}')

def model3():
    t1 = torch.tensor(100)
    print(f't1:{t1},type:{type(t1)}')

    value = t1.item()
    print(f'value:{value},type:{type(value)}')


if __name__ == '__main__':
    # model1()
    # model2()
    model3()