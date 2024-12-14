a,d,k = map(int,input().split())
if (k-a)%d:
    print("X")
else:
    print((k-a)//d+1 if (k-a)//d+1>0 else "X")