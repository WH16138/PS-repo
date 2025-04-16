import math
a = []
for i in range(int(input())):
    a.append(min(int(input().replace("0","9",10).replace("6","9",10)), 100))

print(math.ceil(sum(a)/len(a)-0.49999999999))