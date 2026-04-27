import torch
import jieba
from torch.utils.data import DataLoader
import torch.nn as nn
import torch.optim as optim
import time

def build_vocab():
    unique_words,all_words = [],[]
    for line in open('../data/jaychou_lyrics.txt','r',encoding='utf-8'):
        words = jieba.lcut(line.strip())
        all_words.append(words)
        for word in words:
            if word not in unique_words:
                unique_words.append(word)
    
    # 添加空格字符到词汇表
    if ' ' not in unique_words:
        unique_words.append(' ')
    
    word_count = len(unique_words)
    # print(word_count)
    word_to_index = {word:i for i,word in enumerate(unique_words)}
    corpus_idx = []
    for words in all_words:
        tmp = []
        for word in words:
            tmp.append(word_to_index[word])
        tmp.append(word_to_index[' '])
        corpus_idx.extend(tmp)
        # print(f'corpus_idx:{corpus_idx}')
    return unique_words,word_to_index,word_count,corpus_idx

class LyricsDataset(torch.utils.data.Dataset):
    def __init__(self,corpus_idx,num_chars):
        self.corpus_idx = corpus_idx
        self.num_chars = num_chars
        self.total_length = len(self.corpus_idx)
        self.number = max(0, self.total_length - self.num_chars - 1)
    def __len__(self):
        return self.number
    def __getitem__(self,idx):
        start = idx
        end = start + self.num_chars
        x = self.corpus_idx[start:end]
        y = self.corpus_idx[start+1:end+1]
        return torch.tensor(x),torch.tensor(y)

class TextGenerator(nn.Module):
    def __init__(self,word_count):
        super(TextGenerator,self).__init__()
        self.ebd = nn.Embedding(word_count,128)
        self.rnn = nn.RNN(128,128,1)
        self.out = nn.Linear(128,word_count)
    def forward(self,inputs,hidden):
        embed = self.ebd(inputs)
        output,hidden = self.rnn(embed.transpose(0,1),hidden)
        output = self.out(output.reshape((-1,output.shape[-1])))
        return output,hidden
    def init_hidden(self,bs):
        return torch.zeros(1,bs,128)
def train():
    index_to_word,word_to_index,word_count,corpus_idx = build_vocab()
    lyrics = LyricsDataset(corpus_idx,32)
    criterion = nn.CrossEntropyLoss()
    optimizer = optim.Adam(model.parameters(),lr=0.001)
    epoch = 10
    for epoch_idx in range(epoch):
        lyrics_dataloader = DataLoader(lyrics,shuffle=True,batch_size=1)
        start = time.time()
        iter_num = 0
        total_loss = 0
        for x,y in lyrics_dataloader:
            hidden = model.init_hidden(bs=1)
            output,hidden = model(x,hidden)
            y = torch.transpose(y,0,1).contiguous().view(-1)
            loss = criterion(output,y)
            optimizer.zero_grad()
            loss.backward()
            optimizer.step()
            iter_num += 1
            total_loss += loss.item()
        print(f'epoch:{epoch_idx+1} loss:{total_loss/iter_num} time:{time.time()-start}')
    torch.save(model.state_dict(),'../model/jaychou_lyrics.pth')


if __name__ == '__main__':
    unique_words,word_to_index,word_count,corpus_idx = build_vocab()
    # dataset = LyricsDataset(corpus_idx,num_chars=5)
    # x,y = dataset[1]
    # print(f'输入值：{x}')       #输入[0,1,2,3,40]    输入【1，2，
    # print(f'输出值：{y}')       #输出[1,2,3,40,41]
    model = TextGenerator(word_count)
    train()
