class Solution:
    def maxArea(self, heights: List[int]) -> int:
        n = len(heights)
        i = 0
        j = n - 1
        max_area = 0
        max_length = min(heights[i], heights[j]) * (j - i)
        while i < j:
            if heights[i] >= heights[j]:
                j -= 1
            elif heights[i] < heights[j]:
                i += 1
            max_length = max(min(heights[i], heights[j]) * (j - i), max_length)
        return max_length
            

        