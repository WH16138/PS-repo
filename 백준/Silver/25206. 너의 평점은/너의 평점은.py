d = {'A+':4.5,'A0':4.0,'B+':3.5,'B0':3.0,'C+':2.5,'C0':2.0,'D+':1.5,'D0':1.0,'F':0}
g = 0
b = 0
for i in range(20):
    n,p,s = input().split()
    if s == 'P':continue
    g += d[s]*float(p)
    b += float(p)
print(g/b)