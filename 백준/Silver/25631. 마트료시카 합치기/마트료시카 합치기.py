n = int(input())
arr = list(map(int,input().split()))
d = {}
m = 0
for a in arr:
    if a in d.keys():
        d[a] += 1
    else:
        d[a] = 1
    m = max(m, d[a])
print(m)