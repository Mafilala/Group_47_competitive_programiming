class Solution:
    def maxSum(self, grid: List[List[int]]) -> int:
        row = len(grid)
        col = len(grid[0])
        max_sum = float('-inf')
        for i in range(row - 2):
            for j in range(col - 2):
                s = sum(grid[i][j: j+3]) + sum(grid[i + 2][j: j+3]) + grid[i + 1][j + 1]
                if s > max_sum:
                    max_sum = s
        return max_sum
