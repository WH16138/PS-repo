N,M = map(int,input().split())

a = 1
for i in range(N):
    k = int(input())
    if k:
        a *= k
        a %= M
a %= M
print(a)