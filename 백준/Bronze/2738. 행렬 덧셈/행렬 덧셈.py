N,M = map(int,input().split())
A = [list(map(int,input().split())) for i in range(N)]
B = [list(map(int,input().split())) for i in range(N)]
for i in range(N):
    print(" ".join([str(a+b) for a,b in zip(A[i],B[i])]))