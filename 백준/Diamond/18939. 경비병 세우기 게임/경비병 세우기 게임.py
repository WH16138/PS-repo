import sys
input = sys.stdin.readline

for t in range(int(input())):
    n,m,k = map(int, input().split())
    b = (k-1)*2
    c = (n-b)*(m-b)
    print("Yuto" if ((n-b)<=1 and (m-b)<=1) or c%2 else "Platina")