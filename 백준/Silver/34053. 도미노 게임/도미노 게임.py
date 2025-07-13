N,M = map(int,input().split())

m = float("inf")
s = 0
for i in range(N):
    for j in map(int,input().split()):
        s += j
        m = min(m,j)

print(s-m)