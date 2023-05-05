tc = int(input())
for _ in range(tc):
    n = int(input())
    li = list(map(int, input().split()))
    ref = []
    num_of_two = 0
    for idx, num in enumerate(li):
        while num > 1 and num % 2 == 0:
            num_of_two += 1
            num /= 2
            li[idx] = num
        index = idx + 1
        possible = False
        twos = 0
        temp = li[idx] * index
        while index > 1 and temp % 2 == 0:
            possible = True
            twos += 1
            temp /= 2
        if possible:
            ref.append(twos)
        if num_of_two >= n:
            break
    if num_of_two >= n:
        print(0)
    elif num_of_two < n:
        ops = 0
        ref.sort(reverse=True)
        while num_of_two < n:
            for v in ref:
                num_of_two += v
                ops += 1
                if num_of_two >= n:
                    break
            break
        if num_of_two >= n:
            print(ops)
        else:
            print(-1)
