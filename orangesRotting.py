class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        queue = deque()
        r = len(grid)
        c = len(grid[0])
        fresh = 0
        directions = [
            (1, 0),
            (-1, 0),
            (0, 1),
            (0, -1)
        ]

        def isBound(row, col):
            return 0 <= row < r and 0 <= col < c

        for i in range(r):
            for j in range(c):
                if grid[i][j] == 2:
                    queue.append((i, j))
                if grid[i][j] == 1:
                    fresh += 1
        mins = 0
        maf = 3
        while queue and fresh:
            for i in range(len(queue)):
                row, col = queue.popleft()
                for dr in directions:
                    new_row = row + dr[0]
                    new_col = col + dr[1]

                    if isBound(new_row, new_col):
                        
                        if grid[new_row][new_col] == 1:
                            fresh -= 1
                            grid[new_row][new_col] = 2
                            queue.append((new_row, new_col))

            mins += 1

        return mins if fresh == 0 else -1
