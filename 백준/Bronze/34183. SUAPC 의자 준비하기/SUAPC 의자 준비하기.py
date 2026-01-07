N,M,A,B = map(int,input().split())
d = N*3-M
print(0 if d <= 0 else d*A+B)