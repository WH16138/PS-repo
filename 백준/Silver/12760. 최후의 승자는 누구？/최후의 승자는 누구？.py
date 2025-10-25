N,M = map(int,input().split())
cards = [sorted(list(map(int,input().split()))) for i in range(N)]
scores = [0]*N
for i in range(M):
    maxv = max([cards[j][i] for j in range(N)])
    for j in range(N):
        if cards[j][i]==maxv:
            scores[j]+=1
print(" ".join(map(lambda x:str(x+1),filter(lambda x:scores[x]==max(scores), range(N)))))