class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        N = len(maze)
        M = len(maze[0])
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        queue = deque()
        visited = set()
        visited.add((entrance[0], entrance[1]))
        queue.append(entrance)
        def isValid(r, c):
            return 0 <= r < N and 0 <= c < M and (r, c) not in visited and maze[r][c] == '.'

        steps = 1
        while queue:
            for _ in range(len(queue)):
                row, col = queue.popleft()
                for dr in directions:
                    new_row, new_col = row + dr[0], col + dr[1]
                    if isValid(new_row, new_col):
                        if new_row in  [0,N - 1] or new_col in [0, M - 1]:
                            return steps
                        visited.add((new_row, new_col))
                        queue.append((new_row, new_col))
            steps += 1
        return -1
                    
                
