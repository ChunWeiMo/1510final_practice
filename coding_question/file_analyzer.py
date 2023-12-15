import itertools


def create_word_set(word_list: list) -> set:
    word_set = set()
    for word in word_list:
        word_clean = ''
        for character in word:
            if not character.isalnum():
                character = ''
            word_clean += character
        word_set.add(word)
    return word_set


def unique_words(word_set_1: set, word_set_2: set) -> list:
    words_list = list(word_set_1) + list(word_set_2)
    words_count = dict()
    for word in words_list:
        if word in words_count:
            words_count[word] += 1
        else:
            words_count[word] = 1
    unique_words_list = list()
    for key in words_count:
        if words_count[key] == 1:
            unique_words_list.append(key)
    return unique_words_list


def create_word_dict(word_set_1: set, word_set_2: set) -> dict:
    words_dictionary = dict()
    words_dictionary['unique union'] = unique_words(word_set_1, word_set_2)
    words_dictionary['intersection'] = word_set_1.intersection(word_set_2)
    words_dictionary['first diff'] = word_set_1.difference(word_set_2)
    words_dictionary['second diff'] = word_set_1.difference(word_set_2)
    words_dictionary['symmetric diff'] = word_set_1.symmetric_difference(word_set_2)
    return words_dictionary


def file_analyzer(filename_1: str, filename_2: str) -> dict:
    try:
        with open(filename_1) as filename_1_object,  open(filename_2) as filename_2_object:
            filename_1_content_str = filename_1_object.read()
            filename_2_content_str = filename_2_object.read()
    except FileNotFoundError:
        print("File does not exist.")
    else:
        filename_1_content_list = filename_1_content_str.lower().split()
        filename_2_content_list = filename_2_content_str.lower().split()
        filename_1_set = create_word_set(filename_1_content_list)
        filename_2_set = create_word_set(filename_2_content_list)
        words_dictionary = create_word_dict(filename_1_set, filename_2_set)
        return words_dictionary

def main():
    print(file_analyzer(filename_1='file_1.txt', filename_2='file_2.txt'))


if __name__ == '__main__':
    main()
