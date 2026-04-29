import torch
import torch.nn as nn

#todo:定义RNN
rnn = nn.RNN(input_size=128,hidden_size=256,num_layers=1)
x=torch.randn(size=(5,32,128))
h0 = torch.randn(size=(1,32,256))

output,h1 = rnn(x,h0)
print(f'output:{output.shape}')
print(f'h1:{h1.shape}')