"""
URL : https://leetcode.com/problems/design-add-and-search-words-data-structure/
"""
from collections import defaultdict


class WordDictionary:

    def __init__(self):
        self.word_2_char = defaultdict()

    def addWord(self, word: str) -> None:
        root = self.word_2_char
        root[len(word)].append(word)

    def search(self, word: str):
        root = self.word_2_char

        num = len(word)
        if "." not in word:
            return word in root[num]

        for dict_word in root[num]:
            for ind, data in word:
                if data != dict_word[ind] and data != ".":
                    break

            else:
                return True

        return False
