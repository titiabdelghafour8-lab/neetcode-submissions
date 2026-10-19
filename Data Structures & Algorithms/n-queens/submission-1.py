class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        board = []
        for i in range(n):
            zeros = [0 for k in range(n)]
            board.append(zeros)
        res = []
        def is_safe(i, j):
            for k in range(n):
                if board[k][j]:
                    return False
            k = i 
            l = j
            while k >= 0 and l >= 0:
                if board[k][l]:
                    return False
                k -= 1
                l -= 1
            
            k = i
            l = j
            while k >= 0 and l <= n - 1:
                if board[k][l]:
                    return False
                k -= 1
                l += 1
            return True
        def place(i):
            if i == n:
                current_board = [
                    "".join("Q" if board[i][j] else "." for j in range(n))
                    for i in range(n)
                ]
                res.append(current_board)
                return
            for j in range(n):
                if is_safe(i, j):
                    board[i][j] = 1
                    place(i + 1)
                    board[i][j] = 0
        place(0)
        
        return res
                
























                