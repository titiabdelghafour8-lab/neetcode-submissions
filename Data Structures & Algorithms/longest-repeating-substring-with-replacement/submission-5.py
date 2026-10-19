class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        n = len(s)
        count_map = {}
        sliding_start = 0
        max_freq = 0
        max_length = 0 
        for i in range(n):
            count_map[s[i]] = count_map.get(s[i], 0) + 1
            max_freq = max(max_freq, count_map[s[i]])
            if (i - sliding_start + 1) - max_freq > k:
                count_map[s[sliding_start]] -= 1
                sliding_start += 1
                
            max_length = max(i - sliding_start + 1, max_length) 
        return max_length
        