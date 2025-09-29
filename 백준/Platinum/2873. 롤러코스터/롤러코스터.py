R,C = map(int,input().split())
arr = [list(map(int,input().split())) for _ in range(R)]
ans = ""
if C % 2:
    ans += "D"*(R-1)
    for i in range(C//2):
        ans += "R" + "U"*(R-1) + "R" + "D"*(R-1)
elif R % 2:
    ans += "R"*(C-1)
    for i in range(R//2):
        ans += "D" + "L"*(C-1) + "D" + "R"*(C-1)
else:
    minV = 1000
    minR = 0
    minC = 0
    for i in range(R*C):
        r = i // C
        c = i % C
        if (r + c) % 2 == 1 and arr[r][c] < minV:
            minV = arr[r][c]
            minR = r
            minC = c
    left = minC // 2
    right = (C-1-minC) // 2
    up = minR // 2
    down = (R-1-minR) // 2
    for i in range(left):
        ans += "D" *(R-1) + "R" + "U"*(R-1) + "R"
    ans += "RDLD" * up
    ans += "DR" if minC%2 else "RD"
    ans += "DLDR" * down
    for i in range(right):
        ans += "R" + "U"*(R-1) + "R" + "D"*(R-1)
print(ans)