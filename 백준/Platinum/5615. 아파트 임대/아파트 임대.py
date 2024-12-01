import sys
input = sys.stdin.readline

def miller_rabin(n,a):
    s, d = 0, n-1
    while d%2 == 0:s += 1; d //= 2

    x = pow(a,d,n)
    if x == 1 or x+1 == n: return True
    
    for i in range(0, s-1):
        x = pow(x,2,n)
        if x+1 == n:
            return True
    return False

def is_prime(n):
    A = {2, 7, 61}
    if n in A: return True
    if n == 1 or n%2 ==0: return False
    for a in A:
        if not miller_rabin(n,a): return False
    return True

count = 0
for t in range(int(input())):
    n = int(input())
    if is_prime(2*n+1):
        count += 1
print(count)