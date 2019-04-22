"""
    日期：2019.4.21
    作者：meijamke
    功能：将文本形式的影评分为“正面”或“负面”——二元分类


    问题：由于tensorflow版本过低，tf.keras.dataset里并没有Fashion MNIST 数据集文件夹
    解决：使用keras库的数据集
        用法：
        from keras.datasets import imdb
        (train_data, train_labels), (test_data, test_labels) = imdb.load_data(num_words=10000)
"""
# tensorflow, keras and datasset
import tensorflow as tf
import keras
from keras.datasets import imdb

# lib helper
import numpy as np

# 显示tf版本
# print(tf.__version__)
"""
    加载数据
    为确保数据规模处于可管理的水平，参数 num_words=10000 会保留训练数据中出现频次在前 10000 位的字词。
    数据集已经进行了预处理，影评（字词序列）被转换为整数序列，其中每个整数表示字典中的一个特定字词。
"""
(train_data, train_labels), (test_data, test_labels) = imdb.load_data(num_words=10000)

"""
    探索数据
    数据集已经过预处理：每个样本都是一个整数数组，表示影评中的字词。
    每个标签都是整数值 0 或 1，其中 0 表示负面影评，1 表示正面影评。
"""
# 训练集数据和标签数量
print('train_entries:{}, labels:{}'.format(len(train_data), len(train_labels)))

# 训练集第一个样本
print(train_data[0])

# 影评的长度可能会有所不同。由于神经网络的输入必须具有相同长度，所以这需要在后续处理（填充）
print(len(train_data[0]), len(train_data[1]))

# 将整数转换成字词，查看字词
# reverse_word_index = {'字词': 整数}
word_index = imdb.get_word_index()

word_index = {k: (v+3) for k, v in word_index.items()}
word_index['<PAD>'] = 0
word_index['<START>'] = 1
word_index['<UNK>'] = 2
word_index['<UNUSED>'] = 3

reverse_word_index = {v: k for k, v in word_index.items()}


def decode_review(text):
    return ' '.join(reverse_word_index.get(i, '?') for i in text)


# 使用decode_review查看第一个样本的字词
print(decode_review(train_data[0]))

