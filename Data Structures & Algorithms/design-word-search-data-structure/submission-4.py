from collections import defaultdict


class Node:
    def __init__(self):
        self.next = defaultdict(Node)
        self.is_end = False

class WordDictionary:

    def __init__(self):
        self.root = Node()

    def addWord(self, word: str) -> None:
        node = self.root
        for c in word:
            if c not in node.next:
                node.next[c] = Node()
            node = node.next[c]
        node.is_end = True
        

    def search(self, word: str) -> bool:
        n = len(word)
        def rec_search(node, i):
            if i < n and not node.next:
                return False
            if node.is_end and i == n:
                return True
            if i >= n:
                return False
            if word[i] == ".":
                flag = False
                for c in node.next:
                    flag = flag or rec_search(node.next[c], i + 1)
                return flag
            if word[i] not in node.next:
                return False
            else:
                return rec_search(node.next[word[i]], i + 1)
        return rec_search(self.root, 0)
            
            
        
