from itertools import combinations
N,K = map(int,input().split())

house = [list(map(int,input().split())) for i in range(N)]

def d(p1,p2):
    return abs(p1[0]-p2[0])+abs(p1[1]-p2[1])

mind = float("inf")
shelterC = list(combinations(house, K))
for shel in shelterC:
    maxd = 0
    for h in house:
        clo = float("inf")
        for s in shel:
            clo = min(clo, d(h,s))
        maxd = max(maxd, clo)
    mind = min(mind, maxd)
print(mind)