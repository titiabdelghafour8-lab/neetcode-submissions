from collections import defaultdict



class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        last_appearances = defaultdict(int)
        n = len(s)
        for i in range(n):
            last_appearances[s[i]] = i
        res = []
        curr_max = 0
        prev_max = -1
        for i in range(n):
            curr_max = max(curr_max, last_appearances[s[i]])
            if i == curr_max:
                res.append(curr_max - prev_max)
                prev_max = curr_max
        return res
