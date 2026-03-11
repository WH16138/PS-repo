n,m = map(int,input().split())
a = list(map(int,input().split()))
s = 0
for i in range(1,n+1):
    if any(i%d==0 for d in a):
        s += i
print(s)