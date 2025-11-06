while True:

    nx,ny,w = map(float, input().split())
    nx = int(nx)
    ny = int(ny)

    if nx == 0 and ny == 0 and w == 0:
        break

    x = list(map(float, input().split()))
    y = list(map(float, input().split()))

    x.sort()
    y.sort()

    xbool = True
    ybool = True
    for i in range(nx-1):
        if x[i] + w < x[i+1]:
            xbool = False
            break
    for i in range(ny-1):
        if y[i] + w < y[i+1]:
            ybool = False
            break
    if x[0] -w/2 > 0 or x[-1] + w/2 < 75:
        xbool = False
    if y[0] -w/2 > 0 or y[-1] + w/2 < 100:
        ybool = False

    print("YES" if xbool and ybool else "NO")
