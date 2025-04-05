import heapq as h
import sys
input = sys.stdin.readline

left = []
right = []

for i in range(int(input())):
    n = int(input())

    h.heappush(left,-n)
    if right and -left[0] > right[0]:
        h.heappush(right, -h.heappop(left))

    if len(left) > len(right) + 1:
        h.heappush(right, -h.heappop(left))
    elif len(right) > len(left):
        h.heappush(left, -h.heappop(right))
    
    print(-left[0])