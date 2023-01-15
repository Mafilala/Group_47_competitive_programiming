class Solution:
    def validTicTacToe(self, board: List[str]) -> bool:

        def winning_positions(li_li, x, o):
            c_win, r_win, d_win = 0, 0, 0
            x_win, o_win = False, False
            column = [[] for _ in range(3)]
            for i in range(3):
                if len(set(li_li[i])) == 1 and li_li[i][0] != ' ':
                    r_win += 1
                    if li_li[i][0] == "X":
                        x_win = True
                    else:
                        o_win = True

                column[i].append(li_li[0][i])
                column[i].append(li_li[1][i])
                column[i].append(li_li[2][i])
            for c in column:
                if len(set(c)) == 1 and c[0] != ' ':
                    c_win += 1
                    if c[0] == "X":
                        x_win = True
                    else:
                        o_win = True
            diag1 = li_li[0][0] + li_li[1][1] + li_li[2][2]
            diag2 = li_li[0][2] + li_li[1][1] + li_li[2][0]
            if len(set(diag1)) == 1 and diag1[0] != ' ':
                d_win += 1
                if diag1[0] == "X":
                    x_win = True
                else:
                    o_win = True
            if len(set(diag2)) == 1 and diag2[0] != ' ':
                d_win += 1
                if diag2[0] == "X":
                    x_win = True
                else:
                    o_win = True
            if r_win > 1 or c_win > 1:
                return False
            if x_win and x == o:
                return False
            if o_win and x > o:
                return False
            return True
        x_count = 0
        o_count = 0
        new_board = [[] for _ in range(3)]
        for i, row in enumerate(board):
            for val in row:
                if val == "X":
                    x_count += 1
                elif val == "O":
                    o_count += 1
                new_board[i].append(val)
        if o_count > x_count or x_count > o_count + 1:
            return False
        
        if not winning_positions(new_board, x_count, o_count):
            return False
        return True
