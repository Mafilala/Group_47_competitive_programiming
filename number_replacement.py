from collections import defaultdict
test_cases = int(input())
for _ in range(test_cases):
  n = int(input())
  nums = input().split()
  string = input()
  tracker = defaultdict(lambda: -1)
  known = False
  for i in range(n):
    s = nums[i]
    if tracker[s] != -1:
      idx = tracker[s]
      if string[idx] != string[i]:
        print("NO")
        known = True
        break
    else:
      tracker[s] = i
  if not known:
    print("YES")
