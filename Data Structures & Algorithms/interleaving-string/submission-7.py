import functools


class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        n1 = len(s1)
        n2 = len(s2)
        n3 = len(s3)
        if n3 != (n1 + n2):
            return False

        @functools.cache
        def dp(i: int, j: int) -> bool:
            if (i + j) == n3:
                return True

            ans = False
            if i < n1 and s3[i + j] == s1[i]:
                ans = ans or dp(i + 1, j)
            if j < n2 and s3[i + j] == s2[j]:
                ans = ans or dp(i, j + 1)
            return ans

        return dp(0, 0)