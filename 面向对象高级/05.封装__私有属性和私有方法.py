# 封装属于面向对象的三大属性之一，就是隐藏对象的属性和实现细节。
# 仅对外提供公共接口
# 提高了代码的安全性，但是代码量增加了
class Prentice:
    def __init__(self):
        self.kongfu='[黑马煎饼果子]'
        self.__money = 20000
    def make_cake(self):
        print(f'运用{self.kongfu}制作煎饼果子')
    # 针对私有的属性，提供公共的访问方式
    def get_money(self):
        return self.__money
    def set_money(self, money):
        self.__money = money

class Tusun(Prentice):
    pass

if __name__ == '__main__':
    ts = Tusun()
    print(ts.kongfu)
    ts.make_cake()
    print("="*34)
    # print(ts.__money)#父类私有成员，子类无法访问
    print(f'你的私房钱为{ts.get_money()}元')
    ts.set_money(100)
    print(f'现在你的钱为{ts.get_money()}元')