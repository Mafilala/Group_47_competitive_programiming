from collections import defaultdict
n = int(input())
adj_list = defaultdict(list)
matrix = []

for _ in range(n):
    row = list(map(int, input().split()))
    matrix.append(row)

for i in range(n):
    for j in range(n):
        if matrix[i][j]:
            adj_list[i].append(j + 1)

for i in range(n):
    if adj_list[i]:
        print(len(adj_list[i]), * sorted(adj_list[i]))
