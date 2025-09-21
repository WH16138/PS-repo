def sol(x,y,n):
    if n == 1:
        return arr[0][0]
    elif n == 2:
        return sorted(arr[x+dx][y+dy] for dx,dy in zip([0,1,0,1],[0,0,1,1]))[1]
    else:
        dn = n//2
        return sorted(sol(x+dx,y+dy,dn) for dx,dy in zip([0,dn,0,dn],[0,0,dn,dn]))[1]

N = int(input())
arr = [list(map(int,input().split())) for i in range(N)]
print(sol(0,0,N))