n = int(input())
a = 0
for i in range(n):
    if "50" in str(i):
        a += 2
    else:
        a += 1
print(a)