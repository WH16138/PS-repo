N = int(input())
seq = input().strip()
X = list(filter(None, reversed(seq.split("O"))))

if len(X) == 1 and len(X[0])==N:
    print("YES")
    print("-"*N)
    exit()

flag = True
end = ""

ans = []
last = "?"
for s in seq:
    if s == "O":
        ans.append("+")
        last = "O"
    elif s == "X" and last != "X":
        if not X:
            continue
        x = X.pop()
        if last == "?" and seq[-1] == "X":
            e = X.pop(0)
            ex = e+x
            if len(ex)%2:
                string = "+"*(len(ex)//2) + "-"*(len(ex)//2+1)
                end = string[:len(e)]
                ans.append(string[len(e):])
            else:
                flag = False
        else:
            if len(x)%2:
                ans.append("+"*(len(x)//2) + "-"*(len(x)//2+1))
            else:
                flag = False
        last = "X"

ans.append(end)
if flag:
    print("YES")
    print("".join(ans))
else:
    print("NO")