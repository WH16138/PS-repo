n = 0
m = 0
for i in range(10):
    o,i = map(int,input().split())
    n += i - o
    m = max(n,m)
print(m)