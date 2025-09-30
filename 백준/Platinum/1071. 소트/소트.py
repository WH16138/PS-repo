N = int(input())
arr = list(map(int, input().split()))
count = [0]*1001
for i in arr:
    count[i] += 1
arr = sorted(list(set(arr)))
ans = []

def use(idx):
    x = arr[idx]
    count[x] -= 1
    if count[x] == 0:
        arr.pop(idx)
    return x

while arr:
    if not ans:
        ans.append(use(0))

    else:
        if ans[-1] + 1 == arr[0]:
            if len(arr) == 1:
                i = len(ans)-1
                while i >= 0 and ans[i]+1 == arr[0]:
                    i -= 1
                ans.insert(i+1,use(0))
            else:
                ans.append(use(1))
        else:
            ans.append(use(0))

print(*ans)