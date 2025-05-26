import math
import sys
input = sys.stdin.readline

L = 906150257
R = 906488079
size = R-L+1

Pcnt = [0]*size
number = [L+i for i in range(size)]
OE = ["?"]*size

limit = int(math.isqrt(R))+1
is_prime = [True]*(limit+1)
is_prime[0] = is_prime[1] = False

primes = []
for p in range(2, limit + 1):
    if is_prime[p]:
        primes.append(p)
        for multi in range(p*p, limit + 1, p):
            is_prime[multi] = False

for idx, p in enumerate(primes):
    start = ((L+p-1) // p)*p
    for x in range(start, R+1, p):
        i = x-L
        while number[i] % p == 0:
            number[i] //= p
            Pcnt[i] += 1

for i in range(size):
    if number[i] > 1:
        Pcnt[i] += 1

even = 0
odd = 0
for i, cnt in enumerate(Pcnt):
    if cnt % 2 == 0:
        even += 1
    else:
        odd += 1

    OE[i] = "O" if even >= odd else "E"

exceptions = set([L + idx for idx, v in enumerate(OE) if v == "E"])

for _ in range(int(input())):
    n = int(input())
    if n == 1 or n in exceptions:
        print("E")
    else:
        print("O")