from collections import defaultdict
graph = defaultdict(list)
n = int(input())
k = int(input())
for _ in range(k):
  li = list(map(int, input().split()))
  if li[0] == 1:
    v, u = li[1], li[2]
    graph[v].append(u)
    graph[u].append(v)

  else:
    v = li[-1]
    if graph[v]:
      print(* graph[v])
