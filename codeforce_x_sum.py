tc = int(input())
for _ in range(tc):
  board = []
  r, c = list(map(int, input().split()))
  for i in range(r):
    li = list(map(int, input().split()))
    board.append(li)
  left_d = [0] * (r + c -1)
  right_d = [0] * (r + c -1)
  max_ = 0
  for i in range(r):
    for j in range(c):
      val = board[i][j]
      left_d[j - i] += val
      right_d[i + j] += val
  for i in range(r):
    for j in range(c):
      val = board[i][j]
      x_sum = left_d[j - i] + right_d[j + i] - val
      max_ = max(max_, x_sum)
  print(max_)
