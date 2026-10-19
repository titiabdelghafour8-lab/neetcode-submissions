class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        i = 0
        result = [0] * n
        stack = deque()
        for i in range(n - 1):
            stack.append(i)
            while stack and temperatures[i + 1] > temperatures[stack[-1]]:
                k = stack.pop()
                result[k] = i + 1 - k
        return result



