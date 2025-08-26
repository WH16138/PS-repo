P, K = map(int, input().split())

p = 2
result = "GOOD"
while p < K and p <= P**0.5:
    if P%p == 0:
        result = f"BAD {p}"
        break
    p += 1
print(result)
