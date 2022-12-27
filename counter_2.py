from collections import Counter
n,m=list(map(int, input().split()))
array= input().split()
count = Counter(array)
A=[x for x in input().split()]
B=[x for x in input().split()]
happiness=0
for i in A:
    happiness += count.get(i, 0)  
for i in B:
    happiness -= count.get(i, 0)
print(happiness)  
