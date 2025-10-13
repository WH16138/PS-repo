import random
import sys
print = sys.stdout.write

moves = [(1,2),(2,1),(2,-1),(1,-2),(-1,-2),(-2,-1),(-2,1),(-1,2)]
def in_board(x, y, n):
    return 0<=x<n and 0<=y<n

def cal_dgr(x,y,n,board):
    dgr = 0
    for dx,dy in moves:
        nx,ny = x+dx,y+dy
        if in_board(nx,ny,n) and not board[ny][nx]:
            dgr += 1
    return dgr

def find_path(x,y,n,board,deg):
    cand = []
    cx = (n-1)/2
    cy = (n-1)/2
    for dx, dy in moves:
        nx, ny = x+dx, y+dy
        if not in_board(nx, ny, n) or board[ny][nx]:continue
        dist2 = (nx-cx)*(nx-cx) + (ny-cy)*(ny-cy)
        cand.append((deg[ny][nx], -dist2, nx, ny))
    cand.sort(reverse=True)
    return [(nx, ny) for _, _, nx, ny in cand]

def sol(n, sx, sy):
    board = [[0]*n for i in range(n)]
    deg = [[0]*n for _ in range(n)]
    for yy in range(n):
        for xx in range(n):
            cnt = 0
            for dx,dy in moves:
                nx, ny = xx+dx, yy+dy
                if 0<=nx<n and 0<=ny< n:
                    cnt += 1
            deg[yy][xx] = cnt

    x,y, = sx, sy
    path = [(x,y)]
    step = 1
    board[y][x] = step
    for dx,dy in moves:
        nx, ny = x+dx, y+dy
        if 0<=nx<n and 0<=ny<n and board[ny][nx] == 0:
            deg[ny][nx] -= 1
    cand_stack = []
    cand_stack.append(find_path(x,y,n,board,deg))

    while step < n*n:
        if not cand_stack:
            return False 
        cands = cand_stack[-1]
        if not cands:
            return False
        nx,ny = cands.pop()
        step += 1
        board[ny][nx] = step
        for dx,dy in moves:
            mx, my = nx+dx, ny+dy
            if 0<= mx < n and 0<=my<n and board[my][mx] == 0:
                deg[my][mx] -= 1
        path.append((nx, ny))
        cand_stack.append(find_path(nx,ny,n,board,deg))
    return path

N = int(input())
start_x, start_y = map(int, input().split())

flag = False
for trial in range(3):
    random.shuffle(moves)
    path = sol(N,start_x-1,start_y-1)
    if path:
        flag = True
        print("\n".join(map(lambda a: f"{a[0]+1} {a[1]+1}", path)))
        break
if not flag:
    print("-1 -1")