class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        ROW = len(image)
        COL = len(image[0])
        print('r:', ROW, 'c:', COL)
        visited = [[0 for _ in range(COL)] for _ in range(ROW)]
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        def isValid(r, c, p):
            return 0 <= r < ROW and 0 <= c < COL and not visited[r][c] and image[r][c] == p


        def dfs(row, col, c):
            visited[row][col] = 1
            image[row][col] = color
            for dr in directions:
                new_row = row + dr[0]
                new_col = col + dr[1]
                if isValid(new_row, new_col, c):
                    new_c = image[new_row][new_col]
                    dfs(new_row, new_col, new_c)

                    
        dfs(sr, sc, image[sr][sc])
        return image
