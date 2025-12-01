for t in range(int(input())):
    grid = [list(input()) for i in range(3)]
    flag = 0
    xo = input()

    for r in range(3):
        if flag:break
        k = 0
        for c in range(3): 
            if grid[r][c] == xo: k += 1
        if k == 2:
            flag = 1
            for c in range(3):
                grid[r][c] = xo

    for c in range(3):
        if flag:break
        k = 0
        for r in range(3): 
            if grid[r][c] == xo: k += 1
        if k == 2:
            flag = 1
            for r in range(3):
                grid[r][c] = xo
    
    if not flag:
        k = 0
        for i in range(3):
            if grid[i][i] == xo: k += 1
        if k == 2:
            flag = 1
            for i in range(3):
                grid[i][i] = xo

    if not flag:
        k = 0
        for i in range(3):
            if grid[2-i][i] == xo: k += 1
        if k == 2:
            flag = 1
            for i in range(3):
                grid[2-i][i] = xo

    print(f"Case {t+1}:")
    for i in range(3):
        print("".join(grid[i]))