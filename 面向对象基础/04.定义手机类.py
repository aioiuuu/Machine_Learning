class Phone(object):
    def open(self):
        print('手机能正常开机了')
    def close(self):
        print('关机了，睡觉')
    def take_photo(self):
        print('我可以拍照')

phone=Phone()
phone.open()
phone.close()
phone.take_photo()