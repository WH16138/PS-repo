answer = [0]

for i in range(1,80001):
    if i%3 == 0 or i%7 == 0:
        answer.append(answer[-1]+i)
    else:
        answer.append(answer[-1])

input()
for n in map(int,input().split()):
    print(answer[n])