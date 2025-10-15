n = int(input())
arr = []
for i in range(n):
    s,c,t = map(int, input().split())
    arr.append((s,c,t,i+1))
arr.sort(key=lambda x: (-x[0], x[1], x[2]))
print(arr[0][3])