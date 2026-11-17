import string
from collections import defaultdict
class Node:
    def __init__(self):
        self.next = defaultdict(Node)
        self.is_end = False

class PrefixTree:

    def __init__(self):
        self.root = Node()

    def insert(self, word: str) -> None:
        i = 0
        node = self.root
        for c in word:
            if c not in node.next:
                new_node = Node()
                node.next[c] = new_node
            node = node.next[c]
        node.is_end = True

        

    def search(self, word: str) -> bool:
        n = len(word)
        if n == 0:
            return True
        node = self.root
        i = 0
        while i < n and word[i] in node.next:
            node = node.next[word[i]]
            i += 1
            if i == n and node.is_end:
                return True
        return False
        

    def startsWith(self, prefix: str) -> bool:
        n = len(prefix)
        if n == 0:
            return True
        node = self.root
        i = 0
        while i < n and prefix[i] in node.next:
            node = node.next[prefix[i]]
            i += 1
            if i == n:
                return True
        return False











        
        