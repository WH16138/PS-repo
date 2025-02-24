N,M,K = map(int,input().split())
for i in range(M):
    t,r = map(int,input().split())
    K -= r
    if K < 0:
        print(i+1, 1)
        quit()
print(-1)