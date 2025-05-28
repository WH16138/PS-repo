n = int(input())
arr = list(map(int,input().split()))

xor = 0
for a in arr:
    xor = xor^a

print("koosaga" if xor else "cubelover")