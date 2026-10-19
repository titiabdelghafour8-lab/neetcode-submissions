class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix:
            return False
        n = len(matrix)
        m = len(matrix[0])
        k_min = 0
        k_max = m * n - 1
        while k_min <= k_max:
            k_middle = int((k_min + k_max) / 2)
            j = k_middle % m
            i = int((k_middle - j) / m)
            if matrix[i][j] == target:
                return True
            elif matrix[i][j] > target:
                k_max = k_middle - 1
            else:
                k_min = k_middle + 1
        return False

        