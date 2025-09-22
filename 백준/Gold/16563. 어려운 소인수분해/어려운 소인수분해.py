def sieve_of_eratosthenes(n):
    prime = [True for _ in range(n+1)]
    p = 2
    while (p**2 <= n):
        if (prime[p] == True):
            for i in range(p**2, n+1, p):
                prime[i] = False
        p += 1
    return [p for p in range(2, n+1) if prime[p]]

primes = sieve_of_eratosthenes(int(5000000**0.5))
for num in map(int, open(0).read().split()[1:]):
    factors = []
    for prime in primes:
        if prime * prime > num:
            break
        while (num % prime == 0):
            factors.append(prime)
            num //= prime
    if num > 1:
        factors.append(num)
    print(*factors)