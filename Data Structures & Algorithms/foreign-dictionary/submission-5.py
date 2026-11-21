from collections import defaultdict
from collections import deque
        

class Solution:
    def topological_sort(self, adj):
        ins_deg = defaultdict(int)
        for key in adj:
            for neighbor in adj[key]:
                ins_deg[neighbor] += 1
            
        ins_zero = deque()
        for key in adj:
            if ins_deg[key] == 0:
                ins_zero.append(key)
        res = []
        while ins_zero:
            el = ins_zero.popleft()
            res.append(el)
            for neighbor in adj[el]:
                ins_deg[neighbor] -= 1
                if ins_deg[neighbor] == 0:
                    ins_zero.append(neighbor)
        if len(res) != len(adj):
            return ""

        return "".join(res) 
    
    def foreignDictionary(self, words: List[str]) -> str:
        adj = defaultdict(set)
        for word in words:
            for c in word:
                adj[c]
        n = len(words)
        for i in range(n - 1):
            w1 = words[i]
            w2 = words[i + 1]
            m = min(len(w1), len(w2))
            diff_found = False
            for k in range(m):
                if w1[k] != w2[k]:
                    adj[w1[k]].add(w2[k])
                    diff_found = True
                    break
            if not diff_found and len(w1) > len(w2):
                return ""

        return self.topological_sort(adj)








        