for t in range(int(input())):
    input()
    N,M = map(int,input().split())
    S = max(map(int,input().split()))
    B = max(map(int,input().split()))
    if S >= B:
        print('S')
    else:
        print('B')