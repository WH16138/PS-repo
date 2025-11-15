for i in range(int(input())):
    ta, tb, va, vb = map(int, input().split())
    ans = float("inf")
    for a in range(va+1):
        ans = min(ans, max(a*ta, (va-a)*ta + vb*tb))
    print(ans)