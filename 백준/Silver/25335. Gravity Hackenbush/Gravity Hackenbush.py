import sys
input = sys.stdin.readline

N,M = map(int,input().split())
for i in range(N):
    input()
R,G,B = 0, 0, 0
for i in range(M):
    _,_,c = input().split()
    if c == "R":
        R += 1
    elif c == "G":
        G += 1
    else:
        B += 1
R += G//2+G%2
B += G//2
print("jhnah917" if R > B else "jhnan917")