import torch
t1 = torch.tensor([10,20],requires_grad=True,dtype=torch.float)
print(f't1:{t1},type:{type(t1)}')

#尝试把上述对象转化为张量
# n1 = t1.numpy()
# print(f'n1:{n1},type:{type(n1)}')

#解决方法：使用detach()函数，拷贝一份张量，然后转化
n2 = t1.detach().numpy()
print(f'n2:{n2},type:{type(n2)}')