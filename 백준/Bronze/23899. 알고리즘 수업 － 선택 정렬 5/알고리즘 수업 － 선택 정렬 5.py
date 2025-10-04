def select_sort(arr,comp):
    if arr == comp:
        return 1
    for i in range(len(arr)-1, 0, -1):
        maxidx = 0
        maxv = 0
        for j in range(i+1):
            if arr[j] > maxv:
                maxv = arr[j]
                maxidx = j
        arr[maxidx], arr[i] = arr[i], arr[maxidx]
        if arr == comp:
            return 1
    return 0

input()
print(select_sort(list(map(int,input().split())), list(map(int,input().split()))))