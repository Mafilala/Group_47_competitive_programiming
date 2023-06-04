tc = int(input())
for _ in range(tc):
    s, l = map(int, input().split())
    stair = list(map(int, input().split()))
    legs = list(map(int, input().split()))
    di = {}

    sortedLegs = sorted(legs)
    start = 0
    end = len(stair)
    psum = 0
    prevStep = 0
    curPtr = 0
    while curPtr < len(legs) and start < end:

        if psum + stair[start] - prevStep <= sortedLegs[curPtr]:
            psum += stair[start]
            prevStep = psum
            start += 1
        else:
            di[sortedLegs[curPtr]] = psum
            curPtr += 1
    ans = []
    for leg in legs:
        if leg in di:
            ans.append(di[leg])
        elif curPtr == len(legs):
            ans.append(psum)
        else:
            ans.append(sum(stair))
    print(*ans)
