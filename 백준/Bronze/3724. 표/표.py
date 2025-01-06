for t in range(int(input())):
    col,row = map(int,input().split())
    matrix = []
    for i in range(row):
        matrix.append(list(map(int, input().split())))
    maxValue = -float("inf")
    maxcol = 0
    for c in range(col):
        m = 1
        for r in range(row):
            m *= matrix[r][c]
        if m >= maxValue:
            maxValue = m
            maxcol = c
    print(maxcol + 1)