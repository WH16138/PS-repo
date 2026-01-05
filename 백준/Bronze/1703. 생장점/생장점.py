while 1:
    inp = list(map(int,input().split()))
    a = inp[0]
    if a == 0:
        break
    else:
        c = 1
        for i in range(a):
            c *= inp[i*2+1]
            c -= inp[i*2+2]
        print(c)