n = int(input())
arr = list(map(int,input().split()))
ans = 0

for a in arr:
    ans = ans^a
print("koosaga" if ans else "cubelover")