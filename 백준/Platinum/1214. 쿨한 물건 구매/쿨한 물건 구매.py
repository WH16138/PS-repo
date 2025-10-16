D,P,Q = map(int,input().split())
if P < Q:
    P,Q=Q,P
N = min(D//Q, Q)
minv = float("inf")
for n in range(N+1):
    diff = D - n*P
    if diff <= 0:
        m = 0
    else:
        m = (diff-1)//Q+1
    cur = n*P+m*Q
    minv = min(cur,minv)
print(minv)