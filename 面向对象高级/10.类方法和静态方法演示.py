class Student(object):
    school = '黑马程序员'

    @classmethod
    def show1(cls):
        print(f'cls:{cls}')
        print(cls.school)
        print('我是类方法')
    @staticmethod
    def show2():
        print(Student.school)
        print('我是静态方法')

if __name__ == '__main__':
    s1=Student()
    s1.show1()
    s1.show2()