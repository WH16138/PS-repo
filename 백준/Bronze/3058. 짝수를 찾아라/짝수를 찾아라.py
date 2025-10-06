for i in range(int(input())):
    arr = list(map(int,input().split()))
    even = []
    for n in arr:
        if n%2==0:even.append(n)
    print(sum(even),min(even))