import string

class Solution:
    def isPalindrome(self, s: str) -> bool:
        if not s: 
            return True
        valid_chars = set(string.ascii_lowercase + string.ascii_uppercase + string.digits)
        s_valid = [x.lower() for x in s if x in valid_chars]
        return s_valid == s_valid[::-1]