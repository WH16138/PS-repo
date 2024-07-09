import sys
input = sys.stdin.readline

n,m = map(int,input().split())
arr = list(map(int, input().split()))
sorted_arr = sorted((v,i+1) for i,v in enumerate(arr))
for q in range(m):
	i,j,k = map(int,input().split())
	cnt = 0
	temp = -10**9
	for v,idx in sorted_arr:
		if i<=idx<=j:
			cnt += 1
			temp = max(temp, v)
		if cnt == k:
			print(temp)
			break