from collections import deque


class Solution:
    def isValid(self, s: str) -> bool:
        if not s:
            return True
        n = len(s)
        parentheses_dict = {"{": "}", "(": ")", "[": "]" }
        i = 0
        closing_queue = deque()
        while i < n:
            if s[i] in parentheses_dict:
                closing_queue.appendleft(parentheses_dict[s[i]])
                i += 1
            else:
                if not closing_queue:
                    return False
                x = closing_queue.popleft()
                if s[i] == x:
                    i += 1
                    continue
                else:
                    return False
        return len(closing_queue) == 0