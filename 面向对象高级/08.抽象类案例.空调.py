class AC:
    def cool_wind(self):
        pass
    def hot_wind(self):
        pass
    def swing_l_r(self):
        pass
class Midea_AC(AC):
    def cool_wind(self):
        print('美的空调制冷')
    def hot_wind(self):
        print('美的空调加热')
    def swing_l_r(self):
        print('美的空调左右摆风')
class GREE(AC):
    def cool_wind(self):
        print('格力空调制冷')
    def hot_wind(self):
        print('格力空调加热')
    def swing_l_r(self):
        print('格力空调左右摆风')
def make_cool(ac: AC):
    ac.cool_wind()

mide = Midea_AC()
geli = GREE()
make_cool(geli)
make_cool(mide)
