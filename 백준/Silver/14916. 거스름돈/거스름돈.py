def sol(n):
    arr = [0,-1,1,-1,2,1,3,2,4,3,2,4]
    cnt = 0
    cnt += max(n-7, 0) // 5
    n -= cnt*5
    if arr[n] == -1:
        return -1
    else:
        return arr[n]+cnt
print(sol(int(input())))