import functools


class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        ns = len(s)
        np = len(p)

        @functools.cache
        def dp(i, j): # whether we s matches p but starting at position i in s, and at j in p
            if j >= np:
                return i >= ns
            
            first_match = i < ns and (s[i] == p[j] or p[j] == '.')

            if (j + 1) < np and p[j + 1] == '*':
                return (first_match and dp(i + 1, j)) or dp(i, j + 2)

            return first_match and dp(i + 1, j + 1)
        return dp(0, 0)
