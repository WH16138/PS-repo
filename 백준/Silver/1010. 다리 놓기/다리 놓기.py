import math
for i in range(int(input())):
    a,b = map(int,input().split())
    a,b = min(a,b), max(a,b)
    print(math.factorial(b)//math.factorial(a)//math.factorial(b-a))