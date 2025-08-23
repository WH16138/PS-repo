s = input().upper()
count = {}
maxc = 0
maxa = "?"
for c in s:
    if count.get(c, 0):
        count[c] = count[c] + 1
    else:
        count[c] = 1
    if count[c] == maxc:
        maxa = "?"
    elif count[c] > maxc:
        maxa = c
        maxc = count[c]

print(maxa)