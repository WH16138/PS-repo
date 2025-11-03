N,L,R = map(int, input().split())

arr = list(map(int, input().split()))
arr = arr[:L-1] + sorted(arr[L-1:R]) + arr[R:]

flag = 1
for i in range(1, N):
    if arr[i] < arr[i-1]:
        flag = 0
        break
print(flag)