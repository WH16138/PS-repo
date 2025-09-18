def miller_rabin(n):
    if n < 2: return False
    if n != 2 and n%2==0: return False
    for p in [2,3,5,7,11,13,17,19,23,29]:
        if n != p and n%p == 0:
            return False
        if n == p:
            return True
        
    base = [2,325,9375,28178,450775,9780504,1795265022] #64bit
    d = n-1
    s = 0
    while d%2 == 0:
        d //= 2
        s += 1
    for a in base:
        if a % n == 0:
            continue
        x = pow(a,d,n)
        if x == 1 or x == n-1:continue
        
        composite = True
        for _ in range(s-1):
            x = x*x % n
            if x == n-1:
                composite = False
                break
        if composite:return False
    return True

import random
import math

def pollard_rho(n):
    if n%2==0:return 2
    if n%3==0:return 3

    def f(x,c,n):return (x**2+c) % n
    
    while True:
        y = random.randrange(1,n)
        c = random.randrange(1,n)

        m = 128
        r = 1
        q, g = 1, 1

        x = y
        y = (y*y+c) % n
        while g == 1:
            x = y
            for i in range(r):y = f(y,c,n)
            k = 0
            while k < r and g == 1:
                ys = y
                lim = min(m, r-k)
                for i in range(lim):
                    y = f(y,c,n)
                    q = (q*abs(x-y))%n
                g = math.gcd(q,n)
                k += lim
            r *= 2

        if g == n:
            g = 1
            while g == 1:
                ys = f(ys,c,n)
                g = math.gcd(abs(x-ys), n)
        
        if g > 1 and g < n:
            return g
        
N = int(input())
nums = [N]
arr = []
while nums:
    n = nums.pop()
    if n == 1:
        continue
    if miller_rabin(n):
        arr.append(n)
        continue
    p = pollard_rho(n)
    n //= p
    nums.append(p)
    nums.append(n)

def euler_phi(n, factors):
    result = 1
    for p in list(set(factors)):
        if n % p == 0:
            a = 0
            while n % p == 0:
                n //= p
                a += 1
            result *= p**a - p**(a - 1)
    if n > 1:
        result *= n - 1
    return result

print(euler_phi(N, arr))