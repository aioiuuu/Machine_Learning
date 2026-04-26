class Car:
    def __init__(self):
        print('我是无参init魔法方法')
    # 在init魔法方法中，初始化属性
        self.color = 'red'
        self.number=4
    #定义show（）函数，打印该类对象的各个属性值
    def show(self):
        print(f'颜色：{self.color},轮胎数：{self.number}')

c1=Car()
print(c1.color,c1.number)
c1.show()