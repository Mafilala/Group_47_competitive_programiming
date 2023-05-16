from collections import defaultdict
n, e = list(map(int, input().split()))

di = defaultdict(int)
for i in range(e):
    a, b = list(map(int, input().split()))

    di[a] += 1
    di[b] += 1
if not di:
    print("YES")
else:
    edges = di[1]
    for i in range(1, n + 1):
        if edges != di[i]:
            print("NO")
            exit()
    print("YES")
