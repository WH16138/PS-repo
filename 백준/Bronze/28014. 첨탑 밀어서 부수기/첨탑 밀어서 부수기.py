n = input()
arr = list(map(int,input().split()))
a = 1
while len(arr) > 1:
    if arr[-1] >= arr[-2]:
        a += 1
    arr.pop()
print(a)