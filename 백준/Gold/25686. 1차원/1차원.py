def sol(arr):
    if len(arr) == 1:
        return arr
    return sol(arr[::2])+sol(arr[1::2])

print(*sol(list(range(1,(int(input()))+1))))