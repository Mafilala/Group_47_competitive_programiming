class Solution:
    def onesMinusZeros(self, grid: List[List[int]]) -> List[List[int]]:
        cols = [0] * len(grid[0])
        rows = []
        for i in range(len(grid)):
            rc = 0
            for j in range(len(grid[i])):
                val = grid[i][j]
                if val == 0:
                    rc -= 1
                    cols[j] -= 1
                else:
                    rc += 1
                    cols[j] += 1
            rows.append(rc)
        ans = [[] for _ in range(len(grid))]
        for i in range(len(grid)):
                for j in range(len(grid[i])):
                    ans[i].append(rows[i] + cols[j])
        return ans
