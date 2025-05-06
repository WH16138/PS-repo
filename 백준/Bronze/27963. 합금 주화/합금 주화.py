d1, d2, x = map(int,input().split())
M,m= max(d1,d2),min(d1,d2)
V,v = x/M,(100-x)/m
print(100/(V+v))