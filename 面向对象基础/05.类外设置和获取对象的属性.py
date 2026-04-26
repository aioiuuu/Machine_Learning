class Car(object):
    def run(self):
        print(f'{self}汽车会跑')
c1=Car()
c1.run()
c1.color='red'
c1.number=4
print(f'颜色：{c1.color}  轮胎数：{c1.number}')
