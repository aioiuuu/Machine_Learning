import torch
from torch import nn
rnn = nn.RNN(input_size=3,hidden_size=4,batch_first=True,num_layers=2,bidirectional=True)

# input.shape:(batch_size,seq_len,input_size)
input = torch.randn(2,4,3)

#output.shape:[batch_size,seq_len,2*hidden_size]
#hn.shape:[num_layers*num_directions,batch_size,hidden_size]
output,hn = rnn(input)
print(output.shape)         #(2,4,8)
print(hn.shape)             #(4,2,4)