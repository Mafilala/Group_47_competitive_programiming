test_cases = int(input())
for _ in range(test_cases):
  t1, t2 = input().split()
  s1 = t1[-1]
  s2 = t2[-1]
  deg1 = t1[:-1]
  deg2 = t2[:-1]
  if s1 == s2:
    if s1 == "L":
      if len(deg1) > len(deg2):
        print(">")
      elif len(deg1) < len(deg2):
        print("<")
      else:
        print("=")
    elif s1 == "S":
      if len(deg1) > len(deg2):
        print("<")
      elif len(deg1) < len(deg2):
        print(">")
      else:
        print("=")
    else:
      print("=")
  else:
    if s1 == "L":
      print(">")
    elif s1 == "S":
      print("<")
    else:
      if s2 == "L":
        print("<")
      else:
        print(">")
