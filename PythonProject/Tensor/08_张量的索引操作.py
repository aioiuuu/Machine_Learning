import torch
torch.manual_seed(24)
t1 = torch.randint(1,10,(5,5))
print(f't1:{t1}')
print('*'*30)

print(t1[1])
print(t1[1,:])  # 获取行
print(t1[:,2])  # 获取列
print('*'*30)

# 获取（1，2），（3，4）两个位置的元素
print(t1[[1,3],[2,4]])
print('*'*30)
#范围索引
# 前3行，前2列
print(t1[:3,:2])

print(t1[1:,:2])

print(t1[1::2,0::2])

#创建一个三维张量
t1 = torch.randint(1,10,(2,3,4))
print(f't2:{t1}')

