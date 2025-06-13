p = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
for _ in range(int(input())):
    a,n = input().split("-")
    print("nice" if abs(sum(p.index(a[i])*26**(2-i) for i in range(3)) - int(n)) <= 100 else "not nice")