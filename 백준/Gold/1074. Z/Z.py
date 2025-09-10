def sol(n,r,c):
    if n == 0:
        return 1
    if r < 2**(n-1):
        if c < 2**(n-1):
            return sol(n-1, r, c)
        else:
            return 4**(n-1) + sol(n-1, r, c-2**(n-1))
    else:
        if c < 2**(n-1):
            return 2*4**(n-1) + sol(n-1, r-2**(n-1), c)
        else:
            return 3*4**(n-1) + sol(n-1, r-2**(n-1), c-2**(n-1))

print(sol(*map(int, input().split()))-1)