import torch
#创建张量
t1 = torch.tensor([
    [1,2,3],
    [4,5,6]
], dtype=torch.float)
print(f't1:{t1}')

#sum求和
print(t1.sum(dim=0))   #按行求和
print(t1.sum(dim=1))   #按列求和
print(t1.sum())
print('-'*30)

#max()求最大值，min()同理
print(t1.max(dim=0))     #按列求最大值
print(t1.max(dim=1))     #按行求最大值
print(t1.max())
print('-'*30)

#mean()求均值
print(t1.mean(dim=0))   #按列求均值
print(t1.mean(dim=1))   #按行求均值
print(t1.mean())        #全局求均值
print('-'*30)

# pow() n次方
print(t1.pow(2))
print(t1**2)
print('-'*30)

# exp() 指数
print(t1.exp())
print('-'*30)

#log() 对数
print(t1.log())
print('-'*30)