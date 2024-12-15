A = [1,2,3,3,4,10]
B = [1,2,2,2,3,5,10]
for t in range(int(input())):
    a = sum([x*y for x,y in zip(A,map(int,input().split()))])
    b = sum([x*y for x,y in zip(B,map(int,input().split()))])
    if a==b:
        print(f"Battle {t+1}: No victor on this battle field")
    elif a > b:
        print(f"Battle {t+1}: Good triumphs over Evil")
    else:
        print(f"Battle {t+1}: Evil eradicates all trace of Good")