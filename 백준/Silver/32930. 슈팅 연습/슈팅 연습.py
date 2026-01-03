def dist2(p1,p2):
    return (p1[0]-p2[0])**2+(p1[1]-p2[1])**2
cur = [0,0]
n,m = map(int,input().split())
score = 0
points = [list(map(int,input().split())) for i in range(n)]
for i in range(m):
    points.sort(key=lambda x:dist2(cur,x))
    p = points.pop()
    score += dist2(cur,p)
    cur = p
    points.append(list(map(int,input().split())))
print(score)