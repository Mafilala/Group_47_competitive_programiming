class Solution:
    def shortestBridge(self, grid: List[List[int]]) -> int:

        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        N = len(grid)
        M = len(grid[0])

        '''
       0,1,0,0,0
       0,1,0,1,1
       0,0,0,0,1
       0,0,0,0,0
       0,0,0,0,0
        
        '''

        def isValid(r, c):
            return 0 <= r < N and 0 <= c < M and (r, c) not in visited
    
        for r, row in enumerate(grid):
            for c, val in enumerate(row):
                if val == 1:
                    starter = (r, c)
                    break
        queue = deque()
        otherq = deque()
        visited = set()
        visited.add(starter)
        queue.append(starter)
        otherq.append(starter)
        print(starter)
        
        while queue:
            row, col = queue.popleft()
            for dr in directions:
                new_row, new_col = row + dr[0], col + dr[1]
                if isValid(new_row, new_col) and grid[new_row][new_col] == 1:
                    queue.append((new_row, new_col))
                    visited.add((new_row, new_col))
                    otherq.append((new_row, new_col))
        
        print(otherq)
        steps = 0
        while otherq:
            for _ in range(len(otherq)):
                row, col = otherq.popleft()
                for dr in directions:
                    new_row, new_col = row + dr[0], col + dr[1]
                    if isValid(new_row, new_col):
                        if grid[new_row][new_col] == 0:
                            otherq.append((new_row, new_col))
                            visited.add((new_row, new_col))
                        else:
                            return steps
                
            steps += 1


