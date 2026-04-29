import torch
import torch.nn as nn
import matplotlib.pyplot as plt

#todo:定义函数，用于完成图像的加载，卷积，特征图可视化操作
def dm01():
    #todo:加载RGB真彩图
    img = plt.imread('../data/a.jpg')
    #todo:打印读取到的图像信息
    # print(f'img:{img},shape:{img.shape}')
    #todo:把图像的形状从：HWC--->CWH,思路：img--》张量---》转换维度
    img2 = torch.tensor(img,dtype=torch.float32)
    img2 = img2.permute(2,0,1)
    # print(f'img2:{img2},shape:{img2.shape}')
    #todo:因为这里只有一张图，所以我们可以给它再增加1个维度，从CHW--->（1，c,h,w）,1张3通道的1066*600像素的图片
    img3 = img2.unsqueeze(dim=0)
    # print(f'img3:{img3},shape:{img3.shape}')
    #todo:定义卷积核
    conv = nn.Conv2d(3,4,3,2,0)
    #todo:具体的卷积计算
    conv_img = conv(img3)
    #todo;擦好看提取到的4个特征图
    img4 = conv_img[0]
    #todo:把上述图从CHW--》HWC
    img5 = img4.permute(1,2,0)
    #todo:可视化
    feature1 = img5[:,:,3].detach().numpy()
    plt.imshow(feature1)
    plt.show()

if __name__ == '__main__':
    dm01()