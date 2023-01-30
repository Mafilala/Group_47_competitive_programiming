n, m = list(map(int, input().split()))
row_map = [dict() for _ in range(n)]
col_map = [dict() for _ in range(m)]
grid = []
for i in range(n):
  row = input()
  grid.append(row)
  r_dict = row_map[i]
  for j in range(m):
    c_dict = col_map[j]
    val = row[j]
    r_dict[val] = 1 + r_dict.get(val, 0)
    c_dict[val] = 1 + c_dict.get(val, 0)

for i,li in enumerate(grid):
  for j, ele in enumerate(li):
    if row_map[i][ele] == 1 and col_map[j][ele] == 1:
      print(ele, end='')
