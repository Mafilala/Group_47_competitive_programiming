class Solution:
    def largestLocal(self, grid: List[List[int]]) -> List[List[int]]:
        n = len(grid) - 2
        ans = [[] for i in range(n)]
        for i in range(n):
            for j in range(n):
                max_ = 0
                m1 = max(grid[i][j : j + 3])
                m2 = max(grid[i + 1][j : j + 3])
                m3 = max(grid[i + 2][j : j + 3])
                max_ = max(m1, m2, m3)
                ans[i].append(max_)
        return ans
