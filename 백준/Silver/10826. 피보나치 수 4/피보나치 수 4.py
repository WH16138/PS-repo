N = int(input())

p = [0,1]
while len(p)<=N:
    p.append(p[-1]+p[-2])
print(p[N])