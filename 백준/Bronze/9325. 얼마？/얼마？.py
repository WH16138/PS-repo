for t in range(int(input())):
    c = int(input())
    for i in range(int(input())):
        a,b = map(int,input().split())
        c += a*b
    print(c)