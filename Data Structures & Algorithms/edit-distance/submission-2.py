
import functools


class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        n1 = len(word1)
        n2 = len(word2)
        
        @functools.cache
        def dp(i, j):
            if j < 0: # j < 0 designate an empty string 0 designate a string with only one char
                return (i + 1)
            if i < 0:
                return (j + 1)
            if word1[i] == word2[j]:
                return dp(i - 1, j - 1)
            else:
                return 1 + min(dp(i - 1, j), dp(i, j - 1), dp(i - 1, j - 1))
                # delete dp(i - 1, j) ? 
                # replace dp(i - 1, j - 1) ? 
                # replace dp(i, j - 1) ? 
        return dp(n1 - 1, n2 - 1)

