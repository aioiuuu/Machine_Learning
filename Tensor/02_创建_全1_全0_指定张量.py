import torch
t1 = torch.tensor([[1,2],[3,4],[5,6]])
print(f't1:{t1},type:{type(t1)}')
print('-'*30)

# 基于模板创建张量
t2 = torch.ones_like(t1)
print(f't2:{t2},type:{type(t2)}')
print('-'*30)

# 创建3行2列的零张量
t3 = torch.zeros(2,3)
print(f't3:{t3},type:{type(t3)}')
print('-'*30)

# t4 3行2列
t4 = torch.tensor([[1,2],[3,4],[5,6]])
print(f't2:{t4},type:{type(t4)}')
print('-'*30)

# 基于t4的模板创建张量
t3 = torch.zeros_like(t4)
print(f't3:{t3},type:{type(t3)}')
print('-'*30)

# 创建指定张量
t5 = torch.full(size=(2,3),fill_value=10)
print(f't5:{t5},type:{type(t5)}')
print('-'*30)