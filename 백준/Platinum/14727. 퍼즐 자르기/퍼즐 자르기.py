import sys
input = sys.stdin.readline
N = int(input())
histo = [int(input()) for i in range(N)]

def sol(histo):
    n = len(histo)
    if n==1:
        return histo[0]
    elif n == 2:
        return max(histo)
    else:
        a = max(sol(histo[:n//2]),sol(histo[n//2:]))
        l, r = n//2, n//2+1
        h = min(histo[l],histo[r-1])
        while True:
            if l > 0:
                if r < n:
                    if histo[l-1] > histo[r]:
                        l -= 1
                    else:
                        r += 1
                else:
                    l -= 1
            else:
                if r < n:
                    r += 1
                else:
                    break
            h = min(h,histo[l],histo[r-1])
            a = max(a, h*(r-l))
        return a
        
print(sol(histo))