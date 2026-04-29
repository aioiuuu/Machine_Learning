import torch.nn as nn

#均匀分布随机初始化
def dm01():
    #创建一个线性层，输入维度为5，输出维度为3
    linear = nn.Linear(5,3)
    #对权重进行初始化，从0-1均匀分布产生参数
    nn.init.uniform_(linear.weight)
    #对偏置进行初始化，从0-1均匀分布产生参数
    nn.init.uniform_(linear.bias)
    #打印生成结果
    print(linear.weight)

#固定值初始化
def dm02():
    # 创建一个线性层，输入维度为5，输出维度为3
    linear = nn.Linear(5, 3)
    # 对权重进行初始化，设置固定值3
    nn.init.constant_(linear.weight,val=3)
    # 对偏置进行初始化，设置固定值3
    nn.init.constant_(linear.bias,val=3)
    # 打印生成结果
    print(linear.weight)

# 全1初始化
def dm03():
    # 创建一个线性层，输入维度为5，输出维度为3
    linear = nn.Linear(5, 3)
    # 对权重进行初始化，设置全1值
    nn.init.ones_(linear.weight)
    # 对偏置进行初始化，设置全1值
    nn.init.ones_(linear.bias)
    # 打印生成结果
    print(linear.weight)

# 全0值初始化
def dm04():
    # 创建一个线性层，输入维度为5，输出维度为3
    linear = nn.Linear(5, 3)
    # 对权重进行初始化，设置全0值
    nn.init.zeros_(linear.weight)
    # 对偏置进行初始化，设置全0值
    nn.init.zeros_(linear.bias)
    # 打印生成结果
    print(linear.weight)

#正态初始化
def dm05():
    # 创建一个线性层，输入维度为5，输出维度为3
    linear = nn.Linear(5, 3)
    # 对权重进行初始化，设置正态分布
    nn.init.normal_(linear.weight)
    # 对偏置进行初始化，设置正态分布
    nn.init.normal_(linear.bias)
    # 打印生成结果
    print(linear.weight)

#kaiming初始化
def dm06():
    # 创建一个线性层，输入维度为5，输出维度为3
    linear = nn.Linear(5, 3)
    # 对权重进行初始化，设置kaiming初始化
    nn.init.kaiming_normal_(linear.weight)
    # 打印生成结果
    print(linear.weight)

#xavier初始化
def dm07():
    # 创建一个线性层，输入维度为5，输出维度为3
    linear = nn.Linear(5, 3)
    # 对权重进行初始化，设置xavier初始化
    nn.init.xavier_normal_(linear.weight)
    # 打印生成结果
    print(linear.weight)

if __name__ == '__main__':
    # dm01()
    # dm02()
    # dm03()
    # dm04()
    # dm05()
    # dm06()
    dm07()