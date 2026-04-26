class Car:
    def __init__(self,color,number):
        self.color=color
        self.number=number
    def show(self):
        print(f'颜色{self.color},轮胎数{self.number}')
c1=Car('red',1)
c1.show()
print('-'*22)
c2=Car('blue',2)
c2.show()
