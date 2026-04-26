# 定义三种战斗机
class HeroFighter(object):
    def power(self):
        return 60
class AdvHeroFighter(HeroFighter):
    def power(self):
        return 80
class EnemyFighter(object):
    def power(self):
        return 70
# 构建对战平台
def object_play(hero,enemy):
    if hero.power() >=enemy.power():
        print('英雄机 战胜 敌机')
    else:
        print('英雄机 惜败 敌机')
object_play(HeroFighter(),EnemyFighter())
object_play(AdvHeroFighter(),EnemyFighter())