n = int(input())
nums = list(map(int,input().split()))

def rulefor(a,b,arr):
    for i in range(len(arr)-1):
        if arr[i]*a+b != arr[i+1]:
            return False
    return True

if n == 1:
    print('A')
if n == 2:
    if nums[0]==nums[1]:
        print(nums[0])
    else:
        print('A')
if n >= 3:
    rules = [rule for rule in zip(list(range(-200,201)),[nums[1]-a*nums[0] for a in range(-200,201)])]
    solution = []
    for a,b in rules:
        if rulefor(a,b,nums):
            solution.append(nums[-1]*a+b)

    if len(set(solution)) == 0:
        print('B')
    elif len(set(solution)) == 1:
        print(solution[0])
    else:
        print('A')