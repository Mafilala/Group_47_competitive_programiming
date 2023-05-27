from collections import defaultdict, deque


n, m = list(map(int, input().split()))
a, b = list(map(int, input().split()))
adj_list = defaultdict(list)
for _ in range(m):
    c, d = list(map(int, input().split()))
    adj_list[c].append(d)
    adj_list[d].append(c)

queue = deque([a])
prev = {a: None}

while queue:
    node = queue.popleft()
    if node == b:
        break
    for neighbour in adj_list[node]:
        if neighbour not in prev:
            prev[neighbour] = node
            queue.append(neighbour)

if b not in prev:
    print(-1)
    exit()
path = []
while b:
    path.append(b)
    b = prev[b]

print(len(path) - 1)
print(*reversed(path))
