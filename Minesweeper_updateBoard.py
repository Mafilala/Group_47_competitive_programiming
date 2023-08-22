class Solution:
    def updateBoard(self, board: List[List[str]], click: List[int]) -> List[List[str]]:
        Row = len(board)
        Col = len(board[0])
        directions = [(0, 1),(1, 0), (0, -1), (-1, 0), (1, 1), (1, -1), (-1, 1), (-1, -1)]
        def isbound(r, c):
            return 0 <= r < Row and 0 <= c < Col
        visited = set()
        def dfs(r, c):
            if not isbound(r, c):
                return
            if (r, c) in visited:
                return
            if board[r][c] not in ['E', 'M']:
                return
            if board[r][c] == 'M':
                board[r][c] = 'X'
                return
            cnt = 0
            visited.add((r, c))
            for row, col in directions:
                if isbound(r + row, c + col):
                    if board[r + row][c + col] == 'M':
                        cnt += 1
            if cnt:
                board[r][c] = str(cnt)
            else:
                board[r][c] = 'B'
                for row, col in directions:
                    dfs(r + row, c + col)

        dfs(click[0], click[1])

        return board
