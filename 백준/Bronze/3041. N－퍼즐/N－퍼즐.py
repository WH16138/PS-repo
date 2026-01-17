n = 0
ans = "ABCDEFGHIJKLMNO."
string = input()+input()+input()+input()
for r in range(4):
    for c in range(4):
        s = string[r*4+c]
        if s ==".":continue
        n += abs(r-ans.index(s)//4) + abs(c-ans.index(s)%4)
print(n)