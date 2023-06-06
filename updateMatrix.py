class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        N = len(mat)
        M = len(mat[0])
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        queue = deque()
        visited = set()
        def isValid(r, c):
            return 0 <= r < N and 0 <= c < M  and (r, c) not in visited

        for r, row in enumerate(mat):
            for c, val in enumerate(row):
                if val == 0:
                    queue.append((r, c))
                    visited.add((r, c))
        print(visited)
        dist = 1
        while queue:
            for _ in range(len(queue)):
                row, col = queue.popleft()
                for dr in directions:
                    new_row, new_col = row + dr[0], col + dr[1]
                    if isValid(new_row, new_col):
                        mat[new_row][new_col] = dist
                        visited.add((new_row, new_col))
                        queue.append((new_row, new_col))
            dist += 1
        return mat
       
