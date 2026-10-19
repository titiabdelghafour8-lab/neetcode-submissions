class Solution:
    def transpose(self, matrix):
        n = len(matrix)
        for i in range(n):
            for j in range(i):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
        
    def flip(self, matrix):
        n = len(matrix)
        for j in range(n // 2):
            for i in range(n):
                matrix[i][j], matrix[i][n - j - 1] = matrix[i][n - j - 1], matrix[i][j]

    def rotate(self, matrix: List[List[int]]) -> None:
        self.transpose(matrix)
        self.flip(matrix)

        
        