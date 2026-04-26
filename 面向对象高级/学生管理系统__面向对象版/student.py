# 该文件用于记录学生类
# 学生的属性信息为：姓名，年龄，性别，手机号，描述信息
class Student:
    def __init__(self,name,gender,age,phone,desc):
        self.name=name
        self.gender=gender
        self.age=age
        self.phone=phone
        self.desc=desc
    def __str__(self):
        return (f'姓名：{self.name} 性别：{self.gender} 年龄：{self.age} 手机号：{self.phone} 描述信息：{self.desc}')
if __name__ == '__main__':
    s=Student(name='桥上',gender='男',age=22,phone='0123456789',desc='hello')
    print(s)