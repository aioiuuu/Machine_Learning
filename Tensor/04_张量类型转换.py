import torch
t1 = torch.tensor([1,2,3,4,5],dtype=torch.float)
print(f't1:{t1},(元素)类型：{t1.dtype},(张量)类型：{type(t1)}')

t2 = t1.type(torch.int16)
print(f't2:{t2},(元素)类型：{t2.dtype},(张量)类型：{type(t2)}')