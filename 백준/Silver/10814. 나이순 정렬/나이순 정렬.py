n=int(input())
a = []
for i in range(n):
    inp = input().split()
    a.append((int(inp[0]),i,inp[1]))
for i in sorted(a):
    print(i[0],i[2])