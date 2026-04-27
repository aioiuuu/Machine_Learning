import torch
# 随机种子
torch.manual_seed(1)
t1 = torch.randint(1,10,(2,3))
print(f't1:{t1}, shape:{t1.shape}')

t2 = torch.randint(1,10,(2,3))
print(f't2:{t2}, shape:{t2.shape}')

# cat()拼接张量
t3 = torch.cat([t1,t2],dim=0)
print(f't3:{t3}, shape:{t3.shape}')

#stack()拼接张量
t7 = torch.stack([t1,t2],dim=0)
print(f't7:{t7}, shape:{t7.shape}')
