def solve(x,y,n,h):
    if n == 2:
        color = ("a" if y%4 in (1,2) else "b") if x%4 in (1,2) else ("b" if y%4 in (1,2) else "a")
        for dx,dy in ((0,0),(1,0),(0,1),(1,1)):
            if x+dx != h[0] or y+dy != h[1]:
                grid[y+dy][x+dx] = color
    else:
        m = n//2
        for X,Y,H in [(x,y,(x+m-1,y+m-1)),(x+m,y,(x+m,y+m-1)),(x+m,y+m,(x+m,y+m)),(x,y+m,(x+m-1,y+m))]:
            if X<=h[0]<X+m and Y<=h[1]<Y+m:
                solve(X,Y,m,h)
            else: # 규칙대로 a,b 칠한 후 나머지 전부 c 로 칠함
                grid[H[1]][H[0]] = "c"
                solve(X,Y,m,H)

t, k = map(int,input().split())
for _ in range(t):
    hole = list(map(lambda x:int(x)-1,input().split()))
    hole[0],hole[1] = hole[1],hole[0]
    grid = [["@"]*(2**k) for i in range(2**k)]

    solve(0,0,2**k,hole)

    for line in grid:
        print(''.join(map(str,line)))