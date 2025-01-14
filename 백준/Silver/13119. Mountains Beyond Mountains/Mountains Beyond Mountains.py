N,M,X = map(int,input().split())
mount = list(map(int,input().split()))

for n in range(N,0,-1):
    s = ""
    for i in range(M):
        if n == X:
            if mount[i] < n:
                s += "-"
            else:
                s += "*"
        elif n > X:
            if mount[i] < n:
                s += "."
            else:
                s += "#"
        else:
            if mount[i] < n:
                s += "." if (i+1)%3 else "|"
            else:
                s += "#"
    print(s)
