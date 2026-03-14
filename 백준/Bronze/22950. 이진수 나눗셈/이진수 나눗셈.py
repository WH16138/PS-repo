n = int(input())
m = input()
k = int(input())
print("YES" if int(m) == 0 or n-len(m.rstrip("0")) >= k else "NO")