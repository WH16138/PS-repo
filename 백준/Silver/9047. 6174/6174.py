t = int(input())
for i in range(t):
    n = input()
    cnt = 0
    while (int(n) != 6174):
        nlist = list(str(n))
        while len(nlist) < 4:
            nlist.append("0")
        nlist.sort()
        n = int("".join(nlist[::-1])) - int("".join(nlist))
        cnt += 1

    print(cnt)