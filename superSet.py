superSet = set(input().split())
n = int(input())
result = True
for _ in range(n):
    set_ = set(input().split())
    if len(superSet - set_) == 0 or len(set_ - superSet) > 0:
        result = False
print(result)
    
