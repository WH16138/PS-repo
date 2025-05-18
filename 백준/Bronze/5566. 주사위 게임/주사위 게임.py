n, m = map(int,input().split())
board = [int(input()) for i in range(n)]
p = 0
for i in range(1,m+1):
    d = int(input())
    p += d
    if p >= n-1:
        print(i)
        exit()
    p += board[p]
    if p >= n-1:
        print(i)
        exit()