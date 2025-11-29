def sieve_of_eratosthenes(n):
    prime = [True for _ in range(n+1)]
    prime[0] = False
    prime[1] = False
    p = 2
    while (p**2 <= n):
        if (prime[p] == True):
            for i in range(p**2, n+1, p):
                prime[i] = False
        p += 1
    return prime

primes = sieve_of_eratosthenes(318137)
superprimes = [v for i,v in enumerate([p for p in range(2, len(primes)) if primes[p]]) if primes[i+1]]
for t in range(int(input())):
    n = int(input())
    print(superprimes[n-1])