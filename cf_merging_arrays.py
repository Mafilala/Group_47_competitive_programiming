n1, n2 = list(map(int, input().split()))
 
l1 = list(map(int, input().split()))
 
l2 = list(map(int, input().split()))
 
ans = []
 
j = 0
for itm in l2:
  while j < n1 and itm > l1[j]:
    j += 1
  ans.append(j)
print(*ans)
