class Student(object):
    def __init__(self):
        self.current_weight=100
    def run(self):
        print('跑步')
        self.current_weight=self.current_weight - 0.5
    def eat(self):
        print('吃饭')
        self.current_weight=self.current_weight + 2
    def __str__(self):
        return f'当前体重为：{self.current_weight}kg'

student=Student()
student.run()
student.eat()
print(student)



