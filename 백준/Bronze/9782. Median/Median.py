t = 1
while 1:
    arr = list(map(int,input().split()))
    n = arr[0]
    arr =arr[1:]
    if n == 0:
        break
    median = arr[n//2] if n%2 == 1 else (arr[n//2-1]+arr[n//2])/2
    print(f"Case {t}: {median:.1f}")
    t += 1