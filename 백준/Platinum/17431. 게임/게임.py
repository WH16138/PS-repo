def gcd_cnt(x,y,f):
    if y == 1:
        return "BR"[int(f)]*(x-1)
    if x%y == 0:
        return "X"
    x, y = max(x,y), min(x,y)
    q = (x-1) // y
    r = x - q*y
    return gcd_cnt(y, r, not f) + "BR"[int(f)]*q

for t in range(int(input())):
    n = int(input())
    min_cnt = float("inf")
    min_v = ""
    for i in range(1,n):
        result = gcd_cnt(n, i, 0)
        if result[0] == "X":
            continue
        if len(result) < min_cnt:
            min_v = result
            min_cnt = len(result)
    print(min_v)