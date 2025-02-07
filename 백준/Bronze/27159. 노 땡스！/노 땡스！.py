N = int(input())
nums = sorted(list(map(int,input().split())))
last = 0
score = 0
for n in nums:
    if n > last+1:
        score += n
    last = n
print(score)