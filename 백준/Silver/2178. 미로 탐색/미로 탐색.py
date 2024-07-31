import sys

N, M = map(int, input().split())
miro = [[x for x in sys.stdin.readline().strip()] for _ in range(N)]
vis = []
bps = [(0,0)]

search = 1
flag = True
while flag:
    now_bps = bps[:]
    bps = []
    for b in now_bps:
        if b[0]<0 or M<=b[0] or b[1]<0 or N<=b[1] or miro[b[1]][b[0]] == '0' or b in vis:
            continue
        vis.append(b)
        if b == (M-1,N-1):
            flag = False
            print(search)
            break
        else:
            bps.append((b[0]-1,b[1]))
            bps.append((b[0]+1,b[1]))
            bps.append((b[0],b[1]-1))
            bps.append((b[0],b[1]+1))
    search += 1