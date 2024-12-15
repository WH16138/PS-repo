x = [0,0,0]
y = [0,0,0]
for i in range(3):
    x[i], y[i] = map(int,input().split())
x.sort()
y.sort()
if x[0]==x[1]:
    a = x[2]
else:
    a = x[0]
if y[0]==y[1]:
    b = y[2]
else:
    b = y[0]

print(a,b)