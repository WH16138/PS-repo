n = int(input())
pieces = list(map(int, input().split()))

dp = {0:0}
for h in pieces:
    ndp = dict(dp)
    for dh, small in dp.items():
        # 높게 쌓는 경우
        ndp[dh+h] = max(ndp.get(dh+h, -float("inf")), small)
        # 낮은 쪽에 쌓는 경우
        ndp[abs(dh-h)] = max(ndp.get(abs(dh-h), -float("inf")), small + min(dh,h))
    dp = ndp

print(dp[0] if dp[0] else -1)