T = [1]
n = 2
while T[-1] < 1000:
    T.append(T[-1]+n)
    n += 1

for test in range(int(input())):
    flag = 0
    n = int(input())
    for i in T:
        if i > n:
            break
        for j in T:
            if j > n:
                break
            for k in T:
                if k > n:
                    break
                if i+j+k == n:
                    flag = 1
                    break
    print(flag)