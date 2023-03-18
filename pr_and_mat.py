tc = int(input())
for _ in range(tc):
    m, p = list(map(int, input().split()))
    max_ = (m + p) // 4
    min_ = min(m, p)
    if min_ >= max_:
        print(max_)
    else:
        print(min_)
