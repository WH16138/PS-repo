import sys
input = sys.stdin.readline
t = 0
N,K,L = map(int,input().split())
rating = []
for i in range(N):
    rate = list(map(int,input().split()))
    flag = True
    for r in rate:
        if r < L:
            flag = False
    if sum(rate) < K:
        flag = False
    if flag:
        rating += rate
        t += 1
print(t)
print(" ".join(map(str,rating)))