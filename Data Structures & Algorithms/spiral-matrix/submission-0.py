class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        n = len(matrix)
        m = len(matrix[0])
        right = m - 1
        left = 0
        buttom = n - 1
        top = 0
        res = []
        while left <= right and buttom >= top: 
            for k in range(left, right + 1):
                res.append(matrix[top][k])
            top += 1
            for k in range(top, buttom + 1):
                res.append(matrix[k][right])
            right -= 1
            if not (left <= right and buttom >= top):
                break
            for k in range(right, left - 1, -1):
                res.append(matrix[buttom][k])
            buttom -= 1
            for k in range(buttom, top - 1, -1):
                res.append(matrix[k][left])
            left += 1 
        return res
            