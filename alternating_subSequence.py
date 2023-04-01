tc = int(input())
for _ in range(tc):
    n = int(input())
    li = list(map(int, input().split()))
    mul = 1
    l = 0
    ans1 = []
    ans2 = []
    while l < len(li):
        temp = []
        while l < len(li) and li[l] * mul > 0:
            temp.append(li[l])
            l += 1
        mul *= -1
        if temp:
            ans1.append(max(temp))
    mul = -1
    while l < len(li):
        temp = []
        while l < len(li) and li[l] * mul > 0:
            temp.append(li[l])
            l += 1
        mul *= -1
        if temp:
            ans2.append(max(temp))
    if len(ans1) > len(ans2):
        print(sum(ans1))
    elif len(ans1) < len(ans2):
        print(sum(ans2))
    else:
        print(max(sum(ans1), sum(ans2)))
