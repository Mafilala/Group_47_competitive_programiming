from collections import defaultdict
n, m = input().split()
n = int(n)
m = int(m)
n_dict = defaultdict(list)
for i in range(1, n + 1):
    val = input()
    n_dict[val].append(str(i))
for j in range(m):
    val = input()
    if n_dict[val] == []:
        print(-1)
    else:
        print(" ".join(n_dict[val]))
