alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
for _ in range(int(input())):
    cnt,t = input().split()
    arr = input().split()
    if t == "C":
        print(" ".join([str(alpha.index(c)+1) for c in arr]))
    else:
        print(" ".join([alpha[int(n)-1] for n in arr]))  