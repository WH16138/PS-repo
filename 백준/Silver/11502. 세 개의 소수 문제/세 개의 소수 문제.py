def sieve_of_eratosthenes(n):
    prime = [True for _ in range(n+1)]
    p = 2
    while (p**2 <= n):
        if (prime[p] == True):
            for i in range(p**2, n+1, p):
                prime[i] = False
        p += 1
    return [p for p in range(2, n+1) if prime[p]]

primes = sieve_of_eratosthenes(1000)
for t in range(int(input())):
    n = int(input())
    for i in primes:
        if i > n:break
        for j in primes:
            if j > n:break
            for k in primes:
                if k > n:break
                if i + j + k == n:
                    print(i, j, k)
                    n = 0