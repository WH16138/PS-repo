s = 0
for i in range(int(input())):
    a,b = map(int,input().split())
    s += b%a
print(s)