def seive_of_eratosthenes(n):
    prime = [1 for _ in range(n+1)]
    p = 2
    while (p**2 <= n):
        if (prime[p]):
            for i in range(p**2, n+1, p):
                prime[i] = 0
        p += 1
    return [p for p in range(2, n+1) if prime[p]]

def euler_phi(n):
    result = 1
    for p in seive_of_eratosthenes(int(n**0.5)+1):
        if n % p == 0:
            a = 0
            while n % p == 0:
                n //= p
                a += 1
            result *= p**a - p**(a-1)
    return result * (n - 1) if n > 1 else result

N = int(input())
print(euler_phi(N))