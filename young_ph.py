n = int(input())
xyz = [0, 0, 0]
for i in range(n):
    x, y, z = map(int, input().split())
    xyz[0] += x
    xyz[1] += y
    xyz[2] += z
    
if set(xyz) == {0}:
    print("YES")
else:
    print("NO")
