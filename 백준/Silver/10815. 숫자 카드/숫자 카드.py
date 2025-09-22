def binary_search(arr, target):
    left, right = 0, len(arr)-1

    while left <= right:
        mid = left + (right-left)//2

        if arr[mid] == target:
            return 1
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return 0

n = int(input())
cards = sorted(list(map(int,input().split())))
m = int(input())
nums = list(map(int,input().split()))

print(*[binary_search(cards, x) for x in nums])