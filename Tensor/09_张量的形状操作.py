import torch
def model1():
    t1 = torch.randint(1,10,size=(2,3))
    print(f't1:{t1},shape:{t1.shape},row:{t1.shape[0]},column:{t1.shape[1]},{t1.shape[-1]}')

    t2 = t1.reshape(3,2)
    print(f't2:{t2},shape:{t2.shape},row:{t2.shape[0]},column:{t2.shape[1]},{t2.shape[-1]}')

def model2():
    t1 = torch.randint(1,10,size=(2,3))
    print(f't1:{t1},shape:{t1.shape}')    #(2,3)

    # 在0轴上进行扩展
    t2 = t1.unsqueeze(0)
    print(f't2:{t2},shape:{t2.shape}')    #(1,2,3)

    # 在1轴上进行扩展
    t3 = t1.unsqueeze(1)
    print(f't3:{t3},shape:{t3.shape}')   #(2,1,3)

    # 在2维上进行扩展
    t4 = t1.unsqueeze(2)
    print(f't4:{t4},shape:{t4.shape}')   #(2,3,1)

    #删除所有为1的维度：
    t5 = torch.randint(1,10,size=(2,1,3,1,1))
    print(f't5:{t5},shape:{t5.shape}')
    t6 = t5.squeeze()
    print(f't6:{t6},shape:{t6.shape}')

def model3():
    t1 = torch.randint(1,10,size=(2,3,4))
    print(f't1:{t1},shape:{t1.shape}')
    print('*'*30)

    t2 = t1.transpose(0,1)
    print(f't2:{t2},shape:{t2.shape}')

    # 改变维度从（2，3，4）变为（4，2，3）
    t3 = t1.permute(2,0,1)
    print(f't3:{t3},shape:{t3.shape}')

def model4():
    t1 = torch.randint(1,10,size=(2,3))
    print(f't1:{t1},shape:{t1.shape}')
    print('*'*30)
    t2  = t1.view(3,2)
    print(t2.is_contiguous())
    print('*'*30)

    t3 = t1.transpose(0,1)
    print(f't3:{t3},shape:{t3.shape}')
    print(t3.is_contiguous())
if __name__ == '__main__':
    # model1()
    # model2()
    # model3()
    model4()