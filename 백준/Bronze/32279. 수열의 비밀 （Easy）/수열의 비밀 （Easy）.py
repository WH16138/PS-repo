n = int(input())
p,q,r,s = map(int,input().split())
a1 = int(input())

arr = [a1]

for i in range(2,n+1):
    if i%2 == 0:
        arr.append(arr[i//2-1]*p+q)
    else:
        arr.append(arr[(i-1)//2-1]*r+s)

print(sum(arr))