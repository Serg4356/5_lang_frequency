import sys
import collections
import re


def load_data(filepath):
    with open(filepath, 'r', encoding='windows-1251') as text:
        read_text = text.read()
    return read_text


def get_most_frequent_words(text):
    text = re.split(r'\W+', text)
    words_count_dict = collections.Counter(text)
    top_size = 10
    return words_count_dict.most_common(top_size)


if __name__ == '__main__':
    top_ten_freq_words = get_most_frequent_words(load_data(sys.argv[1]))
    place = 1
    print('Top ten most frequent words in text: ')
    for word in top_ten_freq_words:
        print('Place {}. Word: {}. Frequency: {}'.format(place,word[0],word[1]))
        place += 1