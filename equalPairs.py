class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        d = dict()
        count = 0
        columns = [[] for _ in range(len(grid))]
        for row in grid:
            d[tuple(row)] = d.get(tuple(row), 0) + 1
            for idx, col in enumerate(row):
                columns[idx].append(col)
        for column in columns: 
            count += d.get(tuple(column), 0)
        return count
