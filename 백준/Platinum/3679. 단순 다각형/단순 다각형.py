from functools import cmp_to_key

def ccw(a, b, c):
    return (b[0]-a[0])*(c[1]-a[1]) - (b[1]-a[1])*(c[0]-a[0])

def dist2(a, b):
    dx = a[0]-b[0]
    dy = a[1]-b[1]
    return dx*dx + dy*dy

def sort_by_angle(pts):
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

    if len(others) >= 2:
        last = others[-1]
        k = len(others)-1
        while k-1 >= 0 and ccw(p0, others[k-1], last) == 0:
            k -= 1
        others[k:] = reversed(others[k:])

    return [p0] + others

for i in range(int(input())):
    s = list(map(int,input().split()))
    points = [(a,b,i) for a,b,i in zip(s[1::2],s[2::2],range(s[0]))]
    asorted = sort_by_angle(points)
    print(*[p[2] for p in asorted])