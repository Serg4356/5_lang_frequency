import sys


def load_data(filepath):
    with open(filepath, 'r', encoding='windows-1251') as text:
        read_text = text.read()
    return read_text


def get_most_frequent_words(text):
    symbols = ['/','.',',','"',"'",':',';','>','<','!','@','#','$','%','^','&','?','*','(',')','{','}','[',']','|','-','+', '  ']
    for symbol in symbols:
        text = text.replace(symbol,'')
    text = text.split(' ')
    words_count_dict = dict()
    for word in text:
        try:
            words_count_dict[word] = words_count_dict[word] + 1
        except KeyError:
            words_count_dict[word] = 1
    words_count_sorted_tuples = sorted(list(words_count_dict.items()),key = lambda word : word[1])
    top_ten_words = list()
    iter_var = 0
    for word in reversed(words_count_sorted_tuples):
        top_ten_words.append(word)
        iter_var +=1
        if(iter_var > 9): break
    return top_ten_words

if __name__ == '__main__':
    print(get_most_frequent_words(load_data('War_and_peace.txt')))