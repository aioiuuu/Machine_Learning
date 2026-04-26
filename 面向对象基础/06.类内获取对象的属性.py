class Car:
    def run(self):
        print('汽车会跑')
    def show(self):
        print(f'我是show函数，对象的颜色：{self.color},轮胎数：{self.number}')
# 创建汽车类的对象
c1=Car()
# 给其c1赋予属性
c1.color = 'blue'
c1.number=4
# 类外访问属性
print(f'颜色：{c1.color},轮胎数:{c1.number}')
# 类外访问行为
c1.run()
c1.show()