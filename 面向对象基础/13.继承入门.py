class Father(object):
    def __init__(self):
        self.sex='男'
    def walk(self):
        print('喜欢散步行走')

class Son(Father):
    pass

son=Son()
print(son.sex)
son.walk()