def gcd_cnt(x,y):
    if y == 1:
        return (x-1)
    if x%y == 0:
        return float("inf")
    x, y = max(x,y), min(x,y)
    q = (x-1) // y
    r = x - q*y
    return gcd_cnt(y, r) + q

def gcd_make(x,y,f) -> str:
    if y == 1:
        return "XY"[int(f)]*(x-1)
    x, y = max(x,y), min(x,y)
    q = (x-1) // y
    r = x - q*y
    return gcd_make(y, r, not f) + "XY"[int(f)]*q

n = int(input())
if n == 1:
    print("")
    exit()
min_cnt = float("inf")
a = None
for i in range(1,n):
    cnt = gcd_cnt(n, i)
    if cnt == min_cnt:
        na = gcd_make(n, i, 0)
        if na[0] == "Y":na = "".join("X" if c == "Y" else "Y" for c in na)
        if a == None or na < a:
            a = na
    elif cnt <= min_cnt:
        min_cnt = cnt
        na = gcd_make(n, i, 0)
        if na[0] == "Y":na = "".join("X" if c == "Y" else "Y" for c in na)
        a = na
print(a[:-1]+"X")