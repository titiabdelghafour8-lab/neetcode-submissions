class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        dict_set = set(wordDict)
        n = len(s)
        j = 0 
        dp = [False] * (n + 1)
        dp[0] = True
        for i in range(n):
            for j in range(i + 1):
                if dp[j] and s[j:i + 1] in dict_set: 
                    dp[i + 1] = True
                    break
                else:
                    continue
        return dp[n]