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
#print("Sieve 시작 (2~", limit, ")")
for p in range(2, limit + 1):
    if is_prime[p]:
        primes.append(p)
        for multi in range(p*p, limit + 1, p):
            is_prime[multi] = False
    #if p % (max(limit // 100, 1)) == 0:
        #print(f"Sieve {int(p*100 / limit)}% 완료")
#print("Sieve 완료. 소수 개수:", len(primes))

#print("\n소인수 제거 시작")
for idx, p in enumerate(primes):
    start = ((L+p-1) // p)*p
    for x in range(start, R+1, p):
        i = x-L
        while number[i] % p == 0:
            number[i] //= p
            Pcnt[i] += 1
    # 1% 단위 진행도
    #if idx % (max(len(primes) // 100, 1)) == 0:
    #    print(f"소인수 제거 {idx*100 / len(primes):.1f}% 완료")
#print("소인수 제거 완료")

#print("남은 큰 소인수 처리 시작")
for i in range(size):
    if number[i] > 1:
        Pcnt[i] += 1
    #if i % (max(size // 100, 1)) == 0:
        #print(f"남은 처리 {int(i*100 / size)}% 완료")
#print("남은 큰 소인수 처리 완료")

#print("O/E 판정 시작")
even = 0
odd = 0
for i, cnt in enumerate(Pcnt):
    if cnt % 2 == 0:
        even += 1
    else:
        odd += 1

    OE[i] = "O" if even >= odd else "E"

    #if i % (max(size // 100, 1)) == 0:
        #print(f"판정 {int(i*100 / size)}% 완료")
#print("O/E 판정 완료")
#print(f"총 짝수 : {even}, 홀수 : {odd}")

exceptions = set([L + idx for idx, v in enumerate(OE) if v == "E"])
#print("\nE인 값들 (예외 구간):", exceptions)

#print(len(exceptions))

for _ in range(int(input())):
    n = int(input())
    if n == 1 or n in exceptions:
        print("E")
    else:
        print("O")