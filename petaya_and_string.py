inp1 = input().lower()
inp2 = input().lower()
i = 0
while i < len(inp1):
    if inp1[i] > inp2[i]:
        print("1")
        break
    elif inp1[i] < inp2[i]:
        print("-1")
        break
    i += 1
if i == len(inp1):
    print("0")
