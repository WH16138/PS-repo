n = int(input())
minus = False
if n<0:
    minus = True
    n = -n
answer = []

def is_square(n):
    return not bool(n**0.5%1)
def sol(n):
    if is_square(n):
        answer.append(n**0.5)
    elif (n%2):
        answer.extend([(n//2+1),-(n//2)])
    elif not(n%4):
        answer.extend([(n/4+1),-(n/4-1)])
    else:
        for i in range(1,int(n**0.5)+1):
            if is_square(n-i**2):
                answer.extend([i,(n-i**2)**0.5])
                break

if n == 0:
    answer.extend([3,4,-5])
elif n == 2:
    answer.extend([6,-5,-3])
else:
    sol(n)
if not answer:
    answer.append(-1)
    sol(n+1)

answer = [-int(x) if minus else int(x) for x in answer]

if answer:
    print(f"{len(answer)}")
    for n in answer:print(f"{'+' if n>0 else '-'} {abs(n)}")
else:print(-1)