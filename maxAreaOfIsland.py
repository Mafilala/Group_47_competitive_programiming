class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        visited = [[0 for _ in range(n)] for _ in range(m)]

        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        def isValid(r, c):
            return 0 <= r < m and 0 <= c < n and grid[r][c] == 1 and not visited[r][c]
        
        def dfs(row, col, kit):
            visited[row][col] = 1
            for dr in directions:
                new_row = row + dr[0]
                new_col = col + dr[1]
                if isValid(new_row, new_col):
                    kit.add((new_row, new_col))
                    dfs(new_row, new_col, kit)
            return len(kit)
        max_area = 0
        for i in range(m):
            for j in range(n):
                if not visited[i][j] and grid[i][j] == 1:
                    area = dfs(i, j, {(i, j)})
                    max_area = max(max_area, area)
        return max_area
