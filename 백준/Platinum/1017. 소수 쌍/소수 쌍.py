def sieve_of_eratosthenes(n):
    prime = [True for _ in range(n+1)]
    prime[0] = prime[1] = False
    p = 2
    while (p**2 <= n):
        if (prime[p] == True):
            for i in range(p**2, n+1, p):
                prime[i] = False
        p += 1
    return prime
isPrime = sieve_of_eratosthenes(2000)
N = int(input())
arr = list(map(int, input().split()))
first = arr[0] % 2

A = list(filter(lambda x: x % 2 != first, arr))
B = list(filter(lambda x: x % 2 == first, arr))
if len(A) != len(B):
    print(-1)
    exit()

AtoB = [[] for _ in range(len(A))]
firstCanGoTo = []
for i,a in enumerate(A):
    for j,b in enumerate(B):
        if isPrime[a + b]:
            if j == 0:
                firstCanGoTo.append(i)
            else:
                AtoB[i].append(j)

def dfs(a):
    for b in AtoB[a]:
        if visited[b]:
            continue
        visited[b] = True
        if match[b] == -1 or dfs(match[b]):
            match[b] = a
            return True
    return False

ans = []
for firstA in firstCanGoTo:
    match = [-1] * (N//2) # match[b] = a
    visited = [False] * (N//2) # visited[b]
    match[0] = firstA
    visited[0] = True

    cnt = 1
    for a in range(len(A)):
        if a == firstA:
            continue
        visited = [True]+[False]*(N//2-1)
        if dfs(a):
            cnt += 1
    if cnt != len(A):
        continue
    ans.append(A[firstA])

if not ans:
    print(-1)
else:
    print(" ".join(map(str, sorted(ans))))