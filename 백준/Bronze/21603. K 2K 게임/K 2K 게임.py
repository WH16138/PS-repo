N,K = map(int,input().split())
a = []
for i in range(1,N+1):
    if i%10 not in [K%10,(2*K)%10]:
        a.append(str(i))
print(len(a))
print(" ".join(a))