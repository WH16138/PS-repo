def miller_rabin(n):
    if n < 2: return False
    if n != 2 and n%2==0: return False
    for p in [2,3,5,7,11,13,17,19,23,29]:
        if n!=p and n%p == 0:
            return False
        
    base = [2,325,9375,28178,450775,9780504,1795265022] #64bit
    d = (n-1)
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
            for i in range(1,r):y = f(y,c,n)
            k = 0
            while k < r and g == 1:
                ys = y
                lim = min(m, r-k)
                for i in range(1,lim):
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

def find_factors(n):
    if n < 2:return []
    factors = []
    arr = [n]
    while arr:
        cur = arr.pop()
        if miller_rabin(cur):
            factors.append(cur)
            continue
        f = pollard_rho(cur)
        arr.extend([cur//f,f])
    return(factors)

import itertools

def find_divisor(n):
    factors = find_factors(abs(n))
    primes = sorted(list(set(factors)))
    exponents = [range(factors.count(p)+1) for p in primes]
    
    divisors = []
    for exp_combo in itertools.product(*exponents):
        val = 1
        for p, e in zip(primes, exp_combo):
            val *= p**e
        divisors.append(val)
    return sorted(divisors)

A,B,C,D = map(int,input().split())

if A == 0:
    if B == 0:
        if C == 0:
            if D == 0: # 0 = 0
                print("INFINITY")
            else: # D = 0
                print(0)
        else:
            if D == 0: # Cy + 0 = 0
                print("INFINITY")
            else: # Cy + D = 0
                if D%C==0:
                    print("INFINITY")
                else:
                    print(0)
    else:
        if C == 0:
            if D == 0: # Bx + 0 = 0
                print("INFINITY")
            else: # Bx + D = 0
                if D%B==0:
                    print("INFINITY")
                else:
                    print(0)
        else:
            if D == 0: # Bx + Cy = 0
                print("INFINITY")
            else: # Bx + Cy + D = 0
                if D%math.gcd(B,C)==0:
                    print("INFINITY")
                else:
                    print(0)
else:# AAxy + ABx + ACy + BC = BC - DA #(Ax+C)(Ay+B) = BC - DA
    N = B*C-D*A
    if N == 0:
        if C%A==0 or B%A==0:
            print("INFINITY")
        else:
            print(0)
    else:
        divisors = find_divisor(N)
        ans = []
        for f in divisors:
            if (f-C)%A == 0 and ((N//f)-B)%A == 0:
                ans.append(((f-C)//A, ((N//f)-B)//A))
            f = -f
            if (f-C)%A == 0 and ((N//f)-B)%A == 0:
                ans.append(((f-C)//A, ((N//f)-B)//A))
        print(len(ans))
        for a in sorted(list(set(ans))):
            print(*a)