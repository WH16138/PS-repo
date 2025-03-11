n = int(input())
nums = sorted(list(map(int,input().split())))

can = [(nums[i]+nums[j],i,j) for i in range(n) for j in range(n) if i!= j]
can.sort()

mindiff = float("inf")
for i in range(len(can)-1):
    diff = abs(can[i][0]-can[i+1][0])
    if diff < mindiff and len(set(can[i][1:3]).union(set(can[i+1][1:3]))) == 4:
        mindiff = diff

print(mindiff)