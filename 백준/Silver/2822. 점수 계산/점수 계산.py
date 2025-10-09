scores = []
for i in range(8):
    scores.append(int(input()))
ss = sorted(scores)
print(sum(ss[-5:]))
print(" ".join(map(str,sorted([(scores.index(x)+1) for x in ss[-5:]]))))