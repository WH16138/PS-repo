import sys
input = sys.stdin.readline
for t in range(int(input())):
    a,b,c = map(int,input().split())
    print(int(min((b+c)**2+a**2,(a+c)**2+b**2,(a+b)**2+c**2)))