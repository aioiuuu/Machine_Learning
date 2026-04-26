import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import jieba
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report, accuracy_score

# 1.读取文件
df = pd.read_csv('../data/Sentiment Analysis.csv')
# df.info()

# 删除缺失标注结果的行
df = df.dropna(subset=['标注结果'])

df['labels'] = np.where(df['标注结果']=='好评',1,0)
# print(df)

# 2.抽取labels列,作为标签
y = df['labels']
# print(jieba.lcut('好好学习,天天向上,你爱我我爱你,蜜雪冰城甜蜜蜜,小明汽车'))

comment_list = [",".join(jieba.lcut(line)) for line in df['核心评论内容']]
# print(comment_list[:5])
with open('../data/哈工大停用词表.txt','r',encoding='utf-8')as src_f:
    stopwords_list = src_f.readlines()
    stopwords_list = [line.strip() for line in stopwords_list]
    # 保持顺序去重
    seen = set()
    stopwords_list = [x for x in stopwords_list if not (x in seen or seen.add(x))]

# 统计词频矩阵
transfer = CountVectorizer(stop_words=stopwords_list)
x = transfer.fit_transform(comment_list).toarray()
print(transfer.get_feature_names_out())

x_train = x[:10]
y_train = y[:10]
x_test = x[10:]
y_test = y[10:]
estimator = MultinomialNB()
estimator.fit(x_train,y_train)
y_predict = estimator.predict(x_test)
print('预测结果：',y_predict)
print('准确率：',accuracy_score(y_test,y_predict))


