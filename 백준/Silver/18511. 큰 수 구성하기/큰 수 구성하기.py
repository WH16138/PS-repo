N, K = map(int,input().split())
arr = input().split()

a = 0

s = [""]
while s:
    q = s.pop()
    for v in arr:
        if int(v+q) <= N:
            s.append(v+q)
            a = max(a,int(v+q))
print(a)