for i in range(int(input())):
    p,m = map(int,input().split())
    print(p-len(list(set([int(input()) for _ in range(p)]))))