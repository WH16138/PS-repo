import random
import sys
print = sys.stdout.write

moves = [(1,2),(2,1),(2,-1),(1,-2),(-1,-2),(-2,-1),(-2,1),(-1,2)]
def in_board(x,y,n):
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
    for dx, dy in moves:
        nx, ny = x+dx, y+dy
        if not in_board(nx, ny, n) or board[ny][nx]:continue
        cand.append((deg[ny][nx], nx, ny))
    cand.sort()
    return [(nx, ny) for _, nx, ny in cand]

def sol(n, sx, sy, BACKTRACK_LIMIT):
    board = [[0]*n for i in range(n)]
    deg = [[0]*n for _ in range(n)]
    for yy in range(n):
        for xx in range(n):
            cnt = 0
            for dx,dy in moves:
                nx, ny = xx+dx, yy+dy
                if 0 <= nx < n and 0 <= ny < n:
                    cnt += 1
            deg[yy][xx] = cnt

    x,y, = sx, sy
    path = [(x,y)]
    step = 1
    board[y][x] = step
    for dx,dy in moves:
        nx, ny = x+dx, y+dy
        if 0 <= nx < n and 0 <= ny < n and board[ny][nx] == 0:
            deg[ny][nx] -= 1
    cand_stack = []
    cand_stack.append(find_path(x,y,n,board,deg))

    while step < n*n: # 솔루션 완성까지
        if not cand_stack: # 가능한 경로묶음이 없음
            return False 
        cands = cand_stack[-1]
        if not cands: # 현재 경로에 더 이상 갈 곳이 없음
            if step == 1: # 백트랙 불가
                return False # 뒤주 (노답)
            backtrack_count = 0
            while backtrack_count < BACKTRACK_LIMIT:
                backtrack_count += 1
                last_x, last_y = path.pop()
                board[last_y][last_x] = 0
                for dx,dy in moves:
                    nx, ny = last_x+dx, last_y+dy
                    if 0<= nx < n and 0<=ny<n and board[ny][nx] == 0:
                        deg[ny][nx] += 1
                step -= 1

                if cand_stack: cand_stack.pop()
                if not path:
                    break
                if cand_stack and cand_stack[-1]:
                    break
            if not path:
                return False # 시작부터 노답
            if not cand_stack or not cand_stack[-1]:
                return False

            nx,ny = cand_stack[-1].pop(0)
            step += 1
            board[ny][nx] = step
            for dx,dy in moves:
                mx, my = nx+dx, ny+dy
                if 0<= mx < n and 0<= my < n and board[my][mx] == 0:
                    deg[my][mx] -= 1
            path.append((nx, ny))
            cand_stack.append(find_path(nx,ny,n,board,deg))
            continue
        nx,ny = cands.pop(0)
        step += 1
        board[ny][nx] = step
        for dx,dy in moves:
            mx, my = nx+dx, ny+dy
            if 0 <= mx < n and 0 <= my < n and board[my][mx] == 0:
                deg[my][mx] -= 1
        path.append((nx, ny))
        cand_stack.append(find_path(nx,ny,n,board,deg))
    return path

N = int(input())
start_x, start_y = map(int, input().split())

flag = False
for trial in range(3):
    random.shuffle(moves)
    path = sol(N,start_x-1,start_y-1, 5)
    if path:
        flag = True
        print("\n".join(map(lambda a: f"{a[0]+1} {a[1]+1}", path)))
        break
if not flag:
    print("-1 -1")