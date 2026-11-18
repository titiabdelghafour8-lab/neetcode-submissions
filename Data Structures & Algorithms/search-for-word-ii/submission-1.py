from collections import defaultdict

class Node:
    def __init__(self):
        self.next = defaultdict(Node)
        self.word = ""
        self.is_end = False

class PrefixTree:

    def __init__(self):
        self.root = Node()

    def insert(self, word: str) -> None:
        node = self.root
        tmp = []
        for c in word:
            if c not in node.next:
                new_node = Node()
                node.next[c] = new_node
            tmp.append(c)
            node = node.next[c]
        node.is_end = True
        node.word = "".join(tmp)
        




class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        trie = PrefixTree()
        for word in words:
            trie.insert(word)
        n = len(board)
        p = len(board[0])
        directions = [(0, 0), (1, 0), (0, 1), (0, -1), (-1, 0)]
        res = []
        def find_words(i, j, node):
            nonlocal res
            if node.word:
                res.append(node.word)
                node.word = ""
                return
            if board[i][j] in node.next:
                tmp = board[i][j]
                board[i][j] = '#'
                for di, dj in directions:
                    ni, nj = i + di, j + dj
                    if ni < 0 or ni >= n or nj < 0 or nj >= p:
                        continue
                    find_words(ni, nj, node.next[tmp])
                board[i][j] = tmp
        for i in range(n):
            for j in range(p):
                find_words(i, j, trie.root)
        return res

















        