N,M = map(int,input().split())

trash = [list() for y in range(N)]

for y in range(N):
    for i,v in enumerate(input().split()):
        if v == '1':
            trash[y].append(i)

robot = 0
for y in range(N):
    if trash[y]:
        robot += 1
        x = 0
        for y2 in range(y,N):
            if trash[y2] and x <= trash[y2][-1]:
                newx = trash[y2][-1]
                while trash[y2] and x <= trash[y2][-1]:
                    trash[y2].pop()
                x = newx
print(robot)