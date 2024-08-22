import sys
n = int(input())

tasks = [tuple(map(int, sys.stdin.readline().strip().split())) for _ in range(n)]

tasks.sort(key=lambda x:x[1])

time = 1000000000
while tasks:
    t,s = tasks.pop()
    if s<=time:
        time = (s-t)
    else:
        time -= t
print(time)