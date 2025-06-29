import sys
input = sys.stdin.readline

N = int(input())

stack = []
ans = 0
size = 0
for _ in range(N):
    p = int(input())
    
    while stack and stack[-1][0] < p:
        v,n = stack.pop()
        size -= n
        ans += n

    size += 1
    if stack and stack[-1][0] > p:
        ans += 1

    if stack and stack[-1][0] == p:
        ans += stack[-1][1]
        v, n = stack.pop()
        if stack:ans += 1
        stack.append((v, n + 1))
    else:
        stack.append((p, 1))


print(ans)