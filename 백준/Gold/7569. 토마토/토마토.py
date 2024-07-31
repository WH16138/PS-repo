M,N,H = map(int, input().split()) #가로 세로 높이

tomatos = [[[],[]],[[],[]]] #전체 -> 층-> 세로번 가로줄 -> 가로번:요소

tomatos = [[list(map(int,(input().split()))) for y in range(N)] for h in range(H)]

bfs = []
vis = [[[0]*M for y in range(N)] for h in range(H)]

target = 0

for i, t in enumerate(sum(sum(tomatos, []), [])):
    if t == 1:
        bfs.append(((i//(N*M)),(i%(N*M))//M,(i%(N*M))%M))
    if t == 0:
        target += 1

time = 0
while bfs:
    now_bfs = bfs[:]
    bfs = []
    time += 1

    for b in now_bfs:
        if b[0]<0 or H<=b[0] or b[1]<0 or N<=b[1] or b[2]<0 or M<=b[2] or tomatos[b[0]][b[1]][b[2]] == -1 or vis[b[0]][b[1]][b[2]]:
            continue
        if tomatos[b[0]][b[1]][b[2]] == 0:
            target -= 1
        vis[b[0]][b[1]][b[2]] = 1
        bfs.append((b[0]+1,b[1],b[2]))
        bfs.append((b[0]-1,b[1],b[2]))
        bfs.append((b[0],b[1]+1,b[2]))
        bfs.append((b[0],b[1]-1,b[2]))
        bfs.append((b[0],b[1],b[2]+1))
        bfs.append((b[0],b[1],b[2]-1))

if target:
    print(-1)
else:
    print(time-2)