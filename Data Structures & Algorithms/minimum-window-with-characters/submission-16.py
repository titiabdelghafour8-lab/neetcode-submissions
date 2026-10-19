class Solution:
    
    def minWindow(self, s: str, t: str) -> str:
        n1 = len(t)
        n2 = len(s)

        if n1 > n2:
            return ""
        
        s_map = {}
        t_map = {}
        for c in t:
            t_map[c] = t_map.get(c, 0) + 1
        
        
        required = len(t_map)
        formed = 0
        ans = (float("inf"), 0, 0)
        left = 0
        right = 0
        
        while right < n2:
            
            s_map[s[right]] = s_map.get(s[right], 0) + 1
            if s[right] in t_map and s_map[s[right]] == t_map[s[right]]:
                    formed += 1
                
            while formed == required:
                if ans[0] > (right - left + 1):
                    ans = (right - left + 1, left, right)
                if s[left] in t_map and t_map[s[left]] == s_map[s[left]]:
                    formed -= 1
                s_map[s[left]] -= 1
                left += 1
            right += 1
            
        return "" if ans[0] == float("inf") else s[ans[1]: ans[2] + 1]
                





