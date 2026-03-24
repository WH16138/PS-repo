import sys
sys.setrecursionlimit(10**6)

N, M = map(int, input().split())
campus = [[x for x in sys.stdin.readline().strip()] for _ in range(N)]

i = sum(campus, []).index('I')
vis = [[0]*M for _ in range(N)]
people = 0

def search(x,y):
    global people
    if x<0 or M<=x or y<0 or N<=y or vis[y][x] or campus[y][x] == 'X':
        return
    else:
        vis[y][x] = 1
        if campus[y][x] == 'P':
            people += 1
        search(x-1,y)
        search(x+1,y)
        search(x,y-1)
        search(x,y+1)

search(i%M, i//M)

print(people if people else 'TT')