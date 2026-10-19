class Solution:
    def longestPalindrome(self, s: str) -> str:
        idx = 0
        len_max = 0
        n = len(s)
        if n == 0:
            return ""
        elif n == 1:
            return s
        dp = [[0] * n for _ in range(n)]
        for i in range(n - 1, -1, -1):
            for j in range(i, n):
                if s[i] == s[j] and ((j - i) <= 2 or (dp[i + 1][j - 1] == 1)):
                    dp[i][j] = 1
                    if len_max < j - i + 1:
                        idx = i
                        len_max = j - i + 1
        
        return s[idx: idx + len_max]