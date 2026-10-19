class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        n = len(board)
        m = len(board[0])
        count = 0
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        def ex(i, j, count):
            if count == len(word):
                return True
            if i < 0 or j < 0 or i >= n or j >= m or word[count] != board[i][j]:
                return False
            temp = board[i][j]
            board[i][j] = "#"
            for di, dj in directions:
                if ex(i + di, j + dj, count + 1):
                    return True
            board[i][j] = temp
            count -= 1
        
        for k in range(n):
            for l in range(m):
                if ex(k, l, 0):
                    return True
        return False

            


            
        