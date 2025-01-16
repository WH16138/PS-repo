result = "YES"
T,X = input().split()
N = int(input())
for i in range(N):
    input()
    if X not in input().split():
        result = "NO"
print(result)