from student import Student
class StudentCMS(object):
    def __init__(self):
        self.stu_list=[]
    def show_view(self):
        print("*"*23)
        print('学生管理系统')
        print('\t1.添加学生信息')
        print('\t2.删除学生信息')
        print('\t3.修改学生信息')
        print('\t4.查询单个学生信息')
        print('\t5.查询所有学生信息')
        print('\t6.保存所有学生信息')
        print('\t0.退出系统')
        print('*'*23)
        print()
    def add_student(self):
        pass
    def del_student(self):
        pass
    def update_student(self):
        pass
    def search_one_student(self):
        pass
    def search_all_student(self):
        pass
    def save_student(self):
        pass
    # 加载学生系统
    def load_student(self):
        pass
    def start(self):
        while True:
            self.show_view()
            input_num = input('请输入您要操作的编号：')
            if input_num == '1':
                print('添加学生信息\n')
                self.add_student()
            elif input_num == '2':
                print('删除学生信息\n')
                self.del_student()
            elif input_num == '3':
                print('更新学生信息\n')
                self.update_student()
            elif input_num == '4':
                print('查询单个学生信息\n')
                self.search_one_student()
            elif input_num == '5':
                print('查询所有学生信息\n')
                self.search_all_student()
            elif input_num == '6':
                print('保存学生信息\n')
                self.save_student()
            elif input_num == '0':
                result = input('您确定要退出吗？(Y/N):')
                if result.lower() == 'y':
                    print('谢谢您的使用')
                    break
            else:
                print('输入错误\n')
if __name__ == '__main__':
    s=StudentCMS()
    s.start()
