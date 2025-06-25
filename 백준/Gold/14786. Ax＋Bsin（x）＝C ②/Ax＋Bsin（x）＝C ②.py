import sys, math
input = sys.stdin.readline

def cal(a,b,x):
    return a*x + b*math.sin(x)

def solve(a, b, target):
    l, r = 0, 10**6
    for _ in range(100000):
        mid = (l + r) / 2
        if cal(a, b, mid) < target:
            l = mid
        else:
            r = mid
    return l, r

a,b,c = map(int, input().split())
ans = solve(a, b, c) 
print(ans[0])