for t in range(int(input())):
    words = [input() for _ in range(int(input()))]
    flag = 0
    for i,a in enumerate(words):
        if flag:break
        for j,b in enumerate(words):
            if i != j:
                s=a+b
                if s==s[::-1]:
                    print(s)
                    flag=1
                    break
    if not flag:print(0)
