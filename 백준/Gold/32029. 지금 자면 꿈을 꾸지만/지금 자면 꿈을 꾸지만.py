N,A,B = map(int,input().split())
limit = list(map(int,input().split()))
limit.sort()

M = 0
for q in range(N):
    for sleep in range(A):
        a = A
        time = 0
        ans = 0
        for task in range(N):
            if task == q:
                a -= sleep
                time += sleep*B
            if limit[task] >= time+a:
                ans += 1
                time += a
        M = max(M, ans)

print(M)