import pandas as pd
from pathlib import Path
import jieba
from sklearn.model_selection import train_test_split
import config
from tqdm import tqdm

RAW_DATA_DIR=Path(__file__).parent.parent/"data"/"raw"

def build_dataset(sentences,word2index):
    indexed_sentences = [[word2index.get(token, 0) for token in jieba.lcut(sentence)] for sentence in sentences]
    dataset = []
    for sentence in tqdm(indexed_sentences, desc='构建数据集'):
        for i in range(len(sentence) - config.SEQ_LEN):
            input = sentence[i:i + config.SEQ_LEN]
            target = sentence[i + config.SEQ_LEN]
            dataset.append({'input': input, 'target': target})
    return dataset


def process():
    print('开始处理数据')

    #1.todo:规范路径
    df = pd.read_json(config.RAW_DATA_DIR/"synthesized_.jsonl",lines=True,orient="records")
    sentences = []

    #2.todo；提取句子
    for dialog in df['dialog']:
        for sentence in dialog:
            sentences.append(sentence.split('：')[1])
    # print(sentences[0:5])
    # print(f'句子总数：{len(sentences)}')

    #3.todo:划分数据集
    train_sentences,test_sentences = train_test_split(sentences,test_size=0.2)

    #4.todo:构建词表
    vocab_set = set()
    for sentence in tqdm(train_sentences,desc='构建词表'):
        vocab_set.update(jieba.lcut(sentence))

    vocab_list = ['<unk>'] + list(vocab_set)
    # print(f'词表大小：{len(vocab_list)}')

    #5.todo:保存词表
    with open(config.MODELS_DIR/"vocab.txt","w",encoding="utf-8") as f:
        f.write('\n'.join(vocab_list))

    #6.todo:构建训练集
    word2index = {word:index for index,word in enumerate(vocab_list)}
    # print(train_dataset[0:3])
    train_dataset = build_dataset(train_sentences,word2index)

    #7.todo:保存训练集
    pd.DataFrame(train_dataset).to_json(config.PROCESSED_DATA_DIR/"train_dataset.jsonl",orient="records",lines=True)

    #8.todo:构建测试集
    test_dataset = build_dataset(test_sentences,word2index)

    #9.todo:保存测试集
    pd.DataFrame(test_dataset).to_json(config.PROCESSED_DATA_DIR/"test_dataset.jsonl",orient="records",lines=True)

    print('数据处理完成')
if __name__ == '__main__':
    process()