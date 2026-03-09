import sys
input = sys.stdin.readline
n = int(input())
a = sorted(list([int(input()) for _ in range(n)]))
answer = 0
for i in range(1,n-1):
    answer = max(answer,abs(a[0]-2*a[i]+a[i+1]))
for i in range(n-2):
    answer = max(answer,abs(a[i]-2*a[i+1]+a[-1]))
print(answer)