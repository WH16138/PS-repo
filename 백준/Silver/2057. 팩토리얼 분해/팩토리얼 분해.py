import math as m

N = int(input())

if not N:
    print("NO")
    quit()

fac = 0
while m.factorial(fac) <= N:
    fac += 1

for f in range(fac,-1,-1):
    if m.factorial(f) <= N:
        N -= m.factorial(f)

if N:
    print("NO")
else:
    print("YES")