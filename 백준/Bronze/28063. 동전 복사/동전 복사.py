N = int(input())
x,y = map(int, input().split())
if N == 1:
    print(0)
    exit()
if x == 1 or x==N:
    if y == 1 or y==N:
        print(2)
    else:
        print(3)
elif y == 1 or y==N:
    print(3)
else:
    print(4)