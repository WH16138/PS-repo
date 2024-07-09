import sys
from collections import deque

N,L = map(int, input().split())
arr = list(map(int, input().split()))

dq = deque()
for i in range(N):
    while dq and dq[-1][0] >= arr[i]:
        dq.pop()
    dq.append((arr[i], i))
    if dq[0][1] < i-L+1:
        dq.popleft()
    sys.stdout.write(f'{str(dq[0][0])} ')