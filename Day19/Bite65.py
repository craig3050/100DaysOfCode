import itertools
import os
import urllib.request

draw = 'T, I, I, G, T, T, L'

# PREWORK
DICTIONARY = os.path.join('dictionary.txt')
urllib.request.urlretrieve('http://bit.ly/2iQ3dlZ', DICTIONARY)

with open(DICTIONARY) as f:
    dictionary = set([word.strip().lower() for word in f.read().split()])


#
def get_possible_dict_words(draw):
    word_list = _get_permutations_draw(draw)
    matched_words = []
    for word in word_list:
        if word.lower() in dictionary:
            matched_words.append(word.lower())
    print(matched_words)
# """Get all possible words from a draw (list of letters) which are
#        valid dictionary words. Use _get_permutations_draw and provided
#        dictionary"""
#     pass


def _get_permutations_draw(draw):
    letters = ['' if item is "," else item for item in draw]
    str = ''.join(letters).replace(" ", "").strip()
    words = []
    for number in range(2, len(str)):
        permutations = list(itertools.permutations(str, number))
        for item in permutations:
            temp_words = ""
            for second in item:
                temp_words += str.join(second)
            words.append(temp_words)
    return words


get_possible_dict_words(draw)