import sys
input = sys.stdin.readline
M,m = 0,0
for i in range(int(input())):
    b,s = sorted(list(map(int,input().split())))
    M = max(M,b)
    m = max(m,s)
print(M*m)