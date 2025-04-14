N = int(input())

a = list(map(int, input().split()))
b = list(map(int, input().split()))

ans = 2

for i in range(1, N):
    if a[i] == 0:
        if b[i] == 0 or b[i-1] == 0 or (i+1<N and b[i+1] == 0):
            ans = min(ans, 0)
        else:
            ans = min(ans, 1)
    if b[i-1] == 0:
        ans = min(ans, 1)
print(ans)