# self关键字介绍
# 一个类可以有多个对象，
class Car:
    def run(self):
        print('汽车会跑')
        print(f'我是run函数，self的值是：{self}')


c1=Car()
print(f'c1对象：{c1}')
c1.run()
print('-'*34)

c2=Car()
print(f'c1对象：{c2}')
c2.run()
