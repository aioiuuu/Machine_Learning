class Master(object):
    def __init__(self):
        self.kongfu='[古法煎饼果子]'
    def make_cake(self):
        print(f'运用{self.kongfu}制作煎饼果子')

class Prentice(Master):
    pass

xiaoming=Prentice()
print(xiaoming.kongfu)
xiaoming.make_cake()