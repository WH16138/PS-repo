def solve(s,l,r):
    while l < r:
        if s[l] == s[r]:
            l += 1
            r -= 1
        else:
            return False
    return True

for t in range(int(input())):
    s = input()

    l,r = 0,len(s)-1
    flag = 0
    while l < r:
        if s[l] == s[r]:
            l += 1
            r -= 1
        else:
            can = 0
            if s[l] == s[r-1]:
                if solve(s,l,r-1):
                    can += 1
            if s[l+1] == s[r]:
                if solve(s,l+1,r):
                    can += 1
            if can:
                flag = 1
                break
            else:
                flag = 2
                break
    print(flag)