#2
'''
648. Replace Words
'''


import collections


class Trie:
    class TrieNode(collections.defaultdict):
        def __init__(self):
            super().__init__(Trie.TrieNode)
            self.eow = False
    def __init__(self):
        self.root = Trie.TrieNode()

    def insert(self,word):
        node = self.root
        for char in word: node = node[char]
        node.eow = True

    def replace(self,word):
        node = self.root
        for i, char in enumerate(word):
            node = node[char]
            if node.eow: return word[:i + 1]
        return word

class Solution:
    def replaceWords(self,dict: list[str], sentence: str)-> str:
        trie = Trie()
        for prefix in prefixes: trie.insert(prefix)



        return ' '.join(map(trie.replace,sentence.split()))
