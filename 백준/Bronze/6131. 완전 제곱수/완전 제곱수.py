n = int(input())
ans = 0
for a in range(1,501):
    for b in range(1, 501):
        if a**2 == b**2 + n:
            ans += 1
print(ans)