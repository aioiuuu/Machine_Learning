import torch
import numpy as np
def model1():
    t1 = torch.tensor(10)
    print(f't1:{t1},\ntype:{type(t1)}')
    print('-'*30)
    data = [[1,2,3],[4,5,6]]

    t2 = torch.tensor(data)
    print(f't2:{t2},\ntype:{type(t2)}')
    print('-'*30)
    data = np.random.randint(0,10,(2,3))

    t3 = torch.tensor(data)
    print(f't3:{t3},\ntype:{type(t3)}')
    print('-'*30)

    t4 = torch.Tensor(2,3)
    print(f't4:{t4},\ntype:{type(t4)}')
    print('-'*30)
    
    data = np.random.randint(0,10,(2,3))
    t5 = torch.FloatTensor(data)
    print(f't5:{t5},\ntype:{type(t5)}')

if __name__ == '__main__':
    model1()