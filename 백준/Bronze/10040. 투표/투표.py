N,M = map(int,input().split())
cost = [int(input()) for i in range(N)]
vote = [0]*N

for _ in range(M):
    s = int(input())
    for i,c in enumerate(cost):
        if c <= s:
            vote[i] += 1
            break

print(vote.index(max(vote))+1)