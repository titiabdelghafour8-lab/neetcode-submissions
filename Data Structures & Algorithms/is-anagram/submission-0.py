class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s = sorted(s)
        t = sorted(t)
        return len(s) == len(t) and all(s[i] == t[i] for i in range(len(s)))
        