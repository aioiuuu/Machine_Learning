class Student:
    teacher_name='水镜先生'
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def __str__(self):
        return f'姓名:{self.name} 年龄：{self.age}'
if __name__ == '__main__':
    s1 = Student( name='曹操',age = 20)
    s2 = Student( name='许褚',age = 44)
    print(s1)
    print(s2)
    print(s1.teacher_name)
    print(s2.teacher_name)
