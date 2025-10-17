A,B,V = map(int,input().split())
V -= A
d = 1
if V > 0:d += (V-1)//(A-B)+1
print(d)