import itertools
import os
import urllib.request

draw = 'W, F, G, L, B, N'

# # PREWORK
# DICTIONARY = os.path.join('/tmp', 'dictionary.txt')
# urllib.request.urlretrieve('http://bit.ly/2iQ3dlZ', DICTIONARY)
#
# with open(DICTIONARY) as f:
#     dictionary = set([word.strip().lower() for word in f.read().split()])
#
#
# def get_possible_dict_words(draw):
#     """Get all possible words from a draw (list of letters) which are
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
    print(words)
    return words


    return permutations
    """Helper to get all permutations of a draw (list of letters), hint:
       use itertools.permutations (order of letters matters)"""
    pass

_get_permutations_draw(draw)