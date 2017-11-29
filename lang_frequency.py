import sys
import collections


def load_data(filepath):
    with open(filepath, 'r', encoding='windows-1251') as text:
        read_text = text.read()
    return read_text


def get_most_frequent_words(text):
    symbols = ['/', '.', ',', '"', "'", ':', ';', '>', '<', '!', '@', '#', '$', '%', '^', '&', '?', '*', '(', ')', '{', '}', '[', ']', '|', '-', '+', '  ']
    for symbol in symbols:
        text = text.replace(symbol, '')
    text = text.split(' ')
    words_count_dict = collections.Counter()
    for word in text:
        words_count_dict[word] += 1
    return words_count_dict.most_common(10)


if __name__ == '__main__':
    print('Топ 10 наиболее часто встречающихся слов: \n',get_most_frequent_words(load_data(sys.argv[1])))