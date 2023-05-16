n = int(input())
matrix = [[0 for _ in range(n)] for _ in range(n)]

for i in range(n):
    row = list(map(int, input().split()))
    if row[0]:
        for node in row[1:]:
            matrix[i][node - 1] = 1

for row in matrix:
    print(*row)
