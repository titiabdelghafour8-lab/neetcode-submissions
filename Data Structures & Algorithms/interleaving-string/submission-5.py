import functools
from collections import defaultdict

class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        if not s3 and not s2 and not s1:
            return True
        if s1 == "":
            return s3 == s2
        if s2 == "":
            return s3 == s1
        n1 = len(s1)
        n2 = len(s2)
        n3 = len(s3)
        if n3 != (n1 + n2):
            return False
        repeated = defaultdict(bool)
        @functools.cache
        def dp(i, j, first): # first is True if we are at s1 Flase if we are at s2
            if (i + j) >= n3:
                return True
            if i == n1 and first:
                return dp(i, j, False)

            if j == n2 and not first:
                return dp(i, j, True)

            if first:
                if s3[i + j] == s1[i]:
                    return dp(i + 1, j, first)
                else:
                    first = False
                    if repeated[(i, j)]:
                        return False
                    repeated[(i, j)] = True
                    return dp(i, j, first)
            else:
                if s3[i + j] == s2[j]:
                    return dp(i, j + 1, first)
                else:
                    first = True
                    if repeated[(i, j)]:
                        return False
                    repeated[(i, j)] = True
                    return dp(i, j, first)

        return dp(0, 0, False) or dp(0, 0, True)
