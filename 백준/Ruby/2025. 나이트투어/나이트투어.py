import random
import sys
print = sys.stdout.write

n = int(input())
board = [[0]*n for i in range(n)]

ans = []
x0, y0 = map(int, input().split())

def cal_degree(X,Y):
    global n, board
    coor = [(X+1,Y+2),(X+2,Y+1),(X+2,Y-1),(X+1,Y-2),(X-1,Y-2),(X-2,Y-1),(X-2,Y+1),(X-1,Y+2)]
    degree = 0
    for x,y in coor:
        if 0<=x<n and 0<=y<n and not board[y][x]:
            degree += 1
    return degree

def find_path(X,Y):
    global n, board
    coor = [(X+1,Y+2),(X+2,Y+1),(X+2,Y-1),(X+1,Y-2),(X-1,Y-2),(X-2,Y-1),(X-2,Y+1),(X-1,Y+2)]
    min_degree = 8
    cand = []
    for x,y in coor:
        if not 0<=x<n or not 0<=y<n or board[y][x]:continue
        deg = cal_degree(x,y)
        if deg < min_degree:
            min_degree = deg
            cand = []
        if deg <= min_degree:
            cand.append((x,y))
    return random.choice(cand) if cand else (-1, -1)

for trial in range(5):
    board = [[0]*n for i in range(n)]
    ans = []
    x, y = x0-1, y0-1
    for i in range(1, n*n+1):
        if x == -1 and y == -1:
            break
        board[y][x] = i
        ans.append((x+1,y+1))
        x,y = find_path(x, y)
    
    if len(ans) != n*n: continue
    
    for a in ans:
        print(f"{a[0]} {a[1]}\n")
    exit()
print("-1 -1")