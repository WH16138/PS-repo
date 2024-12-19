n,p = map(int,input().split())
r = 1
for i in range(2,n+1):
    r *= i
    r %= p
print(r)