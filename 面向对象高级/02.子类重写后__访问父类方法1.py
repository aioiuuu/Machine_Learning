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
        Prentice.__init__(self)
        print(f'运用{self.kongfu}制作煎饼果子')
    def make_master_cake(self):
        Master.__init__(self)
        Master.make_cake(self)
    def make_school_cake(self):
        School.__init__(self)
        School.make_cake(self)


if __name__ == '__main__':
    p = Prentice()
    p.make_cake()
    p.make_master_cake()
    p.make_school_cake()
