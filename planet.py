from collections import Counter
test_cases = int(input())
for _ in range(test_cases):
  num, cost = list(map(int, input().split()))
  orbit = Counter(input().split())
  total_cost = 0
  for key, value in orbit.items():
    if value >= cost:
      total_cost += cost
    else:
      total_cost += value
  print(total_cost)
