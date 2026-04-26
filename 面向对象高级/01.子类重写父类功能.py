class Master(object):
    def __init__(self):
        self.kongfu='[古法煎饼果子]'
    def make_cake(self):
        print(f'运用{self.kongfu}制作')
class School(object):
    def __init__(self):
        self.kongfu='[ai煎饼果子]'
    def make_cake(self):
        print(f'运用{self.kongfu}制作')
class Prentice(Master, School):
    def __init__(self):
        self.kongfu='[独创煎饼果子配方]'
    def make_cake(self):
        print(f'运用{self.kongfu}制作煎饼果子')
if __name__ == '__main__':
    p=Prentice()
    print(p.kongfu)
    p.make_cake()