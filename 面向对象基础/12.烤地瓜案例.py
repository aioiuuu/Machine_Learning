class SweetPotato():
    def __init__(self):
        self.cook_time=0
        self.cook_state='生的'
        self.condiments=[]
    def cook(self,time):
        self.cook_time+=time
        if 0<=self.cook_time<3:
            self.cook_state='生的'
        elif 3<=self.cook_time<5:
            self.cook_state='半生不熟'
        elif 5<=self.cook_time< 8:
            self.cook_state='熟了'
        elif self.cook_time>= 8:
            self.cook_state='烤糊了'
    def add_condiments(self,condiment):
        self.condiments.append(condiment)
    def __str__(self):
        return (f'这个地瓜的被烤过的时间是{self.cook_time},状态是{self.cook_state}，'
                f'调料有{self.condiments}')
digua=SweetPotato()
print(digua)
print('='*34)
digua.cook(2)
digua.add_condiments('辣椒面')
print(digua)
print('='*34)
digua.cook(2)
digua.add_condiments('酱油')
print(digua)