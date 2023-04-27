class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:

        def is_valid_state(board):
            cols = [[] for i in range(9)]
            li = list(map(str, range(1,10)))
            for idx, row in enumerate(board):
                if set(row) != set(li):
                    return False
                for i, val in enumerate(row):
                    cols[i].append(val)
            for col in cols:
                if set(col) != set(li):
                    return False
            for i in range(3):
                for j in range(3):
                    grid = getGrid(i, j, board)
                    if set(grid) != set(li):
                        return False
            print(cols)
            return True
            
        def get_candidates(r, c, board):
            li = list(map(str, range(1, 10)))
            candidates = set(li)
            row = getRow(r, board)
            col = getCol(c, board)
            grid = getGrid(r // 3, c // 3, board)
            val = board[r][c]
            for r in row:
                candidates.discard(r)
            for c in col:
                candidates.discard(c)
            for v in grid:
                candidates.discard(v)
            candidates.discard(val)
            return candidates
        def search(row, col, board):
            if is_valid_state(board):
                return True
            for i in range(9):
                for j in range(9):
                    val = board[i][j]
                    if val == '.':
                        for candidate in get_candidates(i, j, board):
                            board[i][j] = candidate
                            is_solved = search(i, j, board) 
                            if is_solved:
                                return True
                            else:
                                board[i][j] = '.'
                        return False
            return True
        
        def getRow(row, board):
            ans = []
            row = board[row]
            for v in row:
                if v != '.':
                    ans.append(v)
            
            return ans
        
        def getCol(col, board):
            ans = []
            for i in range(9):
                val = board[i][col]
                if val != '.':
                    ans.append(val)
            return ans

        def getGrid(r, c, board):
            ans = []
            for i in range(r * 3, (r * 3) + 3):
                for j in range(c * 3, (c * 3) + 3):
                    val = board[i][j]
                    if val != '.':
                        ans.append(val)
            return ans
        search(0, 0, board)
