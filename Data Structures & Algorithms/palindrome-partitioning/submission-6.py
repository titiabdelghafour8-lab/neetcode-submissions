class Solution:
    
    
    def is_palindrome(self, s):
        r = 0
        l = len(s) - 1
        while r <= l:
            if s[r] != s[l]:
                return False
            l -= 1
            r += 1
        return True
    
    def partition(self, s: str) -> List[List[str]]: 
        n = len(s)
        res = []
        one = []
        def backtrack(i, l):
            if l >= n:
                if i == l:
                    res.append(one[:])
                return
                
            if self.is_palindrome(s[i:l + 1]):
                one.append(s[i:l + 1])
                backtrack(l + 1, l + 1)
                one.pop()
            backtrack(i, l + 1)
          
        backtrack(0, 0)
        return res

            

            
