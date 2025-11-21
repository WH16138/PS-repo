N ,C = map(int,input().split())

x,y = N,N
for i in range(C):
    nx,ny = map(int,input().split())
    if min(x,nx)*y < x*min(y,ny):
        y = min(y,ny)
    else:
        x = min(x,nx)

print(x*y)