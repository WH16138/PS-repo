n = int(input())
s = list(map(int,input().split()))

count = [0]*(n+1)

for num in s:
    if num <= n:
        count[num] += 1

for i in range(n,0,-1):
    if i == count[i]:
        print(i)
        quit()

if count[0] == 0:
    print(0)
else:
    print(-1)