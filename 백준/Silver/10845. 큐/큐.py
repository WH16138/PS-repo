from collections import deque
import sys

N = int(input())

que = deque([])
for i in range(N):
    c = list(sys.stdin.readline().split())
    if c[0] == 'push':
        que.append(c[1])
    elif c[0] == 'pop':
        if que:
            print(que.popleft())
        else:
            print(-1)
    elif c[0] == 'size':
        print(len(que))
    elif c[0] == 'empty':
        print(1 if len(que) == 0 else 0)
    elif c[0] == 'front':
        if que:
            print(que[0])
        else:
            print(-1)
    elif c[0] == 'back':
        if que:
            print((que[-1]))
        else:
            print(-1)