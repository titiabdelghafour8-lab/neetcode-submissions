from collections import defaultdict
from collections import deque

class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        LEN = len(beginWord)
        word_set = set(wordList)
        word_set.add(beginWord)
        adj = defaultdict(list)
        for word in word_set:
            for i in range(LEN):
                pattern = word[:i] + "*" + word[i+1:]
                adj[pattern].append(word)
        
        queue = deque([(beginWord, 1)])
        visited = set()
        visited.add(beginWord)
        while queue:
            word, num = queue.popleft()
            if endWord == word:
                return num
            for i in range(LEN):
                pattern = word[:i] + "*" + word[i+1:]
                for neighbor in adj[pattern]:
                    if neighbor not in visited:
                        visited.add(neighbor)
                        queue.append((neighbor, num + 1))
        return 0
