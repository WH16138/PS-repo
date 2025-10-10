l = [int(input()) for i in range(9)]
s = sum(l)
for x1 in range(9):
    for x2 in range(9):
        if x1 != x2 and s - l[x1] - l[x2] == 100:
            print("\n".join(map(str, sorted(l[:x1]+l[x1+1:x2]+l[x2+1:]))))
            quit()