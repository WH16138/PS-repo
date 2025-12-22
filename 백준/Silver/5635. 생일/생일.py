n = int(input())
arr = sorted([input().split() for i in range(n)], key = lambda x:(int(x[-1]),int(x[-2]),int(x[-3])))
print(arr[-1][0])
print(arr[0][0])