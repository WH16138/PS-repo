alpha = "ABCDEFGHIJ"
AJ = [0]*10
canzero = [1]*10
used = [0]*10

for _ in range(int(input())):
    s = input()
    l = len(s)
    for i,c in enumerate(s):
        AJ[alpha.index(c)] += 10**(l-i-1)
        if i == 0:
            canzero[alpha.index(c)] = 0

result = 0

index = min((i for i in range(10) if canzero[i]),key = lambda x:AJ[x])
AJ[index] = 0

for v in range(9,0,-1):
    index = AJ.index(max(AJ))
    result += v*AJ[index]
    AJ[index] = 0

print(result)