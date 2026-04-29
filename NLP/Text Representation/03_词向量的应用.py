from gensim.models import KeyedVectors
import torch
from torch import nn
import jieba

mv = KeyedVectors.load_word2vec_format('../data/word2vec.txt')
unk_token = '<unk>'
index2word = [unk_token]+mv.index_to_key
word2index = {word:index for index,word in enumerate(index2word)}

num_embeddings = len(index2word)
embedding_dim = mv.vector_size
embedding_matrix = torch.randn(num_embeddings, embedding_dim)
for index,word in enumerate(index2word):
    if word in mv:
        embedding_matrix[index] = torch.from_numpy(mv[word])
embedding = nn.Embedding.from_pretrained(embedding_matrix)

text = '我喜欢宇宙飞船'
tokens = jieba.lcut(text)
input_ids = [word2index.get(token, word2index[unk_token]) for token in tokens]
input_tensor = torch.tensor(input_ids)
print(input_tensor)