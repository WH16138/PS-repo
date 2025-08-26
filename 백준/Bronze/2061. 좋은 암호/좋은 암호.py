K, L = map(int,input().split())
for i in range(2,L):
    if K % i == 0:
        print(f"BAD {i}")
        exit()
print("GOOD")