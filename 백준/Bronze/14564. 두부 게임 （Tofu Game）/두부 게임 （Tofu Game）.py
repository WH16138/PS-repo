N,M,A = map(int,input().split())

flag = A
while True:
    call = int(input())
    if call == M//2+1:
        break
    else:
        flag += call - (M//2+1)
        if flag <= 0:
            flag += N
        if flag > N:
            flag -= N
        print(flag)
print(0)