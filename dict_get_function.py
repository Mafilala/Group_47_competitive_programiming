n = int(input())
di = dict()
for _ in range(n):
    _inp = input()
    di[_inp] = di.get(_inp, 0) + 1
 
print(len(di))
for i, val in di.items():
    print(va
