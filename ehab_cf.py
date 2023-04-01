n = int(input())
arr = list(map(int, input().split()))

odd = 0
even = 0

found = False
for n in arr:
    if n % 2 == 0:
        even += 1
    else:
        odd += 1
    if odd > 0 and even > 0:
        found = True
if found:
    print(*sorted(arr))
else:
    print(*arr)
