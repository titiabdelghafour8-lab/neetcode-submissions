class Solution:
    def countSubstrings(self, s: str) -> int:
        n = len(s)
        count = 0
        dp = [[0]*n for _ in range(n)]
        for i in range(n - 1, -1, -1):
            for j in range(i, n):
                if s[i] == s[j] and ((j - i) <= 2 or dp[i + 1][j - 1] == 1):
                    dp[i][j] = 1
                    count += 1
            
                
        return count