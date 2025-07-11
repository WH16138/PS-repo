import sys, bisect
from collections import defaultdict
sys.setrecursionlimit(200000)
input = sys.stdin.readline

N = int(input())
nodes = []
for i in range(N):
    a, lv = map(int, input().split())
    nodes.append((a, lv, i))

nodes.sort()

orig_index = [og for _, _, og in nodes]

level_map = defaultdict(list)
for idx, (_, lv, _) in enumerate(nodes):
    level_map[lv].append(idx)

left = [-1]*N
right = [-1]*N
flag = True

def solve(level = 1, l = 0, r = N):
    global flag
    if l >= r:
        return -1
    pos = level_map.get(level, [])
    L = bisect.bisect_left(pos, l)
    R = bisect.bisect_left(pos, r)
    if R-L != 1:
        flag = False
        return -1
    idx = pos[L]

    orig = orig_index[idx]
    left[orig]  = solve(level+1, l, idx)
    right[orig] = solve(level+1, idx+1, r)
    
    return orig+1

solve(1, 0, N)

if not flag:
    print(-1)
else:
    for i in range(N):
        print(left[i], right[i])
