#导包
import numpy as np
import matplotlib.pyplot as plt
import torch

#定义函数
def dm01():
    img1 = np.zeros((200,200,3))

    #绘制图像
    plt.imshow(img1)
    plt.show()

    #定义全白图片：
    img2 = torch.full(size=(200,200,3),fill_value=255)
    plt.imshow(img2)
    plt.show()
if __name__ == '__main__':
    dm01()