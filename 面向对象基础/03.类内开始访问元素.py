class Car:
    def run(self):
        print(f'{self}汽车在跑。。。')

    def work(self):
        print(f'我是work函数，我的self值：{self}')
        self.run()

c1=Car()
print(f'c1对象：{c1}')
c1.run()
print('-'*34)
c1.work()
print('-'*34)
