n, k = list(map(int, input().split()))
arr = list(map(int, input().split()))
arr.sort()

num = arr[k - 1]
k_ = 0
for nn in arr:
    if nn <= num:
        k_ += 1
if k == 0:
    if arr[0] > 1:
        print(arr[k] - 1)
    else:
        print(-1)
elif k_ > k:
    print(-1)
else:
    print(num)
