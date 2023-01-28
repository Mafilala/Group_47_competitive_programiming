tc = int(input())
for _ in range(tc):
  n = int(input())
  li = list(map(int, input().split()))
  li.sort()
  found = False
  if n == 1:
    print("YES")
    found = True
  else:
    for i in range(1, n):
      v1 = li[i]
      v2 = li[i - 1]
      if abs(v2 - v1) not in [0, 1]:
        print("NO")
        found = True
        break
  if not found:
    print("YES")
