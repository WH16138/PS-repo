mx,Mx,my,My = float("inf"),-float("inf"),float("inf"),-float("inf")
for i in range(int(input())):
    a,b,c,d = map(int,input().split())
    mx = min(mx,a)
    Mx = max(Mx,c)
    my = min(my,b)
    My = max(My,d)
    print(2*(Mx-mx)+2*(My-my))