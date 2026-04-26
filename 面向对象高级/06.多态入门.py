# 1.有继承
# 2.函数重写
# 3.父类引用指向子类对象
class Animal:
    def speak(self):
        pass

class Dog(Animal):
    def speak(self):
        # 方法重写
        print('狗叫：汪汪汪')
class Cat(Animal):
    def speak(self):
        # 方法重写
        print('猫叫：喵喵叫')
# Car对象并不是Animal的子类
class Car:
    def speak(self):
        print('车叫：嘀嘀嘀')

def make_noise(an: Animal):
    # 父类引用指向子类对象
    an.speak()

if __name__ == '__main__':
    dog=Dog()
    cat=Cat()
    car=Car()
    make_noise(dog)
    make_noise(cat)
    make_noise(car)