R,C = map(int,input().split())

dist = [[n,0] for n in range(1,10)]
for r in range(R):
    line = input()
    for n in range(1,10):
        index = line.find(str(n))
        if index != -1:
            dist[n-1][1] = index

dist.sort(key=lambda x: x[1], reverse=True)
rank = 0
ranking = [0]*9

lastdist = -1
for d in dist:
    if lastdist!=d[1]:rank += 1
    ranking[d[0]-1] = rank
    lastdist = d[1]

for r in ranking:
    print(r)