import sys
from collections import deque

M,N = map(int, input().split()) #y,x

tilemap = [list(map(int,sys.stdin.readline().strip())) for y in range(M)]

vis = [[[0]*N for y in range(M)] for i in range(2)]
bfs = deque([(1,0,0,1)])
while bfs:
    b = bfs.pop()
    if vis[b[3]][b[2]][b[1]]:
        continue
    vis[b[3]][b[2]][b[1]] = 1
    if b[1]==N-1 and b[2]==M-1:
        print(b[0])
        quit()
    for x,y in [(-1,0),(+1,0),(0,-1),(0,+1)]:
        if -1<b[1]+x<N and -1<b[2]+y<M:
            if tilemap[b[2]+y][b[1]+x] and b[3] == 1:
                bfs.appendleft((b[0]+1,b[1]+x,b[2]+y,0))
            elif not tilemap[b[2]+y][b[1]+x]:
                bfs.appendleft((b[0]+1,b[1]+x,b[2]+y,b[3]))
print(-1)