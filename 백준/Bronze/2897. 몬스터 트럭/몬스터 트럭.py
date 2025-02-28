row,col = map(int,input().split())
grid = [input() for r in range(row)]

counter = [0,0,0,0,0]

for r in range(row-1):
    for c in range(col-1):
        flag = True
        cnt = 0
        for x in (0,1):
            for y in (0,1):
                if grid[r+x][c+y] == '#':
                    flag = False
                elif grid[r+x][c+y] == 'X':
                    cnt += 1
        if flag:counter[cnt] += 1
for c in counter:
    print(c)