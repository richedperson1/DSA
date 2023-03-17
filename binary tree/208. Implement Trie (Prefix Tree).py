"""
URL : https://leetcode.com/problems/implement-trie-prefix-tree
"""
from collections import *

# Method 1


class Trie:

    def __init__(self):
        self.dictionary = defaultdict(str)

    def insert(self, word: str) -> None:
        self.dictionary[word] = 1  # type: ignore

    def search(self, word: str) -> bool:
        if self.dictionary.get(word):
            return True
        return False

    def startsWith(self, prefix: str) -> bool:
        final_keys = self.dictionary.keys()
        for word in final_keys:
            if word.startswith(prefix):
                return True
        return False


# Method 2

class treeNode:
    def __init__(self) -> None:
        self.children = {}
        self.end_word = False


class Trie2:

    def __init__(self):
        self.rootNode = treeNode()

    def insert(self, word: str) -> None:
        root = self.rootNode
        for char in word:
            if char not in root.children:
                root.children[char] = treeNode()

            root = root.children[char]
        root.end_word = True

    def search(self, word: str) -> bool:
        root = self.rootNode
        for char in word:
            if char not in root.children or root.end_word:
                return False
            root = root.children[char]
        return root.end_word

    def startsWith(self, prefix: str) -> bool:
        root = self.rootNode
        for char in prefix:
            if char not in root.children or root.end_word:
                return False
            root = root.children[char]
        return True
