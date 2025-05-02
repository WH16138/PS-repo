n = int(input())
p = list(map(int,input().split()))
m = 0
cs = 0
sf = 2
for i in p:
    if i > 0:
        cs += 1
        m = max(m,cs)
    else:
        if cs == 0:
            continue
        if sf >= 2:
            sf = 0
        else:
            cs = 0
    sf += 1

print(m)