j,n = map(int,input().split())
a = 0
for i in range(n):
    p = input()
    size = 0
    for c in p:
        if c.isupper():
            size += 4
        elif c.islower() or c in "1234567890":
            size += 2
        else:
            size += 1
    if size <= j:
        a += 1
print(a)