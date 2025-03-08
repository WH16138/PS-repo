import heapq as h

k,n = map(int,input().split())

primes = list(map(int,input().split()))

que = primes[::]
result = []
dupcheck = set()
quemax = max(que)

while len(result) < n:
    num = h.heappop(que)
    for p in primes:
        next = p*num
        if next not in dupcheck and not (len(que) >= n and next > quemax):
            dupcheck.add(next)
            h.heappush(que, next)
            quemax = max(quemax, next)
    result.append(num)

print(result[n-1])