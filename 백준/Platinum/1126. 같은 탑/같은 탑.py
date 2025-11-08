n=int(input())
pieces=list(map(int,input().split()))
dp={0:0}
for h in pieces:
  ndp=dict(dp)
  for dh,small in dp.items():
    ndp[dh+h]=max(ndp.get(dh+h,0),small)
    ndp[abs(dh-h)]=max(ndp.get(abs(dh-h),0),small+min(dh,h))
  dp=ndp
print(dp[0]if dp[0]else -1)