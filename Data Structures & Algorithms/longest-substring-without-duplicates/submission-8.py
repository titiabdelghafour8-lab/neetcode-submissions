class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0
        n = len(s)
        visited = dict({ s[0]: 0 })
        sliding_start = 0
        max_length = 1
        for i in range(1, n):
            if s[i] in visited and visited[s[i]] >= sliding_start:
                sliding_start = visited[s[i]] + 1
            max_length = max(max_length, i - sliding_start + 1)
            visited[s[i]] = i 
        return max_length
                
       