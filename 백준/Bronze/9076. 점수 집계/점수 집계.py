N = int(input())
for i in range(N):
    arr = list(map(int, input().split()))
    arr.sort()
    if arr[3]-arr[1] >= 4:
        print("KIN")
    else:
        print(sum(arr[1:4]))