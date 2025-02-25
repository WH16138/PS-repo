N = int(input())
line = [int(input()) for p in range(N)]
Blist = list(set(line))
maxchain = 0
for b in Blist:
    chain = 0
    last = None
    for i in range(N):
        if line[i] == b:
            continue
        if last == None or chain == 0:
            last = line[i]
            chain += 1
        elif line[i] == last:
            chain += 1
        else:
            last = line[i]
            chain = 1
        maxchain = max(maxchain, chain)
print(maxchain)