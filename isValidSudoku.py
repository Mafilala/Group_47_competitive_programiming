class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = [[] for i in range(9) ]
        cols = [[] for i in range(9) ]
        for i in range(9):
            for j in range(9):
                cell1 = board[i][j]
                cell2 = board[j][i]
                if cell1 != ".":
                    rows[i].append(cell1)
                if cell2 != ".":
                    cols[i].append(cell2)
                if (i + 1) % 3 == 0 and (j + 1) % 3 == 0:
                    bigcell = []
                    for a in range(i - 2, i + 1):
                        bigcell.extend([v for v in board[a][j-2 : j + 1] if v != "."])
                    if len(bigcell) != len(set(bigcell)):
                        return False

            if len(rows[i]) != len(set(rows[i])):
                return False
            if len(cols[i]) != len(set(cols[i])):
                return False
        return True
