import heapq as h
import sys
input = sys.stdin.readline

n = int(input())
length = [list(map(int,input().split())) for i in range(n)]
d = int(input())
hos = []
for ho in length:
    if max(ho)-min(ho) <= d:
        hos.append((min(ho), max(ho)))

hos.sort(key=lambda x:x[1])
q = []
maxP = 0
for ho in hos:
    h.heappush(q, ho[0])
    while q[0] < ho[1]-d:
        h.heappop(q)
    maxP = max(len(q),maxP)

print(maxP)