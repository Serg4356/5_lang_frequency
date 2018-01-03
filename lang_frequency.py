import sys
import collections
import re


def load_data(filepath):
    with open(filepath, 'r', encoding='windows-1251') as file:
        text = file.read()
    return text


def get_most_frequent_words(text):
    text = re.split(r'\W+', text.lower())
    words_counter = collections.Counter(text)
    output_number_of_words = 10
    return words_counter.most_common(output_number_of_words)


if __name__ == '__main__':
    top_freq_words = get_most_frequent_words(load_data(sys.argv[1]))
    print('Top ten most frequent words in text: ')
    for word, freq in top_freq_words:
        print('"{}". freq.: {}'.format(word, freq))
