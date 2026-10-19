class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        n = len(heights)
        if n == 0:
            return 0
        elif n == 1:
            return heights[0]
        stack = []
        max_surface = 0
        start = 0
        for i in range(n):
            start = i
            while stack and heights[i] < stack[-1][0]:
                el = stack.pop()
                start = el[1]
                max_surface = max(max_surface, el[0] * (i - el[1]))
            stack.append((heights[i], start))
        if stack: 
            max_el = max(stack, key=lambda x: x[0] * (n - x[1]))
            max_surface = max(max_surface, max_el[0] * (n - max_el[1]))
            
        return max_surface


        