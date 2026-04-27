import torch
def model1():
    t1 = torch.arange(0,10,2)
    print(f't1:{t1}')
    print('-'*30)

    t2 = torch.linspace(0,10,4)
    print(f't2:{t2}')
    print('-'*30)
def model2():
    torch.manual_seed(1)
    t1 = torch.rand(size=(2,3))
    print(f't1:{t1}')
    print('-'*30)

    t2 = torch.randn(size=(2,3))
    print(f't2:{t2}')
    print('-'*30)

    t3 = torch.randint(low=1,high=10,size=(3,5))
    print(f't3:{t3}')
    print('-'*30)
if __name__ == '__main__':
    # model1()
    model2()
