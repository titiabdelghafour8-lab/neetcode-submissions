import functools


class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        ns = len(s)
        np = len(p)

        @functools.cache
        def dp(i, j): # whether we s matches p but starting at position i in s, and at j in p
            if j >= np and i < ns:
                return False
            if i >= ns and j < np:
                if (j == np - 1 and p[j] == '*') or (j == np - 2 and p[j + 1] == '*'):
                    return True
                return False
            if i >= ns and j >= np:
                return True
            

            if p[j] == '*':
                if p[j - 1] == s[i] or p[j - 1] == '.':
                    return dp(i, j - 1) or dp(i, j + 1) or dp(i - 1, j + 1)
                else:
                    return dp(i, j + 1)
            elif p[j] == '.' or p[j] == s[i]:
                if (j + 1) < np and p[j + 1] == '*':
                    return dp(i, j + 2) or dp(i + 1, j + 1)
                return dp(i + 1, j + 1)
            else:
                return dp(i, j + 1)
        return dp(0, 0)
                
