N = int(input())
q = 1000000007
a,b = 0,1
for i in range(N):
    a,b = b%q,a+b%q
print(a)