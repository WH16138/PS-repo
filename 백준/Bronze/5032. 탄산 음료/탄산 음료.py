e,f,c = map(int,input().split())
b = e+f
a = 0
while b >= c:
    add = b//c
    a += add
    b %= c
    b += add
print(a)