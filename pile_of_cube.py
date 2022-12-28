def is_it_possible(arr, n):
    l = n
    i, j = 0, l - 1
    prev = 0
    while i < j:
        l = arr[i]
        r = arr[j]
        if l >= r and (l <= prev or prev == 0):
            prev = arr[i]
            i += 1
        elif r >= l and (r <= prev or prev == 0):
            prev = arr[j]
            j -= 1
        else:
            return "No"
    return "Yes"

N = int(input())
for _ in range(N):
    n = int(input())
    arr = [int(x) for x in input().split()]
    print(is_it_possible(arr, n))
