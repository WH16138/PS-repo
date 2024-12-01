n = int(input())
u = input()

if n%2 == 0:
    print("NOT POSSIBLE")
    quit()

case1_1 = u[:n//2]
case1_2 = u[n//2:]
case2_1 = u[:n//2+1]
case2_2 = u[n//2+1:]

def check(a,b):
    if len(a)<len(b):
        a,b = b,a
    for i in range(len(b)):
        if a[i] != b[i]:
            if a[i+1:] == b[i:]:
                return b
            else:
                return False
    return b

sol1 = check(case1_1,case1_2)
sol2 = check(case2_1,case2_2)

if sol1:
    if sol2 == False or sol1 == sol2:
        print(sol1)
    else:
        print("NOT UNIQUE")
elif sol2:
    print(sol2)
else:
    print("NOT POSSIBLE")
