from torch import nn
import config

#todo:搭建神经网络
class InputMethodModel(nn.Module):
    def __init__(self,vocab_size):
        super().__init__()
        #todo:词嵌入层
        self.embedding = nn.Embedding(num_embeddings=vocab_size,
                                      embedding_dim=config.EMBEDDING_DIM)
        #todo:RNN层
        self.rnn = nn.RNN(input_size=config.EMBEDDING_DIM,
                          hidden_size=config.HIDDEN_SIZE,
                          batch_first=True)
        #todo:线性层
        self.linear = nn.Linear(in_features=config.HIDDEN_SIZE,
                                out_features=vocab_size)

#todo:定义前向传播
    def forward(self,x):
        #todo:x.shape:[batch_size,seq_length]
        embed = self.embedding(x)
        #todo:embed.shape:[batch_size,seq_length,embedding_dim]
        output,_=self.rnn(embed)
        #todo:output.shape:[batch_size,seq_length,hidden_size]
        last_hidden_state = output[:,-1,:]
        #todo:last_hidden_state:[batch_size,hidden_size]
        output = self.linear(last_hidden_state)
        #todo:output.shape:[batch_size,vocab_size]
        return output