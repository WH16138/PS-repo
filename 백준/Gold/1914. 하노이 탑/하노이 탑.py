import sys
sys.setrecursionlimit(10000000)

N = int(input())
m = 0
seq = []

def hanoi(n, start, to, via):
    global m
    if n == 1:
        seq.append(f"{start} {to}")
        m += 1
    else:
        hanoi(n-1, start, via, to)
        seq.append(f"{start} {to}")
        m += 1
        hanoi(n-1, via, to, start)

if N <= 20:
    hanoi(N,'1','3','2')
    sys.stdout.write(f'{m}\n' + '\n'.join(seq))
else:
    for i in range(N):
        m = m*2+1
    print(m)