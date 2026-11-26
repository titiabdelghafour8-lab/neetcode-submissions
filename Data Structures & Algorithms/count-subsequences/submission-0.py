import functools

class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        ns = len(s)
        nt = len(t)
        @functools.cache
        def dp(i, j): # How many distinct subsequences are there starting at index i at s and j at t ? 
            if j >= nt:
                return 1
            if i >= ns:
                return 0
            

            if s[i] == t[j]:
                return dp(i + 1, j + 1) + dp(i + 1, j)
            else:
                return dp(i + 1, j)
        return dp(0, 0)