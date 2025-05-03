from bisect import bisect_left, bisect_right
from collections import defaultdict
import sys
input = sys.stdin.readline

N = int(input())
pos = [tuple(map(int, input().split())) for _ in range(N)]

x_to_ys = defaultdict(list)
y_to_xs = defaultdict(list)
points = set()
for x, y in pos:
    x_to_ys[x].append(y)
    y_to_xs[y].append(x)
    points.add((x,y))

for ys in x_to_ys.values():
    ys.sort()
for xs in y_to_xs.values():
    xs.sort()

P = int(input())
for _ in range(P):
    x1, y1, x2, y2 = map(int, input().split())

    cnt = 0

    ys = x_to_ys.get(x1, [])
    cnt += bisect_right(ys, y2) - bisect_left(ys, y1)

    ys = x_to_ys.get(x2, [])
    cnt += bisect_right(ys, y2) - bisect_left(ys, y1)

    xs = y_to_xs.get(y1, [])
    cnt += bisect_right(xs, x2) - bisect_left(xs, x1)

    xs = y_to_xs.get(y2, [])
    cnt += bisect_right(xs, x2) - bisect_left(xs, x1)

    for corner in ((x1,y1), (x1,y2), (x2,y1), (x2,y2)):
        if corner in points:
            cnt -= 1

    print(cnt)