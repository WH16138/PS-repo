import sys
input = sys.stdin.readline

n,x = map(int,input().split())

A, _ = map(int,input().split())
v = A
for i in range(n):
    v = (v*x)%(10**9+7)
    A, _ = map(int,input().split())
    v += A
print(v%(10**9+7))