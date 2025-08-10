import sys, math
n = int(input())
arr = sorted([tuple(map(int, sys.stdin.readline().split())) for _ in range(n)])

def d(a, b):
    return (a[0]-b[0])**2 + (a[1]-b[1])**2

def ClosestPair(l, r):
    if r-l == 2:
        return d(arr[l], arr[l+1])
    if r-l == 3:
        return min(d(arr[l], arr[l+1]), d(arr[l], arr[l+2]), d(arr[l+1], arr[l+2]))
    
    mid = (l+r)//2
    a = min(ClosestPair(l, mid), ClosestPair(mid, r))

    midpoints = []
    for i in range(l, r):
        if (arr[mid][0]-arr[i][0])**2 < a:
            midpoints.append(arr[i])
    midpoints.sort(key=lambda x: x[1])

    for i in range(len(midpoints)-1):
        for j in range(i+1, len(midpoints)):
            if (midpoints[j][1]-midpoints[i][1])**2 > a:
                break
            a = min(a, d(midpoints[i], midpoints[j]))
    return a

print(ClosestPair(0,n))