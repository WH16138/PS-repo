n = int(input())
a = 0
for x in range(1,int(n**0.5+1)):
    y = x
    for y in range(x,n+1):
        if x*y > n:
            break
        a += 1
print(a)