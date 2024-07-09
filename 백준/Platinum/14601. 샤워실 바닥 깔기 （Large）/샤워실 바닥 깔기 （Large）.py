k = int(input())
hole = tuple(map(int,input().split()))
hole = (hole[0]-1, (2**k)-hole[1])


grid = [[-1]*(2**k) for i in range(2**k)]
count = 0

def solve(x,y,n,h):
    global count
    if n == 2:
        count += 1
        for dx,dy in ((0,0),(1,0),(0,1),(1,1)):
            if (x+dx,y+dy) != h:
                grid[y+dy][x+dx] = count
    else:
        m = n//2
        count += 1
        num = count
        for X,Y,H in [(x,y,(x+m-1,y+m-1)),(x+m,y,(x+m,y+m-1)),(x,y+m,(x+m-1,y+m)),(x+m,y+m,(x+m,y+m))]:
            if X<=h[0]<X+m and Y<=h[1]<Y+m:
                solve(X,Y,m,h)
            else:
                grid[H[1]][H[0]] = num
                solve(X,Y,m,H)

solve(0,0,2**k,hole)

for line in grid:
    print(' '.join(map(str,line)))