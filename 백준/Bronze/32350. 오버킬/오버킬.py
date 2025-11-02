n,d,p = map(int,input().split())
arr = list(map(int,input().split()))
arr.reverse()

t = 0
while arr:
    hp = arr.pop()
    t += 1
    if hp > d:
        arr.append(hp - d)
    else:
        left = ((d-hp)*p)//100
        hp = arr.pop() if arr else 0
        if hp > left:
            arr.append(hp - left)
print(t)