import sys
count = [0]*10001
for _ in range(int(input())):
    count[int(sys.stdin.readline().strip())] += 1
for i,n in enumerate(count[1:],start=1):
    for j in range(n):
        print(i)