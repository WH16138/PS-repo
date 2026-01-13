s,m=0,float("inf")
for i in range(7):
    a = int(input())
    if a%2:
        s += a
        m = min(a,m)
if s > 0:
    print(s)
    print(m)
else:
    print(-1)