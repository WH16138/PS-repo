from functools import cmp_to_key

def ccw(a, b, c):
    return (b[0]-a[0])*(c[1]-a[1]) - (b[1]-a[1])*(c[0]-a[0])

def dist2(a, b):
    dx = a[0]-b[0]
    dy = a[1]-b[1]
    return dx*dx + dy*dy

def sort_by_angle(points):
    pts = list(set(points))
    p0 = min(pts, key=lambda p: (p[1],p[0]))
    others = [p for p in pts if p != p0]

    def cmp(a, b):
        t = ccw(p0, a, b)
        if t > 0:
            return -1
        if t < 0:
            return 1
        da = dist2(p0, a)
        db = dist2(p0, b)
        if da < db:
            return -1
        if da > db:
            return 1
        return 0

    others.sort(key=cmp_to_key(cmp))
    return [p0] + others

def convex_hull_graham(points):
    asorted_points = sort_by_angle(points)
    hull = [asorted_points[0]]
    for p in asorted_points[1:]:
        while len(hull) >= 2 and ccw(hull[-2],hull[-1],p) <= 0:
            hull.pop()
        hull.append(p)
    return hull

n = int(input())
points = [tuple(map(int,input().split())) for i in range(n)]

print(len(convex_hull_graham(points)))