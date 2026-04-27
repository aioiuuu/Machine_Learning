import torch
import jieba
import torch.nn as nn

def dm01():
    #todo：定义一句话
    text  = '北京冬奥的进度条已经过半，不少外国运动员在完成自己的比赛之后踏上归途。'
    words = jieba.lcut(text)
    print(f'分词结果：{words}')
    #todo:定义词嵌入层
    #todo:参1：词表大小，参2：词嵌入的维度
    embed = nn.Embedding(len(words),4)

    for i,word in enumerate(words):
        word_vec = embed(torch.tensor([i]))
        print(f'{word}的词嵌入向量：{word_vec}')

if __name__ == '__main__':
    dm01()