a,m = map(int, input().split())
i = 1
while 1:
    if a*i%m == 1: 
        print(i)
        quit()
    i += 1