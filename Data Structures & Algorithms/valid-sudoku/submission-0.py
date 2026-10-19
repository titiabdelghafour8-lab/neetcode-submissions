class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        n = 9
        sub_n = 9
        row_check = [0] * (n * n)
        column_check = [0] * (n * n)
        bucket_check = [0] * (n * n)
        for i in range(n):
            for j in range(n):
                if board[i][j] != ".":
                    row_check[i * n + int(board[i][j]) - 1] += 1
                if board[j][i] != ".":
                    column_check[i * n + int(board[j][i]) - 1] += 1
                k = j // 3 + 3 * (i // 3)
                l = j % 3 + 3 * (i % 3)
                if board[k][l] != ".":
                    bucket_check[i * n + int(board[k][l]) - 1] += 1
        for i in range(n):
            for j in range(n):
                if max(bucket_check[i * n + j], column_check[i * n + j], row_check[i * n + j]) > 1:
                    return False
        return True