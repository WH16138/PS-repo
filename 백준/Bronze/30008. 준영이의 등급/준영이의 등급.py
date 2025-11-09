N, K = map(int,input().split())
ranks = map(int,input().split())
g = []
for rank in ranks:
    r = rank*100//N
    if r <= 4:g += ["1"]
    elif 4 < r <= 11:g += ["2"]
    elif 11 < r <= 23:g += ["3"]
    elif 23 < r <= 40:g += ["4"]
    elif 40 < r <= 60:g += ["5"]
    elif 60 < r <= 77:g += ["6"]
    elif 77 < r <= 89:g += ["7"]
    elif 89 < r <= 96:g += ["8"]
    elif 96 < r:g += ["9"]
print(" ".join(g))