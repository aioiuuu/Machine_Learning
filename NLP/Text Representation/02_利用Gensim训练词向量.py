import pandas as pd
import jieba
import re
from gensim.models import Word2Vec
df=pd.read_csv('../data/ChnSentiCorp_htl_all.csv',encoding='utf-8').dropna()
# print(df.head())
# print(df[df['review'].isna()])处理了脏数据
sentence=[[token for token in jieba.lcut(sentence) if token.strip() != '' and re.match(r'[\u4e00-\u9fff]', token)] for sentence in df['review']]
# print(sentence[0:3])查看sentence的前三条切词
model = Word2Vec(
    sentence,
    vector_size=100,    #词向量维度
    window=5,           #上下文窗口大小
    min_count=2,        #最小词频
    sg=1,               #Skip-Gram
    workers=4           #并行训练线程数
)
model.wv.save_word2vec_format('../data/word2vec.txt')