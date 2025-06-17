from collections import deque

n,k = map(int, input().split())
a = []
arr = deque(list(range(1, n + 1)))
while len(arr):
    for _ in range(k - 1):
        arr.append(arr.popleft())
    a.append(arr.popleft())

print(f"<{', '.join(map(str, a))}>")