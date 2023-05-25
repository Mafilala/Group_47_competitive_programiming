class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        R, C = len(grid), len(grid[0])
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1), (1, 1), (-1, 1), (1, -1), (-1, -1)]
        visited = [[0 for _ in range(C)] for _ in range(R)]

        def isValid(row, col):
            return 0 <= row < R and 0 <= col < C and not visited[row][col] and grid[row][col] == 0

        min_length = 0
        queue = deque([(0, 0)])
        visited[0][0] = 1

        if grid[0][0] == 1:
            return -1

        found = False
        while queue and not found:
            for _ in range(len(queue)):
                row, col = queue.popleft()
                if (row, col) == (R - 1, C - 1):
                    found = True
                    break
                for dr in directions:
                    new_row, new_col = row + dr[0], col + dr[1]
                    if isValid(new_row, new_col):
                        visited[new_row][new_col] = 1
                        queue.append((new_row, new_col))
                
            min_length += 1

        return min_length if found else -1
