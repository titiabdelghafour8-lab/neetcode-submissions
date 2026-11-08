from collections import deque


class Solution:
    
    def solve(self, board: List[List[str]]) -> None:
        #first we do a traveral to the borders and detect the regions that aren't surrouneded
        #we store those locations in a set for O(1) CHECKS
        #we then scan the inner cells for regions
        #every travers
        directions = [(1, 0), (0, 1), (0, -1), (-1, 0)]
        in_border_region = set()

        NL = len(board)
        NC = len(board[0])
        visited = set()
        def bfs_not_border(element):
            nonlocal directions, board, visited
            queue = deque([element])
            local_visited = set()
            local_visited.add(element)
            board[element[0]][element[1]] = 'X'
            while queue:
                x, y = queue.popleft()
                for dx, dy in directions:
                    nx, ny = x + dx, y + dy
                    if nx < 0 or ny < 0 or nx >= NL or ny >= NC:
                        continue
                    if board[nx][ny] == 'X':
                        continue
                    if (nx, ny) not in local_visited:
                        queue.append((nx, ny))
                        local_visited.add((nx, ny))
                        visited.add((nx, ny))
                        board[nx][ny] = 'X'

        def bfs_border(element):
            nonlocal directions, board, visited
            queue = deque([element])
            local_visited = set()
            local_visited.add(element)
            visited.add(element)
            while queue:
                x, y = queue.popleft()
                for dx, dy in directions:
                    nx, ny = x + dx, y + dy
                    if nx < 0 or ny < 0 or nx >= NL or ny >= NC:
                        continue
                    if board[nx][ny] == 'X':
                        continue
                    if (nx, ny) not in local_visited:
                        queue.append((nx, ny))
                        local_visited.add((nx, ny))
                        visited.add((nx, ny))

        for i in range(NL):
            if board[i][0] == 'X':
                continue
            bfs_border((i, 0))
        for i in range(NL):
            if board[i][NC - 1] == 'X':
                continue
            bfs_border((i, NC - 1))
        for j in range(NC):
            if board[0][j] == 'X':
                continue
            bfs_border((0, j))
        for j in range(NC):
            if board[NL - 1][j] == 'X':
                continue
            bfs_border((NL - 1, j))
        

        for k in range(NL):
            for l in range(NC):
                if (k, l) in visited or board[k][l] == 'X':
                    continue
                bfs_not_border((k, l))
        

                    
            
                    


        


