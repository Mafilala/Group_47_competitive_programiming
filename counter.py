k = int(input())
li = input().split()
from collections import Counter
cnt = Counter(li)
captain = list(cnt.most_common()[-1])
print(int(captain[0]
